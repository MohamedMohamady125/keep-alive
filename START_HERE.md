# Start here

Step-by-step guide to turn this folder into a real product with VS Code and
Claude Code. Do the parts in order.

## Part 1 — Open it in VS Code
1. Unzip this folder and move it somewhere permanent, e.g. your home folder:
   `~/keep-alive`.
2. Open VS Code → **File → Open Folder…** → choose `keep-alive`.
3. Open the terminal inside VS Code: **View → Terminal**.

## Part 2 — Run the app from the code
Paste in the VS Code terminal:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python keep_alive.py
```
The Keep Alive window should open. If the mouse doesn't move, allow your
terminal / VS Code under System Settings → Privacy & Security → Accessibility.

## Part 3 — Start Claude Code
In the same terminal:
```
claude
```
Claude Code reads `CLAUDE.md` automatically, so it already knows what the
product is and what to build next. A good first message:

> Read CLAUDE.md and walk me through the roadmap. Start with step 1 (app icon)
> and step 2 (menu bar / tray mode). Explain each change before you make it,
> and run the app after each change so I can test it.

Do the roadmap one step at a time, and test the app after each step.

## Part 4 — Put it on GitHub (free builds + download links)
1. Make a free account at github.com.
2. Create a new **empty** repository named `keep-alive` (no README).
3. Ask Claude Code:
   > Set up git in this folder and push it to my new GitHub repo
   > https://github.com/MY-USERNAME/keep-alive
4. In `website/index.html`, replace `YOUR-GITHUB-USERNAME` with your
   GitHub username (or ask Claude Code to do it).

## Part 5 — Make your first release
Ask Claude Code:
> Tag and push version v1.0.0.

GitHub then builds the Mac and Windows apps (about 5–10 minutes). Check the
**Actions** tab; when it's green, the **Releases** page has
`KeepAlive-mac.zip` and `KeepAlive.exe`.

## Part 6 — Put the website online
1. On GitHub: repo **Settings → Pages → Source: GitHub Actions**.
2. Push any change to `website/` (or run "Deploy website" from the Actions tab).
3. Your site goes live at `https://MY-USERNAME.github.io/keep-alive/`.
   The download buttons already point to your latest release.

Send people that website link. That's the product.

## Later: make it feel professional
- **Apple Developer account ($99/year)** → sign + notarize the Mac app so
  there's no security warning.
- **Windows code-signing certificate** → removes the "Windows protected your
  PC" warning.
- Own domain name (e.g. keepalive.app) pointed at GitHub Pages.
Claude Code can set up the signing steps once you have the accounts.
