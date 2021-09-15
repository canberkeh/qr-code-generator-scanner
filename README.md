# Qr generator & scanner
## General Info
This application works as a qr generator and scanner. After running on terminal, Generate operation creates a qr code and opens, Scanner runs computers camera and when detects a qr code
shown on camera, will display information and save it to a file. 

## How it works
Follow instructions given under setup section. After executing run.py, app will ask operation on terminal.
1- QrGenerator --> Generates qr code
2- QrScanner --> Scans qr code  # Camera wont stop while trying to close it. CTRL + C will kill program + camera.
quit() --> exit
Logging may be followed in log doc after running app.

## Setup

 1. Create and activate env

    >     virtualenv venv
    >     .\venv\Scripts\activate

 2. Install pip packages

	> 	 `pip install -r requirements.txt`

 3. Run run.py

##
![yourqrcode](https://user-images.githubusercontent.com/73230039/133126076-5c63756a-588e-41c2-9bed-a43b26db60ef.png)