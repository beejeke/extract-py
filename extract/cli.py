# -*- coding=utf-8 -*-
"""
Command Line Interface for Extract-py.
"""

import pypandoc
import re
import sys
import os

import click

from extract import create_app
from extract.model import CamdexData, Patient, db


app = create_app()
app.app_context().push()

# ODT to TXT converter


@click.group()
def cli():
    pass


@cli.command(help="Realiza una conversión de formato (.odt a .txt)")
@click.argument("in_filename")
def convert(in_filename):
    output_file = in_filename[:-4] + '.txt'
    cout = pypandoc.convert_file(in_filename, 'plain', outputfile=output_file)
    assert cout ==""
    print(in_filename)
    print(f'>>> ODT file converted to "{output_file}" ✅')


# Parser and extract method for txt files


@cli.command(help="Realiza una extracción a medida de los datos personales del paciente")
@click.argument("in_filename")
def patient(in_filename):
    if not os.path.exists(in_filename):
        print("ERROR: Input file does not exist ❌ ")
        sys.exit()

    with open(in_filename, 'r') as file:
        rows = file.readlines()
        for row in reversed(rows):
            if re.match('D/DÑA', row):
                row_parse = row.strip()
                add_name = row_parse[7:]
                break
            elif re.match('Dirección', row):
                row_parse = row.strip()
                add_address = row_parse[11:]
            elif re.match('Tfno', row):
                row_parse = row.strip()
                add_phone = row_parse[6:]
            elif re.match('F.N.', row):
                row_parse = row.strip()
                add_birth = row_parse[6:]
        extract_patient = Patient(name=add_name,
                                  address=add_address,
                                  phone=add_phone,
                                  birthdate=add_birth
                                  )
        db.session.add(extract_patient)
        db.session.commit()

        print(extract_patient)
        print(f'>>> Personal info for patient "{add_name}" was added ✅')


@cli.command(help="Realiza una extracción a medida de los datos del examen CAMDEX del paciente")
@click.argument("in_filename")
def camdex(in_filename):
    with open(in_filename, 'r') as file:
        rows = file.readlines()
        for row in reversed(rows):
            if re.match('D/DÑA', row):
                row_parse = row.strip()
                add_name = row_parse[7:]
                break
            elif re.match('  MMSE', row):
                row_parse = row.strip().replace(" ", "")
                add_mmse = row_parse[4:-3]
            elif re.match('  MEC', row):
                row_parse = row.strip().replace(" ", "")
                add_mec = row_parse[3:-3]
        extract_camdex = CamdexData(patient_name=add_name,
                                    mmse=add_mmse,
                                    mec=add_mec
                                    )
        db.session.add(extract_camdex)
        db.session.commit()

        print(extract_camdex)
        print(f'>>> CAMDEX data for patient "{add_name}" was added ✅')


if __name__ == "__main__":
    sys.exit(cli())