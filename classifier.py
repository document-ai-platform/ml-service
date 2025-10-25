"""
Simple rule-based document classifier.
In production, this would be replaced with a trained ML model.
"""

def classify_document(text):
    """
    Classify document based on extracted text.
    
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
        'eräpäivä', 'due date', 'alv', 'vat'
    ]
    
    contract_keywords = [
        'sopimus', 'contract', 'allekirjoitus', 'signature',
        'osapuoli', 'party', 'sopimusehto', 'terms',
        'voimassaolo', 'validity'
    ]
    
    receipt_keywords = [
        'kuitti', 'receipt', 'kassakuitti', 'cash register',
        'ostoskuitti', 'myyntikuitti', 'sale receipt'
    ]
    
    id_document_keywords = [
        'henkilötunnus', 'personal id', 'passi', 'passport',
        'ajokortti', 'driver', 'henkilökortti', 'id card'
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
    # Higher score = higher confidence, max confidence ~0.95
    confidence = min(0.5 + (max_score * 0.15), 0.95)
    
    return document_type, round(confidence, 2)


# For testing
if __name__ == '__main__':
    # Test cases
    test_texts = [
        "LASKU\nLaskun numero: 12345\nLoppusumma: 100.00 EUR\nEräpäivä: 31.12.2024",
        "SOPIMUS\nTämä sopimus tehdään osapuolten välillä...\nAllekirjoitus:",
        "KASSAKUITTI\nKiitos ostoksestasi!\nYhteensä: 25.50 EUR",
        "Some random text without keywords"
    ]
    
    for text in test_texts:
        doc_type, confidence = classify_document(text)
        print(f"Text: {text[:50]}...")
        print(f"Type: {doc_type}, Confidence: {confidence}\n")