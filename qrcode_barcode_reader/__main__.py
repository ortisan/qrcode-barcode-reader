import uuid

import cv2
import numpy as np
from PIL import Image
from pyzbar import pyzbar


def extract_data(image_ndarray):
    barcodes = pyzbar.decode(image_ndarray)

    for barcode in barcodes:
        type = barcode.type
        info = barcode.data.decode("utf-8")
        print(f"Found {type} with info {info}")

        x, y, w, h = barcode.rect
        bounded_img = image_ndarray[y : y + h, x : x + w]
        cv2.imwrite(f"result/{str(uuid.uuid4())}.png", bounded_img)

    return image_ndarray


def main():
    img = Image.open("examples/image1.png")
    image_ndarray = np.asarray(img)
    extract_data(image_ndarray)


if __name__ == "__main__":
    main()
