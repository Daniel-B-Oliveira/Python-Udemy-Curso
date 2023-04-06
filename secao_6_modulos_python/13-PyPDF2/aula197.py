# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

ROOT_FOLDER = Path(__file__).parent

ORIGINAL_FOLDER = ROOT_FOLDER / 'PDFs_originais'
NEW_FOLDER = ROOT_FOLDER / 'new_files'
BACEN_REPORT = ORIGINAL_FOLDER / 'R20230331.pdf'

NEW_FOLDER.mkdir(exist_ok=True)

reader = PdfReader(BACEN_REPORT)

# print(len(reader.pages))

# for page in reader.pages:
#     print(page)
#     print('\n\n\n')

page0 = reader.pages[0]
image0 = page0.images[0]

# print(page0.extract_text())
# with open(NEW_FOLDER / page0.images[0].name, 'wb') as image:
#     image.write(page0.images[0].data)

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(NEW_FOLDER / f'page{i}.pdf' ,'wb') as file:
        writer.add_page(page)
        writer.write(file)


files = [
    NEW_FOLDER / 'page0.pdf',
    NEW_FOLDER / 'page1.pdf',
]

merger = PdfMerger()
for file in files:
    merger.append(file)  # type: ignore

merger.write(NEW_FOLDER / 'MERGED.pdf')  # type: ignore
merger.close()