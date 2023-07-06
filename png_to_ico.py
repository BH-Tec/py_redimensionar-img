from PIL import Image


def convert_png_to_ico(png_path, ico_path, size=(32, 32)):
    # Abre a imagem PNG
    png_image = Image.open(png_path)

    # Redimensiona a imagem, se necessário
    if png_image.size != size:
        png_image = png_image.resize(size, Image.ANTIALIAS)

    # Cria uma nova imagem vazia do tipo RGBA
    ico_image = Image.new("RGBA", png_image.size, (0, 0, 0, 0))

    # Copia a imagem PNG para a imagem ICO
    ico_image.paste(png_image, (0, 0), mask=png_image)

    # Salva a imagem ICO
    ico_image.save(ico_path, format="ICO")

    print(f"Conversão concluída com sucesso! Imagem salva como: favicon.ico")


# Exemplo de uso
convert_png_to_ico("logo.png", "favicon.ico")
