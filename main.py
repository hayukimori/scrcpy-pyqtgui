import os, sys, re, subprocess;
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ppadb.client import Client as AdbClient

linux_nobrake = "&"       # This works for PowerShell too
nobrake = linux_nobrake

adb = AdbClient(host="127.0.0.1", port=5037)
app = QtWidgets.QApplication([])


class MainProgram:

	def get_devices(win_devices):
		try:
			devices = adb.devices()

			if len(devices) == 0:
				ErrorShower("No devices connected")

			for device in devices:
				win_devices.addItem(device.serial)

		except Exception as e:
			ErrorShower(error=str(e))


	def normalStart(self):

		try:

			space = " "

			device 		= window.normal_devices.currentText()
			bitrate 	= window.normal_bitrate.text()
			fullscreen 	= window.normal_fullscreen.isChecked()
			view_only 	= window.normal_view_only.isChecked()
			borderless 	= window.normal_borderless.isChecked()
			render		= window.normal_render.currentText()

			code = 'scrcpy' + space

			if fullscreen == True:
				code = code + '--fullscreen' + space

			if view_only == True:
				code = code + '--no-control' + space

			if borderless == True:
				code = code + '--window borderless' + space


			final_code = f'''{code} --serial {device} -b {bitrate} --render-driver="{render}"''' + nobrake
			os.system(final_code)

		except Exception as e:
			ErrorShower(str(e))


	def otgStart(self):
		try:

			space = " "

			device 		= window.otg_devices.currentText()
			bitrate 	= window.otg_bitrate.text()
			fullscreen 	= window.otg_fullscreen.isChecked()
			borderless 	= window.otg_borderless.isChecked()
			render		= window.otg_render.currentText()

			code = 'scrcpy' + space

			if fullscreen == True:
				code = code + '--fullscreen' + space

			if borderless == True:
				code = code + '--window borderless' + space


			final_code = f'''{code} --serial {device} -b {bitrate} --render-driver="{render} -K -M"''' + nobrake
			os.system(final_code)

		except Exception as e:
			ErrorShower(str(e))


	def gameStart(self):
		try:

			space = " "

			device 		= window.game_devices.currentText()
			bitrate 	= window.game_bitrate.text()
			fullscreen 	= window.game_fullscreen.isChecked()
			borderless 	= window.game_borderless.isChecked()
			no_otg		= window.game_no_otg.isChecked()
			render		= window.game_render.currentText()


			code = 'scrcpy' + space

			if fullscreen == True:
				code = code + '--fullscreen' + space


			if borderless == True:
				code = code + '--window borderless' + space


			if no_otg != True:
				code = code + '-K -M'


			final_code = f'''{code} --serial {device} -b {bitrate} --render-driver="{render}"''' + nobrake
			os.system(final_code)

		except Exception as e:
			ErrorShower(str(e))


	def manualStart(self):
		try:

			space = " "

			device 		= window.manual_devices.currentText()
			bitrate 	= window.manual_bitrate.text()
			fullscreen 	= window.manual_fullscreen.isChecked()
			view_only 	= window.manual_view_only.isChecked()
			borderless 	= window.manual_borderless.isChecked()
			render		= window.manual_render.currentText()
			add_args	= window.manual_args.toPlainText()

			code = 'scrcpy' + space

			if fullscreen == True:
				code = code + '--fullscreen' + space

			if view_only == True:
				code = code + '--no-control' + space

			if borderless == True:
				code = code + '--window borderless' + space

			if len(add_args) >= 1:
				code = code + add_args + space


			final_code = f'''{code} --serial {device} -b {bitrate} --render-driver="{render}"''' + nobrake
			os.system(final_code)

		except Exception as e:
			ErrorShower(str(e))




class WindowManager():

	def defineFlags():
		window.setWindowFlags(Qt.FramelessWindowHint)
		window.setAttribute(Qt.WA_TranslucentBackground)

	def showMain():
		window.show()


	def _home_page():
		window.stackedWidget.setCurrentIndex(0)

	def _normal_page():
		window.stackedWidget.setCurrentIndex(1)

		WindowManager.reZero(window.normal_devices)
		MainProgram.get_devices(window.normal_devices)

	def _otg_page():
		window.stackedWidget.setCurrentIndex(2)

		WindowManager.reZero(window.otg_devices)
		MainProgram.get_devices(window.otg_devices)

	def _game_page():
		window.stackedWidget.setCurrentIndex(3)

		WindowManager.reZero(window.game_devices)
		MainProgram.get_devices(window.game_devices)

	def _manual_page():
		window.stackedWidget.setCurrentIndex(4)

		WindowManager.reZero(window.manual_devices)
		MainProgram.get_devices(window.manual_devices)


	def _confs_page():
		window.stackedWidget.setCurrentIndex(5)




	def _reload_normal_d():
		WindowManager.reZero(window.normal_devices)
		MainProgram.get_devices(window.normal_devices)


	def _reload_otg_d():
		WindowManager.reZero(window.otg_devices)
		MainProgram.get_devices(window.otg_devices)

	def _reload_game_d():
		WindowManager.reZero(window.game_devices)
		MainProgram.get_devices(window.game_devices)


	def _reload_manual_d():
		WindowManager.reZero(window.manual_devices)
		MainProgram.get_devices(window.manual_devices)




	def reZero(win_devices):
		while len(win_devices) > 0:
			win_devices.removeItem(0)




class ErrorShower():
	def __init__(self, error, windowed=True):
		self.error = error
		self.windowed = windowed

		if windowed == True:
			errorWindow.text.setText(str(error))
			errorWindow.show()
		else:
			print(f"<ERROR> {str(error)}")



window = uic.loadUi("assets/main.ui")
errorWindow = uic.loadUi("assets/error_window.ui")
window.exit_button.clicked.connect(sys.exit)


# Button Functions
window.home_btn.clicked.connect(WindowManager._home_page)
window.normal_btn.clicked.connect(WindowManager._normal_page)
window.otg_btn.clicked.connect(WindowManager._otg_page)
window.game_btn.clicked.connect(WindowManager._game_page)
window.manual_btn.clicked.connect(WindowManager._manual_page)
window.configure_btn.clicked.connect(WindowManager._confs_page)

window.minimize_btn.clicked.connect(window.showMinimized)
errorWindow.ok_btn.clicked.connect(errorWindow.close)

# Reload Buttons
window.normal_reload_btn.clicked.connect(WindowManager._reload_normal_d)
window.otg_reload_btn.clicked.connect(WindowManager._reload_otg_d)
window.game_reload_btn.clicked.connect(WindowManager._reload_game_d)
window.manual_reload_btn.clicked.connect(WindowManager._reload_manual_d)


# Start Buttons
window.normal_start.clicked.connect(MainProgram.normalStart)
window.otg_start.clicked.connect(MainProgram.otgStart)
window.game_start.clicked.connect(MainProgram.gameStart)
window.manual_start.clicked.connect(MainProgram.manualStart)




if __name__ == "__main__":
	WindowManager.defineFlags()
	WindowManager.showMain()
	app.exec()