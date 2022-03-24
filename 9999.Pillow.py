"""
Estudos sobre pillow - PIL
"""

from PIL import Image


mala = Image.open("mochilaAdidasVI.jpg")
mala.show()
mala.rotate(45).show()

print(mala.format, mala.size, mala.mode)
