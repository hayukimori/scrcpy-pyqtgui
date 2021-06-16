# coding: utf-8

#Bibliotecas: PyQt5, os (UNIX), PyGame
import os, sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def main():
    janela.show()

    # OBTER DISPOSITIVOS
    os.system("adb devices >> /tmp/adb_devices_tmp.hy")

    arquivo = open("/tmp/adb_devices_tmp.hy").readlines()
    lines = arquivo[1:]


    for line in lines:
        corte_caracteres = line.split("\t", 1)

        aparelho = corte_caracteres[0]

        mod_aparelho = aparelho.replace('\t', '')
        mod = mod_aparelho.replace('\n', '')

        print(mod)
        janela.device.addItem(mod)

    #current_text = janela.comboBox.currentText()
    #print(f"\n\n{current_text}")
    os.system("rm /tmp/adb_devices_tmp.hy")


def start():

    code = "scrcpy "

    # Pegando resultados
    device      = janela.device.currentText()
    bitrate     = janela.bitrate.currentText()
    fps         = janela.fps.text()
    fullscreen  = janela.fullscreen.isChecked()
    view_only   = janela.view_only.isChecked()
    borderless  = janela.borderless.isChecked()


    # Aicionando resultados ao launcher
    if (fullscreen == True):
        code = code + "--fullscreen "
    if (view_only == True):
        code = code + "--no-control "
    if (borderless == True):
        code = code + "--window-borderless "

    total = f"{code} --serial {device} -b {bitrate} --max-fps={fps}&"
    os.system(total)


def minimize():
    janela.showMinimized()


# Definindo app e carregando janela(s)
app = QtWidgets.QApplication([])
janela = uic.loadUi("main.ui")


# Função para deixar sem bordas e sem background (fundo)
janela.setWindowFlags(Qt.FramelessWindowHint)
janela.setAttribute(Qt.WA_TranslucentBackground);


# Botões
janela.exit.clicked.connect(sys.exit)
janela.start.clicked.connect(start)
janela.minimize.clicked.connect(minimize)

if __name__ == '__main__':
    main()

app.exec()
