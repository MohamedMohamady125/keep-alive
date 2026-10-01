# CLAUDE.md — Keep Alive

Context for Claude Code working in this repo. Read this first.

## What the product is
Keep Alive is a small desktop app for regular, non-technical people. It keeps
a computer "active" so apps that check for user input don't pause, go idle,
or log the user out. While running it:
- moves the mouse a few pixels and back every **20 seconds** (default),
- every **3rd nudge** scrolls down a little and back up the same amount,
- can optionally tap **Shift**,
- can stop itself after N minutes.

The owner wants this to become a real product people download from a website.
Target users do not know programming. Every screen, message and install step
must make sense to them.

## Repo layout
- `keep_alive.py` — the whole app (Python 3 + Tkinter UI + pyautogui for input).
- `requirements.txt` — Python dependencies.
- `build_mac.sh` / `build_windows.bat` — local PyInstaller builds.
- `.github/workflows/build.yml` — builds the Mac `.app` (zipped) and Windows
  `.exe` on GitHub; pushing a tag like `v1.0.0` attaches them to a Release.
- `.github/workflows/pages.yml` — publishes `website/` to GitHub Pages.
- `website/index.html` — the download/landing page (single self-contained
  file). Download buttons read `REPO` near the bottom and link to
  `releases/latest/download/KeepAlive-mac.zip` and `KeepAlive.exe`.

## Rules
- Keep behavior defaults as above unless the owner asks to change them.
- The cursor must always end where it started; scrolling must return to the
  original position.
- Never add telemetry, network calls, or data collection.
- Keep artifact names stable: `KeepAlive-mac.zip` and `KeepAlive.exe` (the
  website links depend on them).
- Plain-language UI text. No jargon in anything a user sees.
- After changing `keep_alive.py`, run it locally to check it still starts.

## Commands
- Run from source: `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && python keep_alive.py`
- Build Mac app: `bash build_mac.sh` → `dist/KeepAlive-mac.zip`
- Build Windows app (on Windows): `build_windows.bat` → `dist\KeepAlive.exe`
- Release: `git tag v1.0.0 && git push origin v1.0.0`

## Roadmap to a polished product (do in this order)
1. **App icon** — design a simple icon; add `icon.icns` (Mac) and `icon.ico`
   (Windows) and pass `--icon` in both build scripts and the workflow.
2. **Menu bar / system tray mode** — run from the Mac menu bar and Windows
   tray (e.g. with `pystray`), with Start/Stop in the menu, so the window
   doesn't have to stay open. Keep the window as "Settings".
3. **Remember settings** — save interval, distance, scroll options to a small
   JSON file in the user's app-data folder and load them on start.
4. **Start automatically** — optional "Open at login" checkbox.
5. **Mac permission flow** — on first run, detect missing Accessibility
   permission and show a friendly screen with a button that opens the right
   System Settings page.
6. **Intel Mac + Apple chip in one download** — universal2 build, or a second
   Intel build in the workflow.
7. **Code signing** — Apple Developer ID signing + notarization (removes the
   "unidentified developer" warning) and a Windows code-signing certificate
   (removes SmartScreen). Needs the owner's paid accounts; store secrets in
   GitHub Actions secrets, never in the repo.
8. **Auto-update check** — compare the running version with the latest GitHub
   Release and show "A new version is available" with a link.
9. **Website** — custom domain, screenshots of the real app, privacy note,
   version number that matches the latest release.
