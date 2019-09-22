
from PIL import Image

Folder = ["CQT"]

def cut(i, Folder):
    img = Image.open(".//SourceData//" + str(Folder) + "//" +str(i) + ".jpg")

    x = 750 + 1550
    y = 480
    x_length = 1034  #7.5sec
    y_length = 3080

    for j in range (0, 3):
        x1 = (x + (x_length * j))
        x2 = x1 + x_length
        y1 = y
        y2 = y + y_length

        region = img.crop((x1, y1, x2, y2))
        region.save(".//10secCQT//" + str(i) + "_" + str((j + 1)) + ".jpg")


for Fold in Folder:
    for i in range(1, 1001):
        cut(i, Fold)