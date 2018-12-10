import xml.etree.ElementTree as ET
import os, argparse

LOGO = ""\
"    _____________  ___  _____  .____   __________\n" \
"   /   _____/\   \/  / /     \ |    |  \______   \ \n" \
"   \_____  \  \     / /  \ /  \|    |   |       _/\n" \
"   /        \ /     \/    Y    \    |___|    |   \ \n" \
"  /_______  //___/\  \____|__  /_______ \____|_  /\n" \
"          \/       \_/       \/        \/      \/ \n"\
"\nSELECTOR EXTENSIBLE MARKUP LANGUAGE REPLACER TOOL v0.1\n"\
"December 10, 2018\n"\
"Author: Bastian Muhlhauser\n"

print(LOGO)

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Especificar la carpeta donde se encuentran los archivos a procesar", metavar='PATH')
parser.add_argument("-r", "--replace", help="Especificar el texto que reemplazará al original", metavar='REPLACEMENT')
parser.add_argument("-e", "--element", help="Especificar el elemento o entidad en la cual se reemplazará el contenido (default: path)", metavar="ELEMENT")
args = parser.parse_args()

input_path = args.input if args.input else ''
replace_with = args.replace if args.replace else ''
element = args.element if args.element else 'path'
files = []
original_value = ""

if input_path != '' and replace_with != '':
    print("[+] Cargando Archivos")

    for i in os.listdir(input_path):
        if i.endswith('.xml'):
            # print(input_path+'/'+i)
            files.append(open(input_path + '/' + i))

    print("[+] Procesando %d archivos\n" % len(files))

    for file in files:
        print("[+] Parseando Archivo:")
        print(file.name)
        tree = ET.parse(file)
        root = tree.getroot()
        for elem in root.iter(element):
            original_value = elem.text.split('/')
            original_value = original_value[len(original_value) - 1]
            print("\n[+] Reemplazando contenido")
            replacement = replace_with + '/' + original_value
            elem.text = replacement
        print("[+] Sobreescribiendo archivo")
        tree.write(file.name)
        print("[+] OK\n")

    print("[+] Hecho")
    print("[+] %d archivos procesados" % len(files))
else:
    parser.print_help()