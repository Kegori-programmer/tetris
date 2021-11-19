@echo off
python --version 2>nul
IF errorlevel 1 (
   set /p DUMMY=please install python https://www.python.org/ftp/python/3.9.9/python-3.9.9-amd64.exe
) ELSE (
    pip install pygame
    python ./tetris.py
)
