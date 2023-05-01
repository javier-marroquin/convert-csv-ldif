import csv
from ldif import LDIFWriter

# Abre el archivo CSV para lectura y el archivo LDIF para escritura
with open('contactos.csv', newline='', encoding='utf-8') as csv_file, \
        open('contactos.ldif', mode='wb') as ldif_file:
    # Crea un objeto LDIFWriter para escribir los datos en el archivo LDIF
    ldif_writer = LDIFWriter(ldif_file)

    # Lee los datos del archivo CSV y convierte cada fila a un registro LDIF
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        dn = 'cn={},ou=People,dc=example,dc=com'.format(row[1])
        attrs = {
            'objectClass': ['top', 'person', 'organizationalPerson', 'inetOrgPerson'],
            'cn': [str(row[0])],
            'givenName': [str(row[0])],
            'sn': [str(row[2])],
            'mail': [str(row[8])],
            'telephoneNumber': [str(row[15])],
        }
        # Convierte dn a una cadena de caracteres y escribe el registro en el archivo LDIF
        ldif_writer.unparse(dn, attrs)
        ldif_file.write(b'\n')

print('Conversión de CSV a LDIF finalizada')


