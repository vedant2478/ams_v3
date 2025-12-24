import customtkinter as ctk
from components.header import Header
from pages.idle_screen import IdleScreen
from pages.auth_type import AuthTypePage
from pages.card_auth import CardAuthPage
from pages.pin_entry import PinEntryPage


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Kiosk UI")
        self.attributes("-fullscreen", True)
        # fixed portrait window for kiosk
        # self.geometry("600x1024")
        self.resizable(False, False)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # header
        self.header = Header(self)
        self.header.grid(row=0, column=0, sticky="nsew")

        # page container
        self.page_container = ctk.CTkFrame(self, fg_color="#071044")
        self.page_container.grid(row=1, column=0, sticky="nsew")

        self.page_container.grid_rowconfigure(0, weight=1)
        self.page_container.grid_columnconfigure(0, weight=1)

        # pages
        self.pages = {}
        self.pages["idle"] = IdleScreen(self.page_container, controller=self)
        self.pages["auth"] = AuthTypePage(self.page_container, controller=self)
        self.pages["card"] = CardAuthPage(self.page_container, controller=self)
        self.pages["pin"] = PinEntryPage(self.page_container, controller=self)

        for page in self.pages.values():
            page.grid(row=0, column=0, sticky="nsew")

        self.current_page = "idle"
        self.pages["idle"].tkraise()

        self.bind("<Escape>", lambda e: self.destroy())

    def show_page(self, name: str):
        """Instant switch between pages."""
        if name == self.current_page:
            return

        if self.current_page == "card":
            self.pages["card"].stop_timer()
        if name == "card":
            self.pages["card"].reset_timer()

        page = self.pages[name]
        page.tkraise()
        self.current_page = name


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = App()
    app.mainloop()
