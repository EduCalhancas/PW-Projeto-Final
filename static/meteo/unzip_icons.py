import zipfile
import os

# Defina o caminho do arquivo zip e o diretório de destino
zip_path = '/home/a22204446/project/static/meteo/icons_ipma_weather.zip'
extract_to = '/home/a22204446/project/static/meteo'

# Crie o diretório de destino, se não existir
if not os.path.exists(extract_to):
    os.makedirs(extract_to)

# Extraia os arquivos
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print(f'Arquivos extraídos para {extract_to}')
