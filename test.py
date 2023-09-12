import PyPDF2
import spacy

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")


def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_reader = PyPDF2.PdfFileReader(pdf_path)
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()
    return text

class PDF:
    path = ""
    text = ""
    def __init__(self, path):
        self.path = path
        self.text = extract_text_from_pdf(path)

def find_best_match(user_input, pdf_collection):
    best_match = ""
    best_sentence = ""
    best_similarity = 0

    # Process user input
    user_doc = nlp(user_input)

    # Iterate through PDF texts and find the best match
    # for pdf in pdf_collection:
    #     pdf_text = pdf.text
    #     sentences = [s.replace("\n","") for s in pdf_text.split(". ")]
    #     for sentence in sentences:
    #         pdf_doc = nlp(pdf_text)
    #         similarity = user_doc.similarity(pdf_doc)
    #         if similarity > best_similarity:
    #             best_similarity = similarity
    #             best_match = pdf.path
    #             best_sentence = sentence
    for pdf in pdf_collection:
        pdf_doc = nlp(pdf.text)
        similarity = user_doc.similarity(pdf_doc)
        print(pdf.path, ":", similarity)#DEBUG
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = pdf.path

    return best_match, best_sentence, best_similarity
