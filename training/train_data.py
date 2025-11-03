"""
Training data for document classification.
Simple synthetic dataset for demonstration.
"""

# Invoice examples
INVOICE_TEXTS = [
    "INVOICE Invoice Number: INV-2024-001 Date: January 15, 2024 Bill To: ABC Company Amount Due: 1,500.00 EUR Payment Terms: Net 30 Total Amount: 1,500.00",
    "LASKU Laskun numero: 12345 Päivämäärä: 15.1.2024 Loppusumma: 2,300.00 EUR Eräpäivä: 15.2.2024 Viitenumero: 1234567890",
    "Invoice #5678 Amount: $1,200.00 Due Date: 2024-02-01 Subtotal: 1,000.00 VAT (20%): 200.00 Total: 1,200.00",
    "FAKTURA Fakturanummer: F-2024-123 Totalt belopp: 850 EUR Förfallodatum: 2024-03-15",
    "BILL Invoice Date: 2024-01-20 Customer: XYZ Ltd Total Amount: 3,450.00 Payment Due: 30 days Reference: REF123456",
    "Lasku Maksaja: Yritys Oy Summa: 567.89 EUR ALV 24%: 136.29 EUR Yhteensä: 704.18 EUR",
    "RECHNUNG Rechnungsnummer: R-2024-456 Gesamtbetrag: 2,100.00 EUR Zahlungsfrist: 14 Tage",
    "Invoice No: 9999 Description: Professional Services Total: 5,000.00 USD Payment Terms: Due on receipt",
    "Myyntilasku Laskun pvm: 10.1.2024 Viitenro: 98765 Yhteensä maksettavaa: 1,234.56 EUR",
    "INVOICE Customer Invoice Date: Jan 15, 2024 Amount: 890.00 EUR VAT: 178.00 Total: 1,068.00",
]

# Contract examples
CONTRACT_TEXTS = [
    "EMPLOYMENT CONTRACT This Employment Agreement entered into on January 1, 2024 between Employer and Employee Terms of employment Salary Benefits Effective Date Signature",
    "TYÖSOPIMUS Tämä työsopimus tehdään työnantajan ja työntekijän välille Tehtävänimike Palkkaus Alkamispäivä Allekirjoitukset",
    "SERVICE AGREEMENT This Agreement is entered into between Company A and Company B Terms and Conditions Services to be provided Payment terms Validity period",
    "SOPIMUS Osapuolet Sopimuskausi Sopimusehdot Allekirjoitukset ja päiväys",
    "RENTAL AGREEMENT Property address Rent amount Duration of lease Tenant obligations Landlord obligations Signatures",
    "VUOKRASOPIMUS Vuokranantaja Vuokralainen Vuokra-aika Vuokran määrä Allekirjoitukset",
    "NON-DISCLOSURE AGREEMENT Confidential information Protection of trade secrets Term of agreement Jurisdiction Signatures",
    "CONSULTING AGREEMENT Consultant services Fees and payment Intellectual property Term and termination Signatures",
    "PARTNERSHIP AGREEMENT Partners Profit sharing Responsibilities Term Dissolution procedure Signatures",
    "SALASSAPITOSOPIMUS Luottamukselliset tiedot Velvollisuudet Voimassaoloaika Allekirjoitukset",
]

# Receipt examples
RECEIPT_TEXTS = [
    "RECEIPT Store: SuperMart Date: 2024-01-15 Items: Bread 2.50 Milk 1.80 Total: 4.30 EUR Payment: Cash Thank you!",
    "KUITTI Kauppa: K-Market Päivä: 15.1.2024 Maito 1.50 Leipä 2.00 Yhteensä: 3.50 EUR Kiitos käynnistä!",
    "Sale Receipt Store: TechShop Item: USB Cable 12.99 Tax: 2.60 Total: 15.59 USD Card payment",
    "KASSAKUITTI MyShop Date: 2024-01-20 Product A: 5.00 Product B: 8.50 Sum: 13.50 EUR Cash",
    "Restaurant Receipt Table 5 Date: 2024-01-18 Pizza 12.00 Drink 3.50 Total: 15.50 EUR Service included",
    "OSTOKUITTI Marketin nimi Date: 20.1.2024 Tuote 1: 4.50 Tuote 2: 6.00 Yht: 10.50 EUR Korttimaksu",
    "Gas Station Receipt Date: 2024-01-22 Fuel: 45.00 EUR Payment: Debit card Thank you for your visit",
    "RECEIPT Pharmacy Date: 2024-01-25 Medicine: 15.80 Total: 15.80 EUR Paid",
    "Coffee Shop Receipt Date: 2024-01-16 Latte: 4.50 Muffin: 3.00 Total: 7.50 EUR",
    "MYYNTIKUITTI Ruokakauppa Päivä: 18.1.2024 Hedelmät: 3.20 Vihannekset: 4.80 Yht: 8.00 EUR",
]

