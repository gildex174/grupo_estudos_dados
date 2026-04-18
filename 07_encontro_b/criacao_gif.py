import sys
from PIL import Image

imagens = []

for arg in sys.argv[1:]:
    imagem = Image.open(arg)
    imagens.append(imagem)

imagens[0].save(
    "ikiru.gif",
    save_all = True,
    append_images = [imagens[1]],
    duration=1000,
    loop=0
)