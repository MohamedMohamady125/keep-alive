#!/bin/bash
# Builds "Keep Alive.app" on a Mac. Needs Python 3 installed (python.org).
set -e
cd "$(dirname "$0")"
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m PyInstaller --noconfirm --windowed --name "Keep Alive" \
  --osx-bundle-identifier com.keepalive.app keep_alive.py
cd dist && ditto -c -k --keepParent "Keep Alive.app" KeepAlive-mac.zip
echo
echo "Done! Your app is at: dist/Keep Alive.app  (zipped: dist/KeepAlive-mac.zip)"
