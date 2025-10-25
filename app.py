from flask import Flask, request, jsonify
from flask_cors import CORS
import pytesseract
from PIL import Image
import io
import logging
from classifier import classify_document

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for Spring Boot backend

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'ml-service'}), 200

@app.route('/api/process', methods=['POST'])
def process_document():
    """
    Process uploaded document:
    1. Extract text using OCR (Tesseract)
    2. Classify document type
    3. Return results
    """
    try:
        # Check if file is present in request
        if 'file' not in request.files:
            logger.error("No file in request")
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            logger.error("Empty filename")
            return jsonify({'error': 'Empty filename'}), 400
        
        logger.info(f"Processing file: {file.filename}")
        
        # Read image from file
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert RGBA to RGB if needed (for PNG with transparency)
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        
        # Perform OCR (Finnish + English)
        logger.info("Extracting text with Tesseract OCR...")
        extracted_text = pytesseract.image_to_string(image, lang='fin+eng')
        
        if not extracted_text or len(extracted_text.strip()) == 0:
            logger.warning("No text extracted from image")
            extracted_text = ""
        
        logger.info(f"Extracted {len(extracted_text)} characters")
        
        # Classify document
        logger.info("Classifying document...")
        document_type, confidence = classify_document(extracted_text)
        
        logger.info(f"Classification result: {document_type} (confidence: {confidence})")
        
        # Prepare response
        response = {
            'extractedText': extracted_text,
            'documentType': document_type,
            'confidence': confidence
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        logger.error(f"Error processing document: {str(e)}", exc_info=True)
        return jsonify({'error': f'Processing failed: {str(e)}'}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    logger.info("Starting ML Service on port 5000...")
    app.run(host='0.0.0.0', port=5000, debug=True)