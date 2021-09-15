'''
This module is made for generating QR barcodes on given qr data/link. 
You must specify your data/link to qr.add_data("here!").
Generated Qr will be opened and you will see a feedback on terminal.
'''
import qrcode
from PIL import Image
from log import logger
import os

logging = logger()
class QrGenerator():

    def generate_qr_code():
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        try:
            qr.add_data("SPECIFY YOUR DATA/LINK HERE")
            qr.make(fit=True)
            img = qr.make_image(fill_color="red", back_color="black")
            img.save("yourqrcode.png")
        except:
            print("Cannot prepare qr code! Check you data.")
            logging.error('given data is not valid.')
        opening_image = Image.open("yourqrcode.png")
        opening_image.show()
        print(opening_image.filename)
        logging.info(f'Qr Code has been generated. Name : {opening_image.filename}')
        print("Your qr code has been generated. Shutting down.")
        controller = False
        return controller
