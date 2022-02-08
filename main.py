# -*- coding: utf-8 -*- 

#Libs: PyQt5, os, sys, re, subprocess, pure-python-adb
import os, sys, re, subprocess;
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ppadb.client import Client as AdbClient


adb = AdbClient(host="127.0.0.1", port=5037)
app = QtWidgets.QApplication([])


class MainProgram:
    def startWindow():
        window.show()


    def reZeroCount():
        while len(window.device) > 0:
            window.device.removeItem(0)


    def get_devices():
        try:
            devices = adb.devices()

            if len(devices) == 0:
                ErrH.noDevices()

            for device in devices:
                window.device.addItem(device.serial)

        except Exception as e:
            ErrH(error_str=str(e))


    def startScrcpy():
        device      = window.device.currentText()
        resolution  = window.resolution.text()
        bitrate     = window.bitrate.currentText()
        fps         = window.fps.text()
        fullscreen  = window.fullscreen.isChecked()
        view_only   = window.view_only.isChecked()
        borderless  = window.borderless.isChecked()
        render      = window.render.currentText()
        add_args    = window.add_args.text()

        code = 'scrcpy '

        if (fullscreen == True):
            code = code + "--fullscreen "
        if (view_only == True):
            code = code + "--no-control "
        if (borderless == True):
            code = code + "--window-borderless "

        try:
            final_code = f'''{code} --serial {device} -m {resolution} -b {bitrate} --max-fps={fps} --render-driver="{render}" {add_args} &'''
            os.system(final_code)

        except Exception as e:
            ErrH(error_str=str(e))
            #raise e


class ErrH:
    def __init__(self, error_str=None):
        self.error_str = error_str

        if self.error_str != None:
            self.showError(error_str)

    def noDevices():
        error_window.show()
        error_window.text.setText("No devices connected")


    def showError(self, error_str):
        error_window.show()
        error_window.text.setText(self.error_str)


class WindowManager:
    def advanced_mode_on():
        window.normal_advanced.setCurrentIndex(1)

    def advanced_mode_off():
        window.normal_advanced.setCurrentIndex(0)

def reloadDevices():
    MainProgram.reZeroCount()
    MainProgram.get_devices()

def main():
    MainProgram.startWindow()
    MainProgram.reZeroCount()
    MainProgram.get_devices()


# Load Windows
window = uic.loadUi("assets/main.ui")
error_window = uic.loadUi("assets/error_window.ui")


# Setting functions to window(s) buttons
window.start.clicked.connect(MainProgram.startScrcpy)
window.reload_btn.clicked.connect(reloadDevices)
window.advanced_mode.clicked.connect(WindowManager.advanced_mode_on)
window.normal_mode.clicked.connect(WindowManager.advanced_mode_off)
error_window.ok_btn.clicked.connect(error_window.close)

if __name__ == "__main__":
    main()



app.exec()
