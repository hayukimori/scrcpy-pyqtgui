# -*- coding: utf-8 -*-
import os, sys, platform

USER_SYSTEM = platform.system()
VAR_HOME = os.getenv('HOME')

################## NEW -- LINUX BASED ########################
linux_default_appbase_instalation_path = VAR_HOME + '/.local/share/HayukiApps/scrcpy_pyqtgui/'
linux_default_assets_folder = linux_default_appbase_instalation_path + '/assets/'
linux_default_shell_script = VAR_HOME + '/.local/bin/scrcpy_pyqtgui'
linux_default_desktop_path = VAR_HOME + '/.local/share/applications/'
linux_default_desktop_filename = 'scrcpy_pyqtgui'
################################################################


# GLB => GLOBAL --- abbreviated global variables
glb_ldai = linux_default_appbase_instalation_path
glb_laf = linux_default_assets_folder
glb_ldsc = linux_default_shell_script
glb_ddp = linux_default_desktop_path
a_files = ['error_window.ui', 'main.ui', 'reload_btn.png', 'configure.png', 'user-home-symbolic.png']



def infoAlert(info: str, error=False):
    if error == False:
        print('[INFO] ' + info)

    elif error == True:
        print('[ERROR] ' + info)

    try:
        if type(error) != bool:
            if error.lower() == "alert":
                print(f"< {error.lower()} > " + info)

    except Exception as e:
        infoAlert(str(e), error=True)

class ManageInstaller():
    def __init__(self, operational_system_base='linux'):
        self.osb = operational_system_base;


        if self.osb.lower() == 'linux':
            self.installerMain = LinuxInstaller()

        else:
            infoAlert(info="Non Linux-based system detected; Unfortunately this program don't have a installer for this system (not yet).\n\n Try to contact me on social networks:\n\n-Twitter: https://twitter.com/hayukimori\n-Discord: hayukimori#0599\nGitHub: https://github.com/hayukimori", error="alert")

class LinuxInstaller():
    def __init__(self):
        if self.verifyExistingInstallation() != True:
            self.startInstaller()

        else:
            self.uninstall(quest=True)


    def startInstaller(self):

        if self.verifyLocalFiles() == False:
            infoAlert(f"Some files couldn't be found, please verify files and try again;\nRequired files: {a_files}", error=True)

        else:
            try:

                # => Informing about package
                package_info = f"\n=============================================\nApp: Scrcpy PtQtGui\nApp: scrcpy_pyqtgui,\nFont: github\nCreator: hayukimori\n\nInstallation Path: {linux_default_appbase_instalation_path}\nStatus: installing\n=============================================\n"
                infoAlert(package_info, error=False)



                # =>  Creating Directories (HayukiApps, assets)
                infoAlert(f"Creating directiories:\n {linux_default_appbase_instalation_path}\n{linux_default_assets_folder}", error=False)
                os.system('mkdir -p ' + linux_default_appbase_instalation_path)
                os.system('mkdir -p ' + linux_default_assets_folder)


                # => Moving files to paths
                infoAlert("Moving files (assets)", error=False)
                for file in a_files:
                    print(file)
                    os.system(f"cp assets/{file} " + linux_default_assets_folder)
                    

                infoAlert("Moving main files", error=False)
                for file in ['main.py', 'install_uninstall.py']:
                    os.system(f'cp {file} ' + linux_default_appbase_instalation_path)



                # => Making Shell Script

                    # Checks if ".local/bin/" is in $PATH
                if self.localbin_in_SystemPath() == False:
                    infoAlert(f"'{VAR_HOME}/.local/bin' isn't in PATH. To start this application using terminal, you'll need to add in $PATH. See README.md to see how to make it", error=False)
                    infoAlert("Creating shell script", error=False)


                self.makeShellScript()


                # => Creating desktop file
                infoAlert("Creating desktop file", error=False)
                dfileText = f'''[Desktop Entry]\nVersion=1.0\nType=Application\nName=Scrcpy Gui\nComment=Scrcpy PyQt5 gui\nIcon=smartphone\nExec=python main.py\nPath={linux_default_appbase_instalation_path}\nTerminal=false\nStartupNotify=true\nCategories=AudioVideo;nUtility;'''

    
                with open(linux_default_desktop_path + linux_default_desktop_filename + '.desktop', 'w') as df:
                    df.write(dfileText)
                    df.close()
                




            except Exception as e:
                infoAlert(str(e) + '\n', error=True)

    def verifyLocalFiles(self):

        results = []

        for a in a_files:
            if os.path.exists("./assets/" + a) == True:
                results.append(True)


        if all_true(results):
            return True
        else:
            return False


    def verifyExistingInstallation(self):
        # for newer version Only
        if os.path.exists(linux_default_appbase_instalation_path) == True:
            return True

        else:
            return False

    def uninstall(self, quest=True):
        print("=====================SCRCPY PYQT GUI FOUND IN SYSTEM ==========================")
        print(f"Installation found in {VAR_HOME}/.local/share/HayukiApps/")
        uinput = input("Uninstall current version or Update (UPdate / UNinstall)\n((default: Update)): ")
        print("===============================================================================")

        uinput_no_spaces = uinput.replace(" ", '')

        if uinput_no_spaces.lower().startswith('un'):
            os.system(f'rm -rf ' + linux_default_appbase_instalation_path)
            os.system(f'rm -rf ' + linux_default_desktop_path + linux_default_desktop_filename)
            

        else:
            os.system(f'rm -rf ' + linux_default_appbase_instalation_path)
            self.startInstaller()


    def makeShellScript(self):
        script_text = f'''#!/bin/bash\ncd {linux_default_appbase_instalation_path}/\npython main.py'''

        
        with open(linux_default_shell_script, 'w') as ss:
            ss.write(script_text)
            ss.close()
            os.system(f"chmod +x {linux_default_shell_script}")


    def localbin_in_SystemPath(self):
        path_linux_var = os.getenv('PATH')

        if '/.local/bin' in path_linux_var:
            return True
        else:
            return False


def all_true(items):
    return all(x == True for x in items)


if __name__ == "__main__":
    Installer = ManageInstaller(operational_system_base=USER_SYSTEM)
