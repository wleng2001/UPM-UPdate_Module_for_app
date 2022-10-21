# UPM-UPdate_Module_for_app
## Description
It's module to python program, which can check and download update from github.

## Instalation

### Linux device
You can clone it in linux devices: 

#### `git clone https://github.com/wleng2001/UPM-UPdate_Module_for_app.git ./UPM`

or download as a zip file on the github webpage.

Next you can download all required program and python library automatically. You maust go to the folder with program and write the command:
#### `bash install.sh`
If you have debian you may have to update python manually. You can do it <a href="https://help.hostry.com/knowledge-base/how-do-i-upgrade-my-python-on-debian/">here</a>. If you want do install all required apps and library you can do it by installing  python, git apss and gitpython, pygithub, gitdb typing_extensions library download. You can check, that you have python by writting the information in terminal: 

#### `python3 --version` to check if you have python

You should get information similary to that:

#### `Python 3.9.7`

If you don't have download python you can do it <a href="https://www.python.org/downloads/">here</a> or you can write the text in terminal:

#### `sudo apt install python3`

Next You must install git, what you can do by typing the text in terminal:

#### `sudo apt-get install git`

If you don't have download pip you can do it by writting the text in terminal:

#### `sudo apt install python3-pip`

Next you should check, that you have required python library (gitdb, typing_extensions, pygithub and gitpython):

#### `pip list` 

You should get information similary to that:

####
```
pip list
Package            Version
------------------ ---------
certifi            2022.6.15
cffi               1.15.1
charset-normalizer 2.1.0
Deprecated         1.2.13
gitdb              4.0.9
GitPython          3.1.29
idna               3.3
pip                22.3
psutil             5.9.1
pycparser          2.21
PyGithub           1.56
PyJWT              2.5.0
PyNaCl             1.5.0
pyserial           3.5
requests           2.28.1
setuptools         57.4.0
smmap              5.0.0
typing_extensions  4.4.0
urllib3            1.26.9
vcgencmd           0.1.1
wrapt              1.14.1
```

Finally If you don't have download gitdb you can do it by writting the text in terminal (typing_extensions, pygithub and gitpython download similary): 

#### `sudo pip3 install gitdb`

### Windows device

On the windows devices you can download zip file from github and unpack it.
Next you must check, that you have python, gitdb, typing_extensions, pygithub and gitpython library download. You can check it by writting the informations in cmd (you can find cmd by typing "cmd" after press **win** key): 

#### `python --version` to check if you have python

You should get information similary to that:

#### `Python 3.9.7`

If you don't have download python you can do it <a href="https://www.python.org/downloads/">here</a>.

Next you must install git, what you can do <a href="https://gitforwindows.org/">here</a>

Rest of app you can download and install by runing *install.bat* file. If you want do it manually below you have how to do it.

if you don't have pip you can install it by writing the command in cmd:

#### `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`

after download you must typing the information in cmd:

#### `python get-pip.py`

#### `pip list` to check if you have gitdb, typing_extensions, pygithub and gitpython

You should get information similary to that:

#### 
```
pip list
Package            Version
------------------ ---------
certifi            2022.6.15
cffi               1.15.1
charset-normalizer 2.1.0
Deprecated         1.2.13
gitdb              4.0.9
GitPython          3.1.29
idna               3.3
pip                22.3
psutil             5.9.1
pycparser          2.21
PyGithub           1.56
PyJWT              2.5.0
PyNaCl             1.5.0
pyserial           3.5
requests           2.28.1
setuptools         57.4.0
smmap              5.0.0
typing_extensions  4.4.0
urllib3            1.26.9
vcgencmd           0.1.1
wrapt              1.14.1
```

Finally If you don't have gitdb, typing_extensions, pygithub and gitpython you can install it by written the text in cmd (you can find cmd by typing "cmd" after press **win** key):

#### `pip3 install gitdb` for gitdb (rest of library you can download similary)

## Usage
