import customtkinter as ctk
from components.header import Header
from pages.idle_screen import IdleScreen
from pages.auth_type import AuthTypePage
from pages.card_auth import CardAuthPage


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Kiosk UI")
        self.attributes("-fullscreen", True)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ---------- header ----------
        self.header = Header(self)
        self.header.grid(row=0, column=0, sticky="nsew")

        # ---------- page container ----------
        self.page_container = ctk.CTkFrame(self, fg_color="#040b36")
        self.page_container.grid(row=1, column=0, sticky="nsew")

        self.page_container.grid_rowconfigure(0, weight=1)
        self.page_container.grid_columnconfigure(0, weight=1)

        # ---------- pages ----------
        self.pages = {}
        self.pages["idle"] = IdleScreen(self.page_container, controller=self)
        self.pages["auth"] = AuthTypePage(self.page_container, controller=self)
        self.pages["card"] = CardAuthPage(self.page_container, controller=self)

        for page in self.pages.values():
            page.grid(row=0, column=0, sticky="nsew")

        # start state: idle is on top
        self.current_page = "idle"
        self.pages["idle"].tkraise()

        # Esc quits app
        self.bind("<Escape>", lambda e: self.destroy())

    # -------- page switching with optional fade --------

    def show_page(self, name: str, animate: bool = True):
        """Raise page by name; manage card timer and optional fade."""
        if name == self.current_page:
            return

        # manage card timer when leaving/entering card page
        if self.current_page == "card":
            self.pages["card"].stop_timer()
        if name == "card":
            self.pages["card"].reset_timer()

        new_page = self.pages[name]

        if not animate:
            new_page.tkraise()
            self.current_page = name
            return

        # simple fade transition
        def step(alpha):
            if alpha <= 0.6:
                new_page.tkraise()
            if alpha <= 1.0:
                self.attributes("-alpha", alpha)
            if alpha < 1.0:
                self.after(20, step, alpha + 0.05)
            else:
                self.attributes("-alpha", 1.0)
                self.current_page = name

        self.after(0, step, 0.6)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = App()
    app.mainloop()
