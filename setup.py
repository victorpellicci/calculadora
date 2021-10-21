from sys import platform
from cx_Freeze import setup, executable

base=None
if platform == 'win32':
	base='Win32Gui'

setup(name='Calculadora do Victor', 
	version='1.0',
	description='Calculadora rapida para o dia a dia',
	options={'build_exe': {	
		'includes':['tkinter', 'ttkbootstrap', ]}},
	executables=[executable('calculadora.py', base=base)])