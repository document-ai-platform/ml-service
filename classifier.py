"""
ML-based document classifier using trained scikit-learn model.
Falls back to rule-based classification if model not available.
"""

import os
import pickle
import logging

logger = logging.getLogger(__name__)

# Try to load trained model
MODEL_PATH = 'training/models/document_classifier.pkl'
model = None

try:
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        logger.info(f"✓ Loaded ML model from {MODEL_PATH}")
    else:
        logger.warning(f"⚠ Model not found at {MODEL_PATH}, using rule-based fallback")
except Exception as e:
    logger.error(f"✗ Error loading model: {e}")
    model = None

def classify_document_ml(text):
    """
    Classify document using trained ML model.
    
    Args:
        text (str): Extracted text from OCR
        
    Returns:
        tuple: (document_type, confidence)
    """
    if not text or len(text.strip()) == 0:
        return 'UNKNOWN', 0.0
    
    try:
        # Predict
        prediction = model.predict([text])[0]
        
        # Get confidence (probability)
        probabilities = model.predict_proba([text])[0]
        confidence = float(max(probabilities))
        
        logger.info(f"ML Classification: {prediction} (confidence: {confidence:.2%})")
        
        return prediction, round(confidence, 2)
        
    except Exception as e:
        logger.error(f"ML classification error: {e}")
        # Fall back to rule-based
        return classify_document_rules(text)

def classify_document_rules(text):
    """
    Rule-based classification as fallback.
    
    Args:
        text (str): Extracted text from OCR
        
    Returns:
        tuple: (document_type, confidence)
    """
    if not text or len(text.strip()) == 0:
        return 'UNKNOWN', 0.0
    
    text_lower = text.lower()
    
    # Define keywords for each document type
    invoice_keywords = [
        'lasku', 'invoice', 'laskun', 'total', 'loppusumma', 
        'yhteensä', 'amount', 'viitenumero', 'reference', 
        'eräpäivä', 'due date', 'alv', 'vat', 'faktura', 'rechnung'
    ]
    
    contract_keywords = [
        'sopimus', 'contract', 'allekirjoitus', 'signature',
        'osapuoli', 'party', 'sopimusehto', 'terms',
        'voimassaolo', 'validity', 'agreement', 'vertrag'
    ]
    
    receipt_keywords = [
        'kuitti', 'receipt', 'kassakuitti', 'cash register',
        'ostoskuitti', 'myyntikuitti', 'sale receipt', 'thank you',
        'kiitos', 'beleg'
    ]
    
    id_document_keywords = [
        'henkilötunnus', 'personal id', 'passi', 'passport',
        'ajokortti', 'driver', 'henkilökortti', 'id card',
        'identity', 'personalausweis', 'license'
    ]
    
    # Count keyword matches
    invoice_score = sum(1 for kw in invoice_keywords if kw in text_lower)
    contract_score = sum(1 for kw in contract_keywords if kw in text_lower)
    receipt_score = sum(1 for kw in receipt_keywords if kw in text_lower)
    id_score = sum(1 for kw in id_document_keywords if kw in text_lower)
    
    # Determine document type based on highest score
    scores = {
        'INVOICE': invoice_score,
        'CONTRACT': contract_score,
        'RECEIPT': receipt_score,
        'ID_DOCUMENT': id_score
    }
    
    # Get type with highest score
    max_score = max(scores.values())
    
    if max_score == 0:
        return 'OTHER', 0.5
    
    document_type = max(scores, key=scores.get)
    
    # Calculate confidence based on score
    confidence = min(0.5 + (max_score * 0.15), 0.95)
    
    logger.info(f"Rule-based classification: {document_type} (confidence: {confidence:.2%})")
    
    return document_type, round(confidence, 2)

def classify_document(text):
    """
    Main classification function.
    Uses ML model if available, otherwise falls back to rules.
    
    Args:
        text (str): Extracted text from OCR
        
    Returns:
        tuple: (document_type, confidence)
    """
    if model is not None:
        return classify_document_ml(text)
    else:
        return classify_document_rules(text)

# For testing
if __name__ == '__main__':
    test_texts = [
        "LASKU\nLaskun numero: 12345\nLoppusumma: 100.00 EUR\nEräpäivä: 31.12.2024",
        "SOPIMUS\nTämä sopimus tehdään osapuolten välillä...\nAllekirjoitus:",
        "KASSAKUITTI\nKiitos ostoksestasi!\nYhteensä: 25.50 EUR",
        "PASSPORT Republic of Finland Number: FIN123456",
        "Some random text without keywords"
    ]
    
    print("Testing classifier:")
    print("=" * 60)
    for text in test_texts:
        doc_type, confidence = classify_document(text)
        print(f"\nText: {text[:50]}...")
        print(f"Type: {doc_type}, Confidence: {confidence}")
    print("=" * 60)