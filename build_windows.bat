@echo off
REM Builds KeepAlive.exe on Windows. Needs Python 3 installed (python.org).
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m PyInstaller --noconfirm --onefile --windowed --name "KeepAlive" keep_alive.py
echo.
echo Done! Your app is at: dist\KeepAlive.exe
pause
