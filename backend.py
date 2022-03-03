#todo achterkant pdfmaker
#todo voor schijven van pdf
from PIL import Image
from tkinter import filedialog
global IMAGELIST
IMAGELIST = []

def filezipper(file,totalnumber):
    for image in range(0,totalnumber):
        image = Image.open(file)
        im = image.convert("RGB")
        IMAGELIST.append(im)
        im.save("test.pdf", save_all=True, append_images=IMAGELIST)

#image1 = Image.open("1.jpg")
#im = image1.convert("RGB")
#imagelist = [im]
#def pdfmaker(IMAGELIST):
#    im.save("test.pdf", save_all=True, append_images=IMAGELIST)


def browsefile():
    filename = filedialog.askopenfilename(initialdir="/", title="select a files", filetypes= (("jpg files", "*.jpg"), ("all file", "*.*")))