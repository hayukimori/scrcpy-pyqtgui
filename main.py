# -*- coding: utf-8 -*-

#Libs: PyQt5, os, PyGame, sys, re, subprocess
import os, sys, subprocess, re
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# ==> Show error
def err_h(details):
    error_window.show()

    if details == "no devices":
        error_window.text.setText("No devices connected")
    else:
        error_window.text.setText(details)








# ==> Get Devices & send to QComboBox

def get_devices():

    try:
        cmd = "adb devices"
        cmd_out = subprocess.check_output(cmd, shell=True).decode("UTF-8")

        lines = cmd_out.split("\n")
        devices = lines[1:]

        for device in devices:
            device = re.sub(r"\tdevice", "", device)

            if len(device) > 1:
                window.device.addItem(device)
            else:
                pass
        


        # If no devices connected, send error to err_h (Line 13)

        if len(window.device) == 0:
            print("No devices connected")
            err_h("no devices")
        

    # if something goes wrong, send the error to "err_h()" (Line 13)
    except Exception as e:
        exceptionString = str(e)
        err_h(exceptionString)




# ==> Show Window & call get_devices function
def main():
    window.show()

    while len(window.device) > 0:
        window.device.removeItem(0)

    get_devices()    
    





# ==> This is the real main function, When "Start" button is pressed, this function will get all window values & send to scrcpy
def start():
    device      = window.device.currentText()
    resolution	= window.resolution.text()
    bitrate     = window.bitrate.currentText()
    fps         = window.fps.text()
    fullscreen  = window.fullscreen.isChecked()
    view_only   = window.view_only.isChecked()
    borderless  = window.borderless.isChecked()


    code = 'scrcpy '


    if (fullscreen == True):
        code = code + "--fullscreen "
    if (view_only == True):
        code = code + "--no-control "
    if (borderless == True):
        code = code + "--window-borderless "


    
    final_code = f"{code} --serial {device} -m {resolution} -b {bitrate} --max-fps={fps}&"
    os.system(final_code)




app = QtWidgets.QApplication([])


# Load Windows
window = uic.loadUi("assets/main.ui")
error_window = uic.loadUi("assets/error_window.ui")


# Setting functions to window(s) buttons
window.start.clicked.connect(start)
window.reload_btn.clicked.connect(main)
error_window.ok_btn.clicked.connect(error_window.close)




# ==> call the primary function
if __name__ == '__main__':
    main()
    

app.exec()