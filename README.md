# Scrcpy GUI

Uma interfáce de usuário simples em PyQt5 para scrcpy

## Pacotes, programas e instalação

Alguns pacotes como PyQt5, adb, scrcpy, python3 são necessários para que tudo funcione
Você pode instalá-los em seu PC usando os seguintes comandos:

#### Debian/Ubuntu
```sh
# apt-get install snapd python3-pip adb
# snap install scrcpy
$ pip3 install PyQt5
$ pip3 install pure-python-adb
```

#### Arch/Manajro
```sh
$ yay -S android-tools
$ yay -S python3 python3-pip scrcpy
$ pip3 install PyQt5
$ pip3 install pure-python-adb
```

### Instalação
Para instalar o programa, basta rodar o script "installer_uninstaller.py"

```sh
$ python3 install_uninstall.py
```

### Desinstalação
Para desinstalar, basta rodar o mesmo script de instalação


## Uso
Para executar o programa, pode utilizar o ícone que é criado no menu ou executar direto do terminal com
```
$ scrcpy_gui
```

![](assets/image_interface.png)


## Solução de problemas

Caso `scrcpy_gui` não inicie pelo terminal, verifique se `/home/usuario/.local/bin` está em $PATH, você pode verificar com `$ echo $PATH`

#### Bash padrão
Caso o path não esteja, você pode adicionar ao "~/.bashrc" a seguinte linha no final do arquivo
```sh
export PATH=$PATH:/home/{seu usuario}/.local/bin
```

#### Fish
Se você estiver utilizando o `fish`, o caso é outro
Você pode adicionar o path da seguinte forma:


No seu editor de texto preferido, adicione a seguinte linha no arquivo `~/.config/fish/config.fish`
```sh
set -U fish_user_paths /home/{seu usuário}/.local/bin $fish_user_paths
```
