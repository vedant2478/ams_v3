import customtkinter as ctk


class Header(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#040b36")  # deep navy

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # left: status dot + text
        left_frame = ctk.CTkFrame(self, fg_color="transparent")
        left_frame.grid(row=0, column=0, sticky="w", padx=12, pady=6)

        status_dot = ctk.CTkLabel(
            left_frame, text="●", text_color="#16c754",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        status_dot.grid(row=0, column=0, sticky="w")

        status_label = ctk.CTkLabel(
            left_frame, text="  System Ready",
            font=ctk.CTkFont(size=14)
        )
        status_label.grid(row=0, column=1, sticky="w")

        # right: code text
        right_label = ctk.CTkLabel(
            self, text="DAKC R0 - 001",
            font=ctk.CTkFont(size=14)
        )
        right_label.grid(row=0, column=1, sticky="e", padx=12, pady=6)
