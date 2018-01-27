#!/usr/bin/env python3

import tkinter as tk
from math import exp

class Plot(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title('GlaPlot')

        self._height = 500
        self._width = 500

        self._origin_x = 50
        self._origin_y = self._height - 50

        self._size_x = self._width - self._origin_x
        self._size_y = self._origin_y

        self.pack()
        self._create_canvas()

    def _scale_data(self, seq, minimum, data_range):
        return ((data_point - minimum) / data_range for data_point in seq)

    def _prepare(self, x, y):
        max_x, min_x, max_y, min_y = max(x), min(x), max(y), min(y)
        x_range, y_range = max_x - min_x, max_y - min_y

        scaled_x = self._scale_data(x, min_x, x_range)
        scaled_y =  self._scale_data(y, min_y, y_range)

        self._draw_axes()
        # self._draw_scales(x_range, y_range)

        return scaled_x, scaled_y


    def _create_canvas(self):
        self._canvas = tk.Canvas(self, height=self._height, width=self._width, bg='white')
        self._canvas.pack()

    def _draw_axes(self):
        self._canvas.create_line(self._origin_x, self._origin_y,
                                 self._size_x, self._origin_y)
        self._canvas.create_line(self._origin_x, self._origin_y,
                                 self._origin_x, self._height - self._size_y)

    def _draw_scales(self, x, y):
        x_unit = 50
        y_unit = 50
        print(x_range / x_unit, y_range / y_unit)
        x_scaled, y_scaled = x_range / x_unit, y_range / y_unit


        # Horizontal
        i = 0
        for x in range(self._origin_x, self._size_x, x_unit):
            self._canvas.create_line(x, self._origin_y, x, self._origin_y + 5)
            self._canvas.create_text(x, self._origin_y + 15, text=round(i *  x_scaled, 1))
            i += 1
        # Vertical
        for y in range(self._origin_y, 50, -y_unit):
            self._canvas.create_line(self._origin_x, y, self._origin_x - 5, y)

    def scatter(self, x, y, connect=False, width=3, fill='#5E88D4'):
        x, y = self._prepare(x, y)
        prev_x = prev_y = None
        for x_i, y_i in zip(x, y):
            # print('X -->', x_i, self._size_x, x_i * self._size_x)
            # print('Y -->', y_i, self._size_y, y_i * self._size_y)
            x_i = self._origin_x + x_i * (self._size_x - 50)
            y_i = self._origin_y - y_i * (self._size_y - 50)
            if connect:
                if not (prev_x and prev_y):
                    prev_x, prev_y = x_i, y_i
                self._canvas.create_line(prev_x, prev_y, x_i, y_i,
                                         width=width, fill=fill)
                prev_x, prev_y = x_i, y_i
            else:
                self._canvas.create_oval(x_i - width, y_i - width,
                                         x_i + width, y_i + width,
                                         fill=fill, outline=fill)


root = tk.Tk()
app = Plot(master=root)
# app.scatter(list(range(1, 14)), list(map(exp, range(1, 14))), True)
app.scatter(list(range(3, 14)), list(map(exp, range(3, 14, 1))))
app.mainloop()
