import customtkinter as ctk


class CardAuthPage(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color="#040b36")   # dark blue
        self.controller = controller

        # layout
        self.grid_rowconfigure((1, 2, 3, 4), weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ---------- back text ----------
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
            text="Card Authentication",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="white"
        )
        title.grid(row=1, column=0, pady=(40, 20))

        # ---------- scanner icon ----------
        icon_frame = ctk.CTkFrame(self, fg_color="transparent")
        icon_frame.grid(row=2, column=0, pady=10)

        canvas = ctk.CTkCanvas(
            icon_frame,
            width=260,
            height=220,
            bg="#023055",
            highlightthickness=0
        )
        canvas.pack()

        line_w = 14
        corner = 30
        x1, y1, x2, y2 = 30, 20, 230, 200

        # four corner brackets
        canvas.create_line(x1, y1 + corner, x1, y1, x1 + corner, y1,
                           width=line_w, fill="white", capstyle="round")
        canvas.create_line(x2 - corner, y1, x2, y1, x2, y1 + corner,
                           width=line_w, fill="white", capstyle="round")
        canvas.create_line(x1, y2 - corner, x1, y2, x1 + corner, y2,
                           width=line_w, fill="white", capstyle="round")
        canvas.create_line(x2 - corner, y2, x2, y2, x2, y2 - corner,
                           width=line_w, fill="white", capstyle="round")

        # middle bar
        canvas.create_line(x1 + 10, (y1 + y2) / 2,
                           x2 - 10, (y1 + y2) / 2,
                           width=line_w, fill="white", capstyle="round")
        # [web:188][web:83]

        # ---------- progress bar ----------
        self.progress = ctk.CTkProgressBar(
            self,
            orientation="horizontal",
            width=360,
            height=26,
            corner_radius=25,
            fg_color="#d0d3d9",
            progress_color="#0b1118",
            mode="determinate"
        )
        self.progress.grid(row=3, column=0, pady=(40, 10))
        self.progress.set(0)  # [web:181][web:198]

        # hint text with remaining time
        self.remaining_var = ctk.StringVar(value="Time remaining: 60 s")
        hint = ctk.CTkLabel(
            self,
            textvariable=self.remaining_var,
            font=ctk.CTkFont(size=18),
            text_color="white"
        )
        hint.grid(row=3, column=0, pady=(80, 10), sticky="n")

        # version label at bottom
        version = ctk.CTkLabel(
            self,
            text="Version:- 12.9.3",
            font=ctk.CTkFont(size=14),
            text_color="white"
        )
        version.grid(row=4, column=0, pady=(0, 20))

        # timer state
        self._timer_running = False
        self._after_id = None

    # ---------- navigation ----------

    def _go_back(self):
        """Back arrow click: go to Authentication Type page."""
        self.controller.show_page("auth")

    # ---------- progress animation (60 seconds) ----------

    def reset_timer(self):
        """Reset bar and countdown to full 60 seconds and start running."""
        # cancel any pending callback
        if self._after_id is not None:
            try:
                self.after_cancel(self._after_id)
            except Exception:
                pass
            self._after_id = None

        self._elapsed_ms = 0
        self._tick_interval = 100  # 100 ms
        self.progress.set(0)
        self.remaining_var.set("Time remaining: 60 s")
        self._timer_running = True
        self._after_id = self.after(self._tick_interval, self._progress_tick)

    def stop_timer(self):
        """Stop timer, used when leaving this page."""
        self._timer_running = False
        if self._after_id is not None:
            try:
                self.after_cancel(self._after_id)
            except Exception:
                pass
            self._after_id = None

    def _progress_tick(self):
        if not self._timer_running:
            return

        total_ms = 60000  # 60 seconds
        self._elapsed_ms += self._tick_interval

        remaining_ms = max(total_ms - self._elapsed_ms, 0)
        remaining_sec = int(remaining_ms / 1000)

        fraction = min(self._elapsed_ms / total_ms, 1.0)
        self.progress.set(fraction)
        self.remaining_var.set(f"Time remaining: {remaining_sec} s")

        if self._elapsed_ms < total_ms:
            self._after_id = self.after(self._tick_interval, self._progress_tick)
        else:
            self._timer_running = False
            # TEMP behaviour: go straight to PIN page
            self.controller.show_page("pin")