# ID Document examples
ID_DOCUMENT_TEXTS = [
    "PASSPORT Republic of Finland Passport Number: FIN123456 Name: Matti Meikäläinen Date of Birth: 01.01.1990 Place of Birth: Helsinki Valid until: 2034",
    "DRIVER LICENSE Finland License Number: 12345678 Name: Liisa Virtanen Date of Birth: 15.05.1985 Valid until: 2035 Categories: B, BE",
    "IDENTITY CARD Personal Identity Number: 010190-123A Name: Kalle Korhonen Date of Birth: 01.01.1990 Issued: 2024",
    "HENKILÖKORTTI Suomi Nimi: Marja Mäkinen Henkilötunnus: 150585-456B Voimassa: 2034",
    "AJOKORTTI Numero: AJ-123456 Nimi: Pekka Pouta Syntymäaika: 20.03.1980 Luokat: A, B",
    "PASSPORT United Kingdom Number: UK987654 Surname: Smith Given Names: John Date of Birth: 10.10.1975",
    "Personalausweis Deutschland Name: Schmidt Vorname: Anna Geburtsdatum: 25.12.1992 Gültig bis: 2034",
    "HENKILÖTODISTUS Nimi: Virtanen Etunimi: Ville Henkilötunnus: 101075-789C",
    "DRIVING LICENCE Number: DL-456789 Name: Brown Sarah Date of Birth: 05.05.1988 Valid: 2035",
    "PASSI Numero: P123456 Nimi: Nieminen Matti Syntymäaika: 12.06.1995",
]

# Other/Unknown examples
OTHER_TEXTS = [
    "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore",
    "Meeting notes: Discussed project timeline Next steps Follow-up meeting scheduled",
    "Shopping list: Milk Bread Eggs Butter Coffee Sugar",
    "Random text without any clear structure or purpose just some words together",
    "Email: Hello, How are you? Best regards, John",
    "Muistiinpanot: Tehtävä 1 Tehtävä 2 Tehtävä 3",
    "Dear Sir or Madam, I am writing to inquire about...",
    "The quick brown fox jumps over the lazy dog",
    "Weather forecast: Sunny tomorrow Temperature 20 degrees",
    "Kirje: Hyvä vastaanottaja, Kiitos viestistänne...",
]

def get_training_data():
    """
    Returns training data as (texts, labels) tuple.
    """
    texts = (
        INVOICE_TEXTS + 
        CONTRACT_TEXTS + 
        RECEIPT_TEXTS + 
        ID_DOCUMENT_TEXTS + 
        OTHER_TEXTS
    )
    
    labels = (
        ['INVOICE'] * len(INVOICE_TEXTS) +
        ['CONTRACT'] * len(CONTRACT_TEXTS) +
        ['RECEIPT'] * len(RECEIPT_TEXTS) +
        ['ID_DOCUMENT'] * len(ID_DOCUMENT_TEXTS) +
        ['OTHER'] * len(OTHER_TEXTS)
    )
    
    return texts, labels

if __name__ == '__main__':
    texts, labels = get_training_data()
    print(f"Training data: {len(texts)} samples")
    print(f"Classes: {set(labels)}")
    
    # Print distribution
    from collections import Counter
    distribution = Counter(labels)
    print("\nClass distribution:")
    for label, count in distribution.items():
        print(f"  {label}: {count} samples")