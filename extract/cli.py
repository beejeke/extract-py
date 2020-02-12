# -*- coding=utf-8 -*-
"""
Command Line Interface for Extract-py.
"""

import re
import sys
import os
import time

import click

from extract import create_app
from extract.model import CamdexData, Patient, db


app = create_app()
app.app_context().push()

# ODT to TXT converter


@click.group()
def cli():
    pass


@cli.command(help="Realiza una conversión de formato (.odt a .txt) y elimina líneas vacías")
@click.argument("in_filename")
def convert(in_filename):

    os.system('./odt2txt.sh ' + in_filename)

    print('\nFilename: ' + in_filename)
    time.sleep(0.5)
    print("[...]")
    time.sleep(0.5)
    print("[...]")
    time.sleep(0.5)
    print("[...]")
    time.sleep(1)
    print(f'>>> ODT file converted to .txt ✅\n\n ')


def remove_empty_lines(in_filename):
    if not os.path.isfile(in_filename):
        print("{} does not exist ".format())
        return
    with open(in_filename) as filehandle:
        lines = filehandle.readlines()

    with open(in_filename, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)


# Parser and extract method for txt files


@cli.command(help="Realiza una extracción a medida de los datos personales del paciente")
@click.argument("in_filename")
def patient(in_filename):
    if not os.path.exists(in_filename):
        print("ERROR: Input file does not exist ❌\n\n ")
        sys.exit()

    with open(in_filename) as file:
        lines = file.readlines()

    with open(in_filename, 'w') as file:
        lines = filter(lambda x: x.strip(), lines)
        file.writelines(lines)

    with open(in_filename, 'r') as file:
        rows = file.readlines()
        for row in rows:
            row.strip()
            if re.match('D/Dña', row):
                row_parse = row.strip()
                add_name = row_parse[7:]
                break

    with open(in_filename, 'r') as file:
        rows = file.readlines()
        for row in reversed(rows):
            row.strip()
            if re.match('Dirección', row):
                row_parse = row.strip()
                add_address = row_parse[10:]
                break
            elif re.match('Tfno', row):
                row_parse = row.strip()
                add_phone = row_parse[5:]
            elif re.match('Edad', row):
                row_parse = row.strip()
                add_age = row_parse[6:-20]
                add_dni = row_parse[19:]
            elif re.match('F.N.', row):
                row_parse = row.strip()
                add_birth = row_parse[6:]
        extract_patient = Patient(name=add_name,
                                  address=add_address,
                                  phone=add_phone,
                                  age=add_age,
                                  dni=add_dni,
                                  birthdate=add_birth
                                  )
        db.session.add(extract_patient)
        db.session.commit()

        print(extract_patient)
        time.sleep(0.5)
        print("Extracting and parsing patient personal data[...]")
        time.sleep(0.5)
        print("[...]")
        time.sleep(0.5)
        print("[...]")
        time.sleep(0.5)
        print("[...]")
        time.sleep(1)
        print(f'>>> Personal info for patient "{add_name}" was added ✅\n\n ')


@cli.command(help="Realiza una extracción a medida de los datos del examen CAMDEX del paciente")
@click.argument("in_filename")
def camdex(in_filename):

    if not os.path.exists(in_filename):
        print("ERROR: Input file does not exist ❌\n\n ")
        sys.exit()
    with open(in_filename, encoding="utf-8") as file:
        for line in file:
            if re.match('D/Dña', line):
                add_data = []
                x = line[7:]
                add_data.append(x.strip('\n'))
            elif re.match('MMSE', line):
                x = file.readline()
                parse = x[:-4]
                add_data.append(parse.strip('\n'))
            elif re.match('MEC', line):
                x = file.readline()
                parse = x[:-4]
                add_data.append(parse.strip('\n'))
            elif re.match('Test de', line):
                x = file.readline()
                parse = x[:-4]
                add_data.append(parse.strip('\n'))
            elif re.match('Camcog', line):
                x = file.readline()
                parse = x[:-5]
                add_data.append(parse.strip('\n'))
            elif re.match('Orientación', line):
                x = file.readline()
                parse = x[:-4]
                add_data.append(parse.strip('\n'))
            elif re.match('Lenguaje total', line):
                x = file.readline()
                parse = x[:-4]
                add_data.append(parse.strip('\n'))
            elif re.match('Lenguaje comprensivo', line):
                x = file.readline()
                parse = x[:-3]
                add_data.append(parse.strip('\n'))
            elif re.match('Lenguaje productivo', line):
                x = file.readline()
                parse = x[:-4]
                add_data.append(parse.strip('\n'))
            elif re.match('Memoria total', line):
                x = file.readline()
                parse = x[:-4]
                add_data.append(parse.strip('\n'))
            elif re.match('Memoria reciente', line):
                x = file.readline()
                parse = x[:-3]
                add_data.append(parse.strip('\n'))
            elif re.match('Memoria remota', line):
                x = file.readline()
                parse = x[:-3]
                add_data.append(parse.strip('\n'))
            elif re.match('Memoria de', line):
                x = file.readline()
                parse = x[:-4]
                add_data.append(parse.strip('\n'))
            elif re.match('Atención y', line):
                x = file.readline()
                parse = x[:-3]
                add_data.append(parse.strip('\n'))
            elif re.match('Praxis', line):
                x = file.readline()
                parse = x[:-4]
                add_data.append(parse.strip('\n'))
            elif re.match('Cálculo', line):
                x = file.readline()
                parse = x[:-3]
                add_data.append(parse.strip('\n'))
            elif re.match('Pensamiento abstracto', line):
                x = file.readline()
                parse = x[:-3]
                add_data.append(parse.strip('\n'))
            elif re.match('Percepción', line):
                x = file.readline()
                parse = x[:-4]
                add_data.append(parse.strip('\n'))

        extract_camdex = CamdexData(patient_name=add_data[0],
                                    mmse=add_data[1],
                                    mec=add_data[2],
                                    ryh=add_data[3],
                                    ct=add_data[4],
                                    ori=add_data[5],
                                    lt=add_data[6],
                                    lc=add_data[7],
                                    lp=add_data[8],
                                    mt=add_data[9],
                                    mrec=add_data[10],
                                    mrem=add_data[11],
                                    ma=add_data[12],
                                    ac=add_data[13],
                                    pr=add_data[14],
                                    cal=add_data[15],
                                    pabs=add_data[16],
                                    ptv=add_data[17]
                                    )
        db.session.add(extract_camdex)
        db.session.commit()

        print(extract_camdex)
        time.sleep(0.5)
        print("Extracting and parsing patient CAMDEX data[...]")
        time.sleep(0.5)
        print("[...]")
        time.sleep(0.5)
        print("[...]")
        time.sleep(0.5)
        print("[...]")
        time.sleep(1)
        print(f'>>> CAMDEX data for patient "{add_data[0]}" was added ✅\n\n ')


if __name__ == "__main__":
    sys.exit(cli())