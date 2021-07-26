# -*- coding: utf-8 -*-
import os, sys, platform


HOME                  = os.getenv('HOME')
P_NAME                = platform.system()
INSTALL_PATH_LINUX    = HOME + '/.local/share/hayukiApps/scrcpy_gui/'
ASSETS_FOLDER_LINUX   = INSTALL_PATH_LINUX + "assets/"
DESKTOP_PATH_LINUX    = HOME + '/.local/share/applications/'
SHELL_SCRIPT          = HOME + '/.local/bin/scrcpy_gui'
DESKTOP_FILENAME      = 'scrcpy_gui'


a_files = ['error_window.ui', 'main.ui', 'reload_btn.png', 'sp_icon.png', 'spsize_icon.png']


def installation_exists_linux():
    if os.path.exists(INSTALL_PATH_LINUX) == True:
        return True
    else:
        return False


def install_linux():

    # => Make install folder
    print(f"[INFO] Installing in {INSTALL_PATH_LINUX}")
    os.system(f"mkdir -p {INSTALL_PATH_LINUX}")
    os.system(f"mkdir -p {ASSETS_FOLDER_LINUX}")

    # => Move assets files to path
    print("[INFO] Moving files")

    for f in a_files:
        os.system(f"cp assets/{f} {ASSETS_FOLDER_LINUX}")
    os.system(f"cp main.py install_uninstall.py {INSTALL_PATH_LINUX}")

    # => Create Desktop File
    print("[INFO] attaching to menu")
    dfileText = f'''[Desktop Entry]\nVersion=1.0\nType=Application\nName=Scrcpy Gui\nComment=Scrcpy PyQt5 gui\nIcon=smartphone\nExec=python3 main.py\nPath={INSTALL_PATH_LINUX}\nTerminal=false\nStartupNotify=true\nCategories=AudioVideo;nUtility;'''

    with open(DESKTOP_PATH_LINUX + DESKTOP_FILENAME + '.desktop', 'w') as df:
        df.write(dfileText)
        df.close()

    # => Verify instalation
    folder_v = os.path.exists(INSTALL_PATH_LINUX)
    if folder_v == True:
        print("OK")
    else:
        print("Not OK")


    # Make Shell
    script_text = f'''#!/bin/bash\ncd {INSTALL_PATH_LINUX}/\npython3 main.py'''

    with open(SHELL_SCRIPT, 'w') as ss:
        ss.write(script_text)
        ss.close
        os.system(f"chmod +x {SHELL_SCRIPT}")


def uninstall_linux():
    # Remove installation folder
    os.system(f"rm -rf {INSTALL_PATH_LINUX}")

    # Remove desktop file
    os.system(f"rm {DESKTOP_PATH_LINUX}{DESKTOP_FILENAME}.desktop")

    # Remove shell script
    os.system(f"rm {SHELL_SCRIPT}")



def main():

    # Install or uninstall from Linux

    if P_NAME.lower() == "linux":
        try:
            # Check if is installed
            if installation_exists_linux() == True:
                q = input(f"Already installed in {INSTALL_PATH_LINUX}, uninstall? (Y/n) ")
                if q.lower() == 'n':
                    sys.exit()

                else:
                    uninstall_linux()

            else:
                install_linux()

        except Exception as e:
            exceptionString = str(e)
            raise e # Temporário, apenas para debug

    else:
        print("Operating system not supported yet")

main()
