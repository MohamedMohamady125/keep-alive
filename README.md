# Keep Alive

**New here? Open START_HERE.md for the full setup guide.**

A tiny app that keeps your computer "active" by nudging the mouse a few pixels
every 20 seconds, scrolling down and back up every few nudges, and optionally
tapping Shift. Useful for apps that pause or log you out when you haven't
touched the keyboard or trackpad.

Tip: scrolling happens in whatever window is under the mouse, so park the
cursor over something harmless (like the desktop or a blank page).

## For people using the app

**Windows:** double-click `KeepAlive.exe`. If a blue "Windows protected your PC"
box appears, click **More info → Run anyway** (it shows because the app isn't
code-signed).

**Mac:** unzip `KeepAlive-mac.zip` and drag **Keep Alive** into Applications.
- First launch: right-click the app → **Open** → **Open** (needed because it
  isn't notarized by Apple).
- Allow it to control the mouse: **System Settings → Privacy & Security →
  Accessibility**, turn on **Keep Alive**, then quit and reopen the app.

Then set how often to nudge, click **Start**, and leave the window open
(minimizing it is fine). Click **Stop** or close the window to end it.

## For you (building the apps)

A computer can only build the app for its own system, so:

- **Windows .exe:** on a Windows PC with Python installed, double-click
  `build_windows.bat`. Result: `dist\KeepAlive.exe`.
- **Mac .app:** on a Mac with Python installed, run `bash build_mac.sh`.
  Result: `dist/KeepAlive-mac.zip`.
- **Both at once, no extra computer needed:** put this folder on GitHub, go to
  the **Actions** tab, run **Build apps**, and download the two files from the
  finished run. Pushing a tag such as `v1.0` also attaches them to a GitHub
  Release page you can share as a download link.
