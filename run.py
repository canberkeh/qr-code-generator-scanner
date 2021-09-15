'''
Run this module to start program
'''
from log import logger


def terminator():
    '''
    Terminal controller for choice inputs. 1-Generator, 2-Scanner, quit() for exit.
    '''
    controller = True
    while controller:
        try:
            choice = input("1 - QrGenerator\n2 - QrScanner(Remember ctrl+c to exit!)\nquit()\n")
            if choice == "1":
                from generator import QrGenerator
                logging.info(f'{QrGenerator.generate_qr_code} method has been terminated.')
                controller = QrGenerator.generate_qr_code()
            elif choice == "2":
                from scanner import QrScanner
                logging.info(f'{QrScanner.__name__} method has been terminated.')
                QrScanner.main()
            elif choice == "quit()":
                logging.info(f'Killing program.')
                controller=False
                print("Take care!")
        except:
            if choice != "quit()" and isinstance(choice, str):
                print("Only numbers!\n")
                logging.warning(f'Wrong input type {choice} type ==> {type(choice)}')
            elif choice is None:
                print("Input needed!\n")
                logging.warning(f'Nonetype input, type ==> {type(choice)}')


if __name__ == '__main__':
    logging = logger()
    terminator()
