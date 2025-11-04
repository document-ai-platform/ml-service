"""
Train document classifier using scikit-learn.
"""

import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from train_data import get_training_data

def train_classifier():
    """
    Train document classification model.
    """
    print("=" * 60)
    print("Training Document Classifier")
    print("=" * 60)
    
    # Load training data
    print("\n1. Loading training data...")
    texts, labels = get_training_data()
    print(f"   Total samples: {len(texts)}")
    print(f"   Classes: {set(labels)}")
    
    # Split data
    print("\n2. Splitting data (80% train, 20% test)...")
    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.2, random_state=42, stratify=labels
    )
    print(f"   Training samples: {len(X_train)}")
    print(f"   Test samples: {len(X_test)}")
    
    # Create pipeline
    print("\n3. Creating ML pipeline...")
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(
            max_features=1000,
            ngram_range=(1, 2),  # Unigrams and bigrams
            min_df=1,
            stop_words='english'
        )),
        ('classifier', MultinomialNB(alpha=0.1))
    ])
    
    # Train model
    print("\n4. Training model...")
    pipeline.fit(X_train, y_train)
    print("   ✓ Model trained!")
    
    # Evaluate on test set
    print("\n5. Evaluating on test set...")
    test_score = pipeline.score(X_test, y_test)
    print(f"   Accuracy: {test_score:.2%}")
    
    # Cross-validation
    print("\n6. Cross-validation (5-fold)...")
    cv_scores = cross_val_score(pipeline, texts, labels, cv=5)
    print(f"   CV Accuracy: {cv_scores.mean():.2%} (+/- {cv_scores.std() * 2:.2%})")
    
    # Detailed classification report
    print("\n7. Detailed metrics:")
    y_pred = pipeline.predict(X_test)
    print(classification_report(y_test, y_pred))
    
    # Confusion matrix
    print("\n8. Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred, labels=pipeline.classes_)
    print(f"   Classes: {pipeline.classes_}")
    print(cm)
    
    # Test predictions
    print("\n9. Testing predictions...")
    test_samples = [
        ("INVOICE Total: 100 EUR Due date: 2024-02-01", "INVOICE"),
        ("SOPIMUS Tämä sopimus tehdään osapuolten välillä", "CONTRACT"),
        ("RECEIPT Store: Shop Total: 5.50 EUR", "RECEIPT"),
        ("Random text here", "OTHER"),
    ]
    
    for text, expected in test_samples:
        prediction = pipeline.predict([text])[0]
        proba = pipeline.predict_proba([text])[0]
        confidence = max(proba)
        match = "✓" if prediction == expected else "✗"
        print(f"   {match} Text: '{text[:40]}...'")
        print(f"      Predicted: {prediction} (confidence: {confidence:.2%})")
        print(f"      Expected: {expected}")
    
    # Save model
    print("\n10. Saving model...")
    model_path = 'models/document_classifier.pkl'
    with open(model_path, 'wb') as f:
        pickle.dump(pipeline, f)
    print(f"   ✓ Model saved to {model_path}")
    
    print("\n" + "=" * 60)
    print("Training complete!")
    print("=" * 60)
    
    return pipeline

if __name__ == '__main__':
    train_classifier()