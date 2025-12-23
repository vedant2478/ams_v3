# pages/auth_type.py
import customtkinter as ctk


class AuthTypePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color="#040b36")
        self.controller = controller

        self.grid_rowconfigure((1, 2, 3, 4), weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ---------- back (to idle) ----------
        back_label = ctk.CTkLabel(
            self,
            text="←  Back",
            font=ctk.CTkFont(size=20),
            text_color="white"
        )
        back_label.grid(row=0, column=0, sticky="w", padx=40, pady=(20, 0))
        back_label.bind("<Button-1>", lambda e: self._go_back())

        # ---------- title ----------
        title = ctk.CTkLabel(
            self,
            text="Authentication Type",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="white"
        )
        title.grid(row=1, column=0, pady=(40, 10))

        # ---------- biometric button ----------
        bio_btn = ctk.CTkButton(
            self,
            text="Biometric\nAuthentication",
            font=ctk.CTkFont(size=22),
            fg_color="#03406d",
            hover_color="#045489",
            border_width=2,
            border_color="#5d87b9",
            corner_radius=40,
            width=450,
            height=160,
            # TODO: add command later
        )
        bio_btn.grid(row=2, column=0, pady=20)

        # ---------- card button ----------
        card_btn = ctk.CTkButton(
            self,
            text="Card\nAuthentication",
            font=ctk.CTkFont(size=22),
            fg_color="#03406d",
            hover_color="#045489",
            border_width=2,
            border_color="#5d87b9",
            corner_radius=40,
            width=450,
            height=160,
            command=self._open_card_auth
        )
        card_btn.grid(row=3, column=0, pady=20)

        # version text bottom
        version = ctk.CTkLabel(
            self,
            text="Version:- 12.9.3",
            font=ctk.CTkFont(size=14),
            text_color="white"
        )
        version.grid(row=4, column=0, pady=(0, 20))

    # ---------- navigation helpers ----------

    def _go_back(self):
        """Back from auth_type → idle page."""
        self.controller.show_page("idle")

    def _open_card_auth(self):
        """Go to card authentication page."""
        self.controller.show_page("card")
