import tkinter as tk
from tkinter import ttk


class Settings(ttk.Frame):

    def __init__(self, parent, controller, show_timer):
        super(Settings, self).__init__(parent)

        self["style"] = "Background.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        settings_container = ttk.Frame(
            self,
            style="Background.TFrame",
            padding="30 15 30 15",
        )

        settings_container.grid(row=0, column=0, sticky="NSEW", padx=10, pady=10)

        settings_container.columnconfigure(0, weight=1)
        settings_container.rowconfigure(0, weight=1)

        pomodoro_label = ttk.Label(
            settings_container,
            style="LightText.TLabel",
            text="Pomodoro",
        )
        pomodoro_label.grid(row=0, column=0, sticky="W")

        pomodoro_input = tk.Spinbox(
            settings_container,
            from_=0,
            to=120,
            increment=1,
            justify="center",
            textvariable=controller.pomodoro,
            width=10,
        )
        pomodoro_input.grid(row=0, column=1, sticky="EW")

        short_break_label = ttk.Label(
            settings_container,
            style="LightText.TLabel",
            text="Short break",
        )
        short_break_label.grid(row=1, column=0, sticky="W")

        short_break_input = tk.Spinbox(
            settings_container,
            from_=0,
            to=30,
            increment=1,
            justify="center",
            textvariable=controller.short_break,
            width=10,
        )
        short_break_input.grid(row=1, column=1, sticky="EW")

        long_break_label = ttk.Label(
            settings_container,
            style="LightText.TLabel",
            text="Long break",
        )
        long_break_label.grid(row=2, column=0, sticky="W")

        long_break_input = tk.Spinbox(
            settings_container,
            from_=0,
            to=60,
            increment=1,
            justify="center",
            textvariable=controller.long_break,
            width=10,
        )
        long_break_input.grid(row=2, column=1, sticky="EW")

        for child in settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        button_container = ttk.Frame(self, style="Background.TFrame")
        button_container.grid(sticky="EW", padx=10)
        button_container.columnconfigure(0, weight=1)

        timer_button = ttk.Button(
            button_container,
            style="Pomodoro.TButton",
            text="<- Back",
            command=show_timer,
            cursor="hand2",
        )
        timer_button.grid(row=0, column=0, sticky="EW", padx=2)
