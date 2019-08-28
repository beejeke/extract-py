import pypandoc
import re
import sys
import os

from extract import create_app
from extract.model import CamdexData, Patient, db

app = create_app()
app.app_context().push()

# ODT to TXT converter


def convert():
    output_file = 'apd29.txt'
    cout = pypandoc.convert_file('apd29.odt', 'plain', outputfile=output_file)
    assert cout ==""
    print(f'ODT file converter to "{output_file}"')


# Parser and extract method for txt files


convert()
#extract_patient('apd29.txt')
#extract_camdex('apd29.txt')
