from PIL import Image


def redimensionar_imagem(imagem, resolucao, nome):
    nova_imagem = imagem.resize(resolucao)
    nova_imagem.save(nome)
    print(f"Conversão concluída com sucesso! Imagem salva como: {nome}")


# Abre a imagem original
imagem_original = Image.open("logo.png")

# Define as resoluções e nomes das novas imagens
novas_imagens = [
    {"resolucao": (36, 36), "nome": "android-icon-36x36.png"},
    {"resolucao": (48, 48), "nome": "android-icon-48x48.png"},
    {"resolucao": (72, 72), "nome": "android-icon-72x72.png"},
    {"resolucao": (96, 96), "nome": "android-icon-96x96.png"},
    {"resolucao": (144, 144), "nome": "android-icon-144x144.png"},
    {"resolucao": (192, 192), "nome": "android-icon-192x192.png"},
    {"resolucao": (192, 192), "nome": "apple-icon.png"},
    {"resolucao": (192, 192), "nome": "apple-icon-precomposed.png"},
    {"resolucao": (57, 57), "nome": "apple-icon-57x57.png"},
    {"resolucao": (60, 60), "nome": "apple-icon-60x60.png"},
    {"resolucao": (72, 72), "nome": "apple-icon-72x72.png"},
    {"resolucao": (76, 76), "nome": "apple-icon-76x76.png"},
    {"resolucao": (114, 114), "nome": "apple-icon-114x114.png"},
    {"resolucao": (120, 120), "nome": "apple-icon-120x120.png"},
    {"resolucao": (144, 144), "nome": "apple-icon-144x144.png"},
    {"resolucao": (152, 152), "nome": "apple-icon-152x152.png"},
    {"resolucao": (180, 180), "nome": "apple-icon-180x180.png"},
    {"resolucao": (16, 16), "nome": "favicon-16x16.png"},
    {"resolucao": (32, 32), "nome": "favicon-32x32.png"},
    {"resolucao": (96, 96), "nome": "favicon-96x96.png"},
    {"resolucao": (70, 70), "nome": "ms-icon-70x70.png"},
    {"resolucao": (144, 144), "nome": "ms-icon-144x144.png"},
    {"resolucao": (150, 150), "nome": "ms-icon-150x150.png"},
    {"resolucao": (310, 310), "nome": "ms-icon-310x310.png"},
]

# Gera e salva as novas imagens com as resoluções especificadas
for imagem in novas_imagens:
    redimensionar_imagem(imagem_original, imagem["resolucao"], imagem["nome"])
