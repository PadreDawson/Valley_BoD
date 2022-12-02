import os

os.system('.\make.bat clean')
os.system('.\make.bat html')
os.system('sphinx-build -b pdf source pdf')