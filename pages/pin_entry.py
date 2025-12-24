import customtkinter as ctk


class PinEntryPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color="#023055")
        self.controller = controller

        self.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure(0, weight=1)

        back_label = ctk.CTkLabel(
            self,
            text="←  Back",
            font=ctk.CTkFont(size=16),
            text_color="white"
        )
        back_label.grid(row=0, column=0, sticky="w", padx=20, pady=(12, 0))
        back_label.bind("<Button-1>", lambda e: self.controller.show_page("auth"))

        self.pin = ""
        self.max_len = 5

        dots_frame = ctk.CTkFrame(self, fg_color="transparent")
        dots_frame.grid(row=1, column=0, pady=(20, 5))

        self.dot_labels = []
        for i in range(self.max_len):
            lbl = ctk.CTkLabel(
                dots_frame,
                text="●",
                width=30,
                height=30,
                fg_color="#345d86",
                corner_radius=15,
                font=ctk.CTkFont(size=20),
                text_color="#345d86",
            )
            lbl.grid(row=0, column=i, padx=4)
            self.dot_labels.append(lbl)

        self.status_label = ctk.CTkLabel(
            self,
            text="",
            font=ctk.CTkFont(size=14),
            text_color="white"
        )
        self.status_label.grid(row=1, column=0, pady=(90, 5))

        sep = ctk.CTkFrame(self, height=1, fg_color="white")
        sep.grid(row=2, column=0, sticky="ew", padx=60, pady=(6, 6))

        keypad_frame = ctk.CTkFrame(self, fg_color="transparent")
        keypad_frame.grid(row=3, column=0, pady=10)

        btn_cfg = dict(
            master=keypad_frame,
            width=120,
            height=60,
            corner_radius=20,
            fg_color="#345d86",
            hover_color="#406e9e",
            font=ctk.CTkFont(size=20),
        )

        keys = [
            ("1", 0, 0), ("2", 0, 1), ("3", 0, 2),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),
            ("⌫", 3, 0), ("0", 3, 1), ("↵", 3, 2),
        ]

        for text, r, c in keys:
            b = ctk.CTkButton(
                text=text,
                command=lambda t=text: self._on_key(t),
                **btn_cfg
            )
            b.grid(row=r, column=c, padx=12, pady=8)

        version = ctk.CTkLabel(
            self,
            text="Version:- 12.9.3",
            font=ctk.CTkFont(size=12),
            text_color="white"
        )
        version.grid(row=4, column=0, pady=(0, 10))

    def _on_key(self, key: str):
        if key.isdigit():
            if len(self.pin) < self.max_len:
                self.pin += key
                self.status_label.configure(text="")
        elif key == "⌫":
            self.pin = self.pin[:-1]
            self.status_label.configure(text="")
        elif key == "↵":
            self._check_pin()
        self._update_dots()

    def _update_dots(self):
        for i, lbl in enumerate(self.dot_labels):
            if i < len(self.pin):
                lbl.configure(text="●", text_color="white")
            else:
                lbl.configure(text="●", text_color="#345d86")

    def _check_pin(self):
        # demo PIN; change as needed
        if self.pin == "12345":
            self.status_label.configure(text="PIN OK", text_color="#9fffe0")
        else:
            self.status_label.configure(text="Incorrect Pin", text_color="#ff8080")
            self.pin = ""
            self._update_dots()
