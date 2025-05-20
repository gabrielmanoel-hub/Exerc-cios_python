import os 
# Permite que interaja com o sistema operacional

import glob
# Usado para encontrar todos os arquivos que corresponde a um padrâo

Pasta = glob.glob(os.path.join('imagens','*.jpg'))
# Cria uma lista com todos os arquivos .jpg dentro da pasta 'imagens'


Pasta.sort()
# Ordena os arquivos encontrados

for i, caminho_antigo in enumerate(Pasta, start=1):
    novo_nome = f'foto_{i:03d}.jpg'
    # Formata o nome do arquivo com 3 digitos
    # Exemplo: 001.jpg, 002.jpg, etc.
    caminho_novo = os.path.join('imagens', novo_nome)
    # Cria o ovo caminho do novo arquivo
    # Exemplo: imagens/foto_001.jpg

    os.rename(caminho_antigo, caminho_novo)
    # Renomeia arquivo
    print(f'Renomeado: {caminho_antigo} -> {caminho_novo}')