import tkinter as tk
from tkinter import ttk


class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):

        super().__init__(container)
        self['text'] = 'Options'

        # radio buttons
        self.selected_value = tk.IntVar()

        ttk.Radiobutton(
            self,
            text='F to C',
            value=0,
            variable=self.selected_value,
            command=self.change_frame).grid(column=0, row=0, padx=5, pady=5)

        ttk.Radiobutton(
            self,
            text='C to F',
            value=1,
            variable=self.selected_value,
            command=self.change_frame).grid(column=1, row=0, padx=5, pady=5)

        self.grid(column=0, row=1, padx=5, pady=5, sticky='ew')

        # initialize frames
        self.frames = {}
        self.frames[0] = ConverterFrame(
            container,
            'Fahrenheit',
            TemperatureConverter.fahrenheit_to_celsius)
        self.frames[1] = ConverterFrame(
            container,
            'Celsius',
            TemperatureConverter.celsius_to_fahrenheit)

        self.change_frame()

    def change_frame(self):
        frame = self.frames[self.selected_value.get()]
        frame.reset()
        frame.tkraise()