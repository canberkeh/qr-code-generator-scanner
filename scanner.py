'''
This module is made for scanning qr codes. Results are on camera screen, at terminal and will be written on barcode_results.txt
Don't forget to ctrl+c to kill this module!
'''
import cv2
from pyzbar import pyzbar
from log import logger
logging = logger()

class QrScanner:
    def read_barcodes(frame):
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            x, y , w, h = barcode.rect
            barcode_info = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
            print(barcode_info)
            with open("barcode_result.txt", mode ='w') as file:
                file.write("Recognized Barcode:" + barcode_info)
        return frame

    def main():
        try:
            camera = cv2.VideoCapture(0)
            logging.info("Camera started!")
            ret, frame = camera.read()
            while ret:
                ret, frame = camera.read()
                frame = QrScanner.read_barcodes(frame)
                cv2.imshow('Barcode/QR code reader', frame)
                if cv2.waitKey(1) & 0xFF == 27:
                    break
            camera.release()
            cv2.destroyAllWindows()
        except:
            logging.error("Camera problem!")
