# ESB Corrections
Corrects ESB auto generated files. Only for Windows OS.

# Requirements
- pyhton (3.4 or above) [Download](https://www.python.org/downloads/)

# How to use
Place generated archivioPJ in ESB_Corrections dir. 
Open config.py and put IN RIGHT ORDER the operation list.
```sh
> python correct.py
```

This will generate new files near the old ones that should be replaced. The program will ask you if you want to replace them. If you don't choose to replace, you can remove just generated files with:
```sh
> python DeleteAllNewFiles.py
```

There will be created backup folder with backuped files.
