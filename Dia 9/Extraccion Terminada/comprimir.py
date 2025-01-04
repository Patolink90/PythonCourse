import zipfile
import shutil

'''mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()'''

#zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')

#zip_abierto.extractall()

carpeta_origen = 'C:\\Users\\Patolink\\PycharmProjects\\pythonProject1\\Dia 9'

archivo_destino = 'Todo_comprimido'

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)