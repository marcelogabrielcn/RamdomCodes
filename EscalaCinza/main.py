import PIL
from PIL import Image
from escala_cinza import grayscale


frutas = Image.open("frutas.jpg")
frutas.show()
pb_futas = grayscale(frutas)
pb_futas.show()
pb_futas.save("pb_frutas.jpg")
