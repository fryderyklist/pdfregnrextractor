import fitz
import re
import glob
import csv
import time
import logging

def create_csv_header():
    csv_writer = csv.writer(csv_file, delimiter=';',
                           quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(["Pzn", "Registrierungsnummer"])
    return csv_writer


def extract_data_for_pdfs():
    for pdf_name in pdfs:
        extract_data_for_pdf(pdf_name)


def extract_data_for_pdf(pdf_name):
    doc = fitz.open(pdf_name)
    for page in doc:
        try:
            text = page.get_text("text")
            write_data_to_csv(text, pdf_name)
        except Exception as e:
            logging.error("Fehler beim lesen der Datei: " + pdf_name)
            pass


def write_data_to_csv(text, pdf_name):
    rx_registration_nr = re.findall(r"Registrierungsnummer: (\w-\d*)", text)
    if rx_registration_nr:
        rx_pzn = re.findall(r"(\d+)", pdf_name)
        csv_writer.writerow([rx_pzn[0], rx_registration_nr[0]])


if __name__ == '__main__':
    start = time.time()
    pdfs = glob.glob("./pdfs/*")
    with open('registrierungsnummern.csv', 'w', newline='') as csv_file:
        csv_writer = create_csv_header()
        extract_data_for_pdfs()
    end = time.time()
    print(f"Runtime for extracting all pdfs in dir ./pdfs is {end - start}")


