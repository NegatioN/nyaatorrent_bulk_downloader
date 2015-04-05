from distutils.core import setup
from cx_Freeze import setup, Executable

setup(
    name='nyatorrent_downloader',
    version='0.2.2',
   # packages=['tests'],
    url='https://github.com/NegatioN/nyaatorrent_bulk_downloader',
    license='',
    author='NegatioN',
    description='A program to download entire series of torrents with one click from nyaa.se',
    executables = [Executable("nyaatorrent_downloader/main.py", base = "Console")]
)
