import customtkinter as ctk
from datetime import datetime
import math


class IdleScreen(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color="#071044")
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.canvas = ctk.CTkCanvas(self, bg="#071044", highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.hour_id = self.minute_id = self.seconds_id = None
        self.date_id = self.swipe_id = None
        self._rings = []
        self._angle = 0

        self._create_rings()
        self._create_text()

        self.bind("<Configure>", self._resize)

        self._update_time()
        self._animate()

        # click anywhere -> auth
        self.bind("<Button-1>", self._go_to_auth)
        self.canvas.bind("<Button-1>", self._go_to_auth)

    def _go_to_auth(self, event):
        self.controller.show_page("auth")

    def _create_text(self):
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
            font=("Inter", 14, "normal")
        )

    def _create_rings(self):
        for color in ("#4b5ce7", "#566bf5", "#9299ff"):
            oid = self.canvas.create_oval(
                0, 0, 0, 0,
                width=20,
                outline=color
            )
            self._rings.append(oid)

    def _resize(self, event):
        w = max(event.width, 1)
        h = max(event.height, 1)

        self.canvas.config(width=w, height=h)

        cx = w / 2
        cy = h / 2

        if h > w:          # portrait
            big_font = int(h * 0.13)
        else:
            big_font = int(h * 0.18)

        sec_font = int(big_font * 0.22)
        date_font = int(big_font * 0.22)

        # ----- hour / minute with more vertical gap -----
        self.canvas.itemconfigure(self.hour_id, font=("Inter", big_font, "bold"))
        self.canvas.coords(self.hour_id, cx, cy - big_font * 0.8)   # moved a bit higher

        self.canvas.itemconfigure(self.minute_id, font=("Inter", big_font, "bold"))
        self.canvas.coords(self.minute_id, cx, cy + big_font * 0.3)  # moved further down

        # ----- seconds with more horizontal gap -----
        self.canvas.itemconfigure(self.seconds_id, font=("Inter", sec_font, "normal"))
        self.canvas.coords(
            self.seconds_id,
            cx + big_font * 0.9,        # was 0.7 → more x margin
            cy + big_font * 0.3
        )

        # date under time
        self.canvas.itemconfigure(self.date_id, font=("Inter", date_font, "normal"))
        self.canvas.coords(self.date_id, cx, cy + big_font * 1.0)

        # swipe text bottom center
        self.canvas.coords(self.swipe_id, w / 2, h - 30)

        if len(self._rings) == 3:
            self.canvas.coords(
                self._rings[0],
                -w * 0.15, h * 0.45,
                w * 0.65, h * 1.1
            )
            self.canvas.itemconfigure(self._rings[0], width=h * 0.025)

            self.canvas.coords(
                self._rings[1],
                w * 0.1, -h * 0.25,
                w * 0.9, h * 0.7
            )
            self.canvas.itemconfigure(self._rings[1], width=h * 0.02)

            self.canvas.coords(
                self._rings[2],
                w * 0.45, h * 0.05,
                w * 1.0, h * 0.9
            )
            self.canvas.itemconfigure(self._rings[2], width=h * 0.02)

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

    def _animate(self):
        dx = math.sin(self._angle) * 0.7
        dy = math.cos(self._angle) * 0.4
        for ring in self._rings:
            self.canvas.move(ring, dx, dy)
        self._angle += 0.03
        self.after(40, self._animate)
