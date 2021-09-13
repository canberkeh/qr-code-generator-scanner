'''
Run this module to start program
'''

def terminator():
    '''
    Terminal controller for choice inputs. 1-Generator, 2-Scanner, quit() for exit.
    '''
    controller = True
    while controller:
        try:
            choice = input("1 - QrGenerator Qr Code\n2 - QrScanner(Remember ctrl+c to exit!)\nquit()\n")
            if choice == "1":
                from generator import QrGenerator
                controller = QrGenerator.generate_qr_code()
            elif choice == "2":
                from scanner import QrScanner
                QrScanner.main()
            elif choice == "quit()":
                controller=False
                print("Take care!")
        except:
            print("Only numbers!\n")


if __name__ == '__main__':
    terminator()
