import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


class TemperatureConverter:#this should be changed to search class
    @staticmethod
    def fahrenheit_to_celsius(f, format=True):
        result = (f - 32) * 5/9
        if format:
            return f'{f} Fahrenheit = {result:.2f} Celsius'
        return result

    @staticmethod
    def celsius_to_fahrenheit(c, format=True):
        result = c * 9/5 + 32
        if format:
            return f'{c} Celsius = {result:.2f} Fahrenheit'
        return result


class ConverterFrame(ttk.Frame):
    def __init__(self, container, type, converter):
        super().__init__(container)

        self.type = type
        self.converter = converter

        # field options
        options = {'padx': 5, 'pady': 0}

        # temperature label
        self.ingredientsLabel = ttk.Label(self, text=self.type)
        self.ingredientsLabel.grid(column=0, row=0, sticky='w',  **options)

        # temperature entry
        self.temperature = tk.StringVar()
        self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
        self.temperature_entry.grid(column=1, row=0, sticky='w', **options)
        self.temperature_entry.focus()

        # button
        self.searchButton = ttk.Button(self, text='Search')
        self.searchButton.grid(column=2, row=0, sticky='w', **options)
        self.searchButton.configure(command=self.convert)

        # result label
        self.result_label = ttk.Label(self)
        self.result_label.grid(row=1, columnspan=7, **options)

        # add padding to the frame and show it
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

    def convert(self, event=None):
        """  Handle button click event
        """
        try:
            input_value = float(self.temperature.get())
            result = self.converter(input_value)
            self.result_label.config(text=result)
        except ValueError as error:
            showerror(title='Error', message=error)

    def reset(self):
        self.temperature_entry.delete(0, "end")
        self.result_label.text = ''


class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):

        super().__init__(container)
        self['text'] = 'Options'

        # radio buttons
        self.selected_value = tk.IntVar()

        ttk.Radiobutton(
            self,
            text='Non-Vegetarian',
            value=0,
            variable=self.selected_value,
            command=self.change_frame).grid(column=0, row=0, padx=5, pady=5)

        ttk.Radiobutton(
            self,
            text='Vegetarian',
            value=1,
            variable=self.selected_value,
            command=self.change_frame).grid(column=1, row=0, padx=5, pady=5)

        self.grid(column=0, row=1, padx=5, pady=5, sticky='ew')

        # initialize frames
        self.frames = {}
        self.frames[0] = ConverterFrame(
            container,
            'Enter Ingredients',
            TemperatureConverter.fahrenheit_to_celsius
            )
        self.frames[1] = ConverterFrame(
            container,
            'Enter Ingredients',
            TemperatureConverter.celsius_to_fahrenheit
            )

        self.change_frame()

    def change_frame(self):
        frame = self.frames[self.selected_value.get()]
        frame.reset()
        frame.tkraise()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Fridge Recipe')
        #self.geometry('350x120')
        self.resizable(False, False)


if __name__ == "__main__":
    app = App()
    ControlFrame(app)
    app.mainloop()