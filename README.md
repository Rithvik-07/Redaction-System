# 🛡 Document Redaction & Anonymization System

##  Abstract
This project presents a hybrid NLP-based document anonymization system that detects and protects sensitive information in text documents using Named Entity Recognition (NER), rule-based detection, and document processing techniques.

The system supports multiple file formats and ensures privacy preservation while maintaining document structure and readability.

---

##  Objective
To design an intelligent system that automatically detects and anonymizes sensitive information such as names, emails, phone numbers, and financial data in documents.

---

##  System Overview

The system is built using a hybrid pipeline combining:

- Microsoft Presidio framework
- spaCy `en_core_web_lg` NLP model
- Rule-based regex detection
- Document parsing libraries

---

##  Key Techniques

### 1. Named Entity Recognition (NER)
- Uses spaCy model for context-aware entity detection
- Identifies PERSON, ORGANIZATION, LOCATION, etc.

### 2. Pattern-Based Detection
- Regular expressions for:
  - Emails
  - Phone numbers
  - Credit card numbers
  - IP addresses

### 3. Document Processing
- PDF extraction: PyMuPDF
- Word extraction: python-docx
- Preserves structure and formatting

---

##  System Features

-  Multi-format support (PDF, DOCX, TXT)
-  Three anonymization modes:
  - Redaction (black box masking)
  - Replacement (<EMAIL>, <PERSON>)
  - Highlighting (non-destructive marking)
-  Streamlit-based user interface
-  Download processed documents

---

##  Workflow

1. User uploads document via Streamlit UI  
2. File is parsed using format-specific extractors  
3. Text is sent to Presidio + spaCy NER pipeline  
4. Entities are detected and classified  
5. Selected anonymization method is applied  
6. Output document is regenerated  
7. User downloads processed file  

---

##  Datasets Used

- CoNLL-2003 (NER benchmark dataset)
- i2b2 Clinical Dataset (medical entity detection)
- Enron Email Dataset (real-world communication data)
- Custom legal and financial dataset

---

##  Technologies Used

- Python
- spaCy
- Microsoft Presidio
- PyMuPDF
- python-docx
- Streamlit

---

##  Future Improvements

- Multilingual entity detection
- Cloud-based processing
- Advanced transformer-based NER (BERT)
- Pseudonymization policies
- API deployment

---

##  Author
Rithvik Manohar
