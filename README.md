# Scrcpy PyQt GUI
> A simple interface to scrcpy made with Qt5

![Python Ver](https://img.shields.io/badge/Python-3.10-blue?style=flat-square)
![PyQt5 Ver](https://img.shields.io/badge/PyQt5-5.15.6-blue?style=flat-square)
![PPADB Ver](https://img.shields.io/badge/ppadb-0.3.0.dev0-blue?style=flat-square)



Scrcpy PyQtGUI is a Qt5 frontend to ease the use of scrcpy (currently run via command line).

By not having access to the output of Scrcpy, there is the possibility of errors that do not appear on the screen or total crash in the interface (in case of running via Windows cmd)

**Versão PT-BR: [README_PT-BR.md](README_PT-BR.md)**
![Demo](demo.png)

## Preparation and installation
Some packages are necessary for the program to work, and they can be installed with the following commands:


#### Ubuntu/Debian

```sh
$ sudo apt-get install snapd python3-pip adb
$ sudo snap install scrcpy
$ pip3 install PyQt5 pure-python-adb
```


#### Arch/Manjaro
(NOTE: Both PARU and YAY can be used in this process, if you have either installed. In this case, I will be using YAY as an example)

```sh
$ yay -S python3 python3-pip scrcpy
$ sudo pacman -S android-tools
$ pip3 install PyQt5 pure-python-adb
```


### Installation
To install on linux distros, just run the `install_uninstall.py` script.
I warn you that the installation of this version will take place in a different directory. It will be in `/home/{your_username}/.local/share/HayukiApps/`

Also notice here that the commands _must_ be executed inside the folder;

```sh
$ python install_uninstall.py
```

#### Windows
Unfortunately the installer is not ready for Windows yet, I will be developing it soon. But I think the program works fine if it has all dependencies and if `adb.exe` and `scrcpy.exe` are in the Windows PATH

## Common problems

If `scrcpy_gui` doesn't start from terminal, check if `/home/user/.local/bin` is in $PATH, you can check with `$ echo $PATH`

#### Default Bash
If the path is not there, you can add to "~/.bashrc" the following line at the end of the file

```sh
export PATH=$PATH:/home/{your username}/.local/bin
```

#### Fish
If you are using `fish`, it's a different case.
You can add the path as follows:

In your favorite text editor, add the following line to the `~/.config/fish/config.fish` file

```sh
set -U fish_user_paths /home/{your user}/.local/bin $fish_user_paths
```

##### Other problems

If the problem is not the one above, you can [open an issue](https://github.com/hayukimori/scrcpy-pyqtgui/issues/new). (PT BR or English)

## About

Code and layout by _Ana Beatriz_ ([@hayukimori](https://twitter.com/hayukimori/))
