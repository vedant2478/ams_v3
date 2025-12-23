import customtkinter as ctk


class Footer(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#040b36")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # version in left bottom
        version_label = ctk.CTkLabel(
            self,
            text="v.122.9.3",
            font=ctk.CTkFont(size=12)
        )
        version_label.grid(row=0, column=0, sticky="w", padx=12, pady=6)

        # center swipe area
        center_frame = ctk.CTkFrame(self, fg_color="transparent")
        center_frame.grid(row=0, column=1)

        arrow_label = ctk.CTkLabel(
            center_frame,
            text="︿︿",
            font=ctk.CTkFont(size=22, weight="bold")
        )
        arrow_label.pack(anchor="center")

        swipe_label = ctk.CTkLabel(
            center_frame,
            text="Swipe to Continue",
            font=ctk.CTkFont(size=14)
        )
        swipe_label.pack(anchor="center", pady=(0, 2))
    