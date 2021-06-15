
from manimlib.imports import *
class BarCharExam(Scene):
    def construct(self):
        colors = [RED, GREEN, BLUE, YELLOW, ORANGE]
        values = [0.5, 0.6, 0.9, 0.45, 0.96, 0.73, 0.2, 0.4, 0.49, 0.75, 0.9]
        bar_chart = BarChart(values, bar_colors = colors)
        self.play(DrawBorderThenFill(bar_chart, run_time = 25))
        self.wait(3)