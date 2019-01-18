import openpyxl
# insert image
imgFile = './web/aaa.png'
img = openpyxl.drawing.image.Image(imgFile)
sheet.add_image(img, 'B5')
# resize image
from PIL import Image
img2 = Image.open(imgFile)
new_img = img2.resize((100, 100))
new_img.save('new.png')
img3 = openpyxl.drawing.image.Image(new_img)
sheet.add_image(img3, 'A5')