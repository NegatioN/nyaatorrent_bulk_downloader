from distutils.core import setup
from cx_Freeze import setup, Executable

setup(
    name='nyaa_bulk_downloader',
    version='0.1',
   # packages=['tests'],
    url='https://github.com/NegatioN/nyaatorrent_bulk_downloader',
    license='',
    author='NegatioN',
    description='A program to download entire series of torrents with one click from nyaa.se',
    executables = [Executable("main.py", base = "Console")]
)
