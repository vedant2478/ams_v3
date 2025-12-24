import customtkinter as ctk


class AuthTypePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color="#023055")
        self.controller = controller

        self.grid_rowconfigure((1, 2, 3, 4), weight=1)
        self.grid_columnconfigure(0, weight=1)

        # back to idle
        back_label = ctk.CTkLabel(
            self,
            text="←  Back",
            font=ctk.CTkFont(size=16),
            text_color="white"
        )
        back_label.grid(row=0, column=0, sticky="w", padx=20, pady=(12, 0))
        back_label.bind("<Button-1>", lambda e: self.controller.show_page("idle"))

        title = ctk.CTkLabel(
            self,
            text="Authentication Type",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="white"
        )
        title.grid(row=1, column=0, pady=(20, 8))

        # buttons sized for 600x1024
        self.bio_btn = ctk.CTkButton(
            self,
            text="Biometric\nAuthentication",
            font=ctk.CTkFont(size=18),
            fg_color="#03406d",
            hover_color="#045489",
            border_width=2,
            border_color="#5d87b9",
            corner_radius=24,
            width=200,
            height=70,
        )
        self.bio_btn.grid(row=2, column=0, pady=15)

        self.card_btn = ctk.CTkButton(
            self,
            text="Card\nAuthentication",
            font=ctk.CTkFont(size=18),
            fg_color="#03406d",
            hover_color="#045489",
            border_width=2,
            border_color="#5d87b9",
            corner_radius=24,
            width=200,
            height=70,
            command=self._open_card_auth
        )
        self.card_btn.grid(row=3, column=0, pady=15)

        version = ctk.CTkLabel(
            self,
            text="Version:- 12.9.3",
            font=ctk.CTkFont(size=12),
            text_color="white"
        )
        version.grid(row=4, column=0, pady=(0, 10))

    def _open_card_auth(self):
        self.controller.show_page("card")
