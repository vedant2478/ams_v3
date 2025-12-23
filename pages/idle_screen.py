import customtkinter as ctk
from datetime import datetime
import math


class IdleScreen(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color="#040b36")
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.canvas = ctk.CTkCanvas(self, bg="#040b36", highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.hour_id = self.minuate_id = self.seconds_id = None
        self.date_id = self.swipe_id = None
        self._rings = []
        self._angle = 0

        self._create_rings()
        self._create_text()

        self.bind("<Configure>", self._resize)

        self._update_time()
        self._animate()

        # ---------- click anywhere on idle -> auth ----------
        self.bind("<Button-1>", self._go_to_auth)
        self.canvas.bind("<Button-1>", self._go_to_auth)

    def _go_to_auth(self, event):
        self.controller.show_page("auth")

    # ---------- create items ----------

    def _create_text(self):
        # temporary dummy; actual size/coords set in _resize
        self.hour_id = self.canvas.create_text(
            0, 0, text="", fill="white", font=("Inter", 10, "bold")
        )
        self.minute_id = self.canvas.create_text(
            0, 0, text="", fill="white", font=("Inter", 10, "bold")
        )
        self.seconds_id = self.canvas.create_text(
            0, 0, text="", fill="#9fffe0", font=("Inter", 10, "bold")
        )
        self.date_id = self.canvas.create_text(
            0, 0, text="", fill="#9fffe0", font=("Inter", 10, "bold")
        )
        self.swipe_id = self.canvas.create_text(
            0, 0,
            text="Swipe to Continue",
            fill="white",
            font=("Inter", 18, "normal")
        )

    def _create_rings(self):
        # create 3 placeholder ovals; geometry set in _resize
        for color in ("#4b5ce7", "#566bf5", "#9299ff"):
            oid = self.canvas.create_oval(
                0, 0, 0, 0,
                width=30,
                outline=color
            )
            self._rings.append(oid)

    # ---------- responsive layout ----------

    def _resize(self, event):
        w = max(event.width, 1)
        h = max(event.height, 1)

        self.canvas.config(width=w, height=h)

        cx = w / 2
        cy = h / 2

        # tweak font scale for portrait vs landscape
        if h > w:          # portrait: make digits smaller
            big_font = int(h * 0.18)
        else:              # landscape
            big_font = int(h * 0.25)

        sec_font = int(big_font * 0.25)
        date_font = int(big_font * 0.25)

        # hour / minute
        self.canvas.itemconfigure(self.hour_id, font=("Inter", big_font, "bold"))
        self.canvas.coords(self.hour_id, cx, cy - big_font * 0.8)

        self.canvas.itemconfigure(self.minute_id, font=("Inter", big_font, "bold"))
        self.canvas.coords(self.minute_id, cx, cy + big_font * 0.2)

        # seconds to the right
        self.canvas.itemconfigure(self.seconds_id, font=("Inter", sec_font, "bold"))
        self.canvas.coords(
            self.seconds_id,
            cx + big_font * 0.8,
            cy + big_font * 0.2
        )

        # date under time
        self.canvas.itemconfigure(self.date_id, font=("Inter", date_font, "bold"))
        self.canvas.coords(self.date_id, cx, cy + big_font * 0.9)

        # swipe text bottom center
        self.canvas.coords(self.swipe_id, w / 2, h - 40)

        # rings (unchanged)
        if len(self._rings) == 3:
            self.canvas.coords(
                self._rings[0],
                -w * 0.1, h * 0.45,
                w * 0.7, h * 1.15
            )
            self.canvas.itemconfigure(self._rings[0], width=h * 0.035)

            self.canvas.coords(
                self._rings[1],
                w * 0.15, -h * 0.25,
                w * 0.95, h * 0.75
            )
            self.canvas.itemconfigure(self._rings[1], width=h * 0.03)

            self.canvas.coords(
                self._rings[2],
                w * 0.45, h * 0.05,
                w * 1.1, h * 0.95
            )
            self.canvas.itemconfigure(self._rings[2], width=h * 0.03)

    # ---------- clock ----------

    def _update_time(self):
        now = datetime.now()
        self.canvas.itemconfigure(self.hour_id, text=now.strftime("%H"))
        self.canvas.itemconfigure(self.minute_id, text=now.strftime("%M"))
        self.canvas.itemconfigure(self.seconds_id, text=now.strftime("%S"))
        self.canvas.itemconfigure(
            self.date_id,
            text=now.strftime("%a %d").upper()
        )
        self.after(1000, self._update_time)

    # ---------- animation ----------

    def _animate(self):
        dx = math.sin(self._angle) * 0.7
        dy = math.cos(self._angle) * 0.4
        for ring in self._rings:
            self.canvas.move(ring, dx, dy)
        self._angle += 0.03
        self.after(40, self._animate)
