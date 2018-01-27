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

    def _scale_data(self, seq, a, b):
        return [(data_point - a) / b for data_point in seq]

    def _prepare(self, x, y):
        self._draw_axes()
        self._draw_scales()
        max_x, min_x, max_y, min_y = max(x), min(x), max(y), min(y)
        x_range, y_range = max_x - min_x, max_y - min_y
        # global_max = max(max_x, max_y)
        return self._scale_data(x, min_x, x_range), self._scale_data(y, min_y, y_range)

    def _create_canvas(self):
        self._canvas = tk.Canvas(self, height=self._height, width=self._width, bg='white')
        self._canvas.pack()

    def _draw_axes(self):
        self._canvas.create_line(self._origin_x, self._origin_y,
                                 self._size_x, self._origin_y)
        self._canvas.create_line(self._origin_x, self._origin_y,
                                 self._origin_x, self._height - self._size_y)

    def _draw_scales(self):
        x_units = 25
        y_units = 25
        # Horizontal
        for x in range(self._origin_x, self._size_x, x_units):
            self._canvas.create_line(x, self._origin_y, x, self._origin_y + 5)
        # Vertical
        for y in range(self._origin_y, 50, -y_units):
            self._canvas.create_line(self._origin_x, y, self._origin_x - 5, y)

    def scatter(self, x, y, connect=False, width=4, fill='#5E88D4'):
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
app.scatter(list(range(1, 14)), list(map(exp, range(1, 14))))
app.mainloop()
