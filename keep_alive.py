"""
Keep Alive - simulates user activity so your computer (and any app that
watches for input) thinks someone is using it.

Run from source:
    pip install pyautogui
    python keep_alive.py
"""

import sys
import threading
import time
import tkinter as tk
from tkinter import ttk, messagebox

import pyautogui

APP_NAME = "Keep Alive"
pyautogui.FAILSAFE = False  # don't stop just because the cursor sits in a corner


class KeepAliveApp:
    def __init__(self, root):
        self.root = root
        root.title(APP_NAME)
        root.resizable(False, False)

        self.running = False
        self.nudges = 0
        self.started_at = 0.0
        self.direction = 1

        frame = ttk.Frame(root, padding=18)
        frame.grid()

        ttk.Label(frame, text=APP_NAME, font=("", 14, "bold")).grid(
            row=0, column=0, columnspan=2, pady=(0, 10)
        )

        ttk.Label(frame, text="Nudge every (seconds):").grid(row=1, column=0, sticky="w")
        self.interval = tk.IntVar(value=6)
        ttk.Spinbox(frame, from_=5, to=600, textvariable=self.interval, width=6).grid(
            row=1, column=1, padx=(8, 0)
        )

        ttk.Label(frame, text="Mouse move (pixels):").grid(row=2, column=0, sticky="w", pady=(6, 0))
        self.distance = tk.IntVar(value=50)
        ttk.Spinbox(frame, from_=1, to=50, textvariable=self.distance, width=6).grid(
            row=2, column=1, padx=(8, 0), pady=(6, 0)
        )

        ttk.Label(frame, text="Stop after (minutes, 0 = never):").grid(
            row=3, column=0, sticky="w", pady=(6, 0)
        )
        self.stop_after = tk.IntVar(value=0)
        ttk.Spinbox(frame, from_=0, to=1440, textvariable=self.stop_after, width=6).grid(
            row=3, column=1, padx=(8, 0), pady=(6, 0)
        )

        self.scroll = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            frame, text="Scroll up and down every", variable=self.scroll
        ).grid(row=4, column=0, sticky="w", pady=(10, 0))
        scroll_row = ttk.Frame(frame)
        scroll_row.grid(row=4, column=1, padx=(8, 0), pady=(10, 0), sticky="w")
        self.scroll_every = tk.IntVar(value=3)
        ttk.Spinbox(scroll_row, from_=1, to=100, textvariable=self.scroll_every, width=4).pack(
            side="left"
        )
        ttk.Label(scroll_row, text=" nudges").pack(side="left")

        self.press_key = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            frame, text="Also tap Shift (keyboard activity)", variable=self.press_key
        ).grid(row=5, column=0, columnspan=2, sticky="w", pady=(6, 0))

        self.button = ttk.Button(frame, text="Start", command=self.toggle)
        self.button.grid(row=6, column=0, columnspan=2, sticky="ew", pady=(14, 6))

        self.status = ttk.Label(frame, text="Stopped", foreground="gray")
        self.status.grid(row=7, column=0, columnspan=2)

        root.protocol("WM_DELETE_WINDOW", self.quit)

    # ---- helpers -------------------------------------------------------
    def _int(self, var, default, low):
        try:
            return max(low, int(var.get()))
        except (tk.TclError, ValueError):
            return default

    def set_status(self, text, color="green"):
        self.root.after(0, lambda: self.status.config(text=text, foreground=color))

    # ---- start / stop --------------------------------------------------
    def toggle(self):
        if self.running:
            self.stop("Stopped")
        else:
            self.running = True
            self.nudges = 0
            self.started_at = time.time()
            self.button.config(text="Stop")
            self.set_status("Running…")
            threading.Thread(target=self.loop, daemon=True).start()

    def stop(self, message, color="gray"):
        self.running = False
        self.root.after(0, lambda: self.button.config(text="Start"))
        self.set_status(message, color)

    # ---- worker --------------------------------------------------------
    def loop(self):
        while self.running:
            limit = self._int(self.stop_after, 0, 0)
            if limit and time.time() - self.started_at >= limit * 60:
                self.stop(f"Stopped after {limit} min")
                return
            if not self.nudge():
                return
            waited, interval = 0.0, self._int(self.interval, 30, 1)
            while self.running and waited < interval:
                time.sleep(0.2)
                waited += 0.2

    def nudge(self):
        d = self._int(self.distance, 5, 1)
        try:
            # move d pixels and stay there, so the cursor ends somewhere new each
            # nudge; reverse at the screen edges so it never runs off-screen
            x, _y = pyautogui.position()
            width, _h = pyautogui.size()
            if not (0 < x + d * self.direction < width - 1):
                self.direction = -self.direction
            pyautogui.moveRel(d * self.direction, 0, duration=0.1)
            scrolled = False
            if self.scroll.get() and (self.nudges + 1) % self._int(self.scroll_every, 3, 1) == 0:
                # scroll down, then back up the same amount so the page ends where it was
                for _ in range(3):
                    pyautogui.scroll(-2)
                    time.sleep(0.15)
                for _ in range(3):
                    pyautogui.scroll(2)
                    time.sleep(0.15)
                scrolled = True
            if self.press_key.get():
                pyautogui.press("shift")
        except Exception as exc:  # usually a missing macOS permission
            self.stop("Couldn't move the mouse", "red")
            hint = ""
            if sys.platform == "darwin":
                hint = (
                    "\n\nOn Mac, open System Settings > Privacy & Security > "
                    "Accessibility and turn on Keep Alive, then try again."
                )
            self.root.after(0, lambda: messagebox.showerror(APP_NAME, f"{exc}{hint}"))
            return False
        self.nudges += 1
        action = "scrolled" if scrolled else "moved"
        self.set_status(
            f"Running… {self.nudges} nudges (last {action} {time.strftime('%H:%M:%S')})"
        )
        return True

    def quit(self):
        self.running = False
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    KeepAliveApp(root)
    root.mainloop()
