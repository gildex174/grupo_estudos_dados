import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
	image = Image.open(arg)
	images.append(image)

print(len(sys.argv[1:]))

images[0].save(
	"ikiru.gif", 
	save_all=True, 
	append_images=[images[1]],
	duration=1000,
	loop=0
)