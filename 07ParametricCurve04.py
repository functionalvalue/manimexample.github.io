# Written By MD Awlad Hossain
# Youtube Cahnnel Funtional Value
# Channel Link : http://youtube.com/FunctionalValue
# FaceBook Page : http://facebook.com/FunctionalValue
# My Profile : http://facebook.com/aawladd
# CopyRight @ Functional Value


# This Code Will run in Manim CE (Community v0.7.0)

from manim import *

class Toruss(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)  # Set Camera Orientation
        axes = ThreeDAxes()   # 3D Axes
        resolution_curve = 80      # Resolution of curve
        resolution_sphere = 80    #Resolution of Sphere

        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]),
            u_range=[-PI/2, PI/2],
            v_range=[0, TAU],
            checkerboard_colors=[RED_D, RED_E], resolution=(resolution_sphere,resolution_sphere)
        )                                                                                                       # Sphere Function 
        sphere.scale(1.5)

        def param_gauss(u, v):                                                                                     # Curve Function 
            x = (4 + np.sin(u))*np.cos(v)
            y = (4 + np.sin(u))*np.sin(v)
            z = np.cos(u)
            return np.array([x, y, z])

        gauss_plane = Surface(
            param_gauss,
            resolution=(resolution_curve, resolution_curve),
            u_range=[0, TAU],
            v_range=[0,TAU]
        )
        gauss_plane.scale(0.5)

        self.play(DrawBorderThenFill(axes), run_time = 1.5)
        self.play(Write(sphere), run_time = 5)
        self.play(ReplacementTransform(sphere, gauss_plane), run_time = 15)
        self.play(gauss_plane.animate.set_style(fill_opacity=1),gauss_plane.animate.set_style(stroke_color=GREEN),gauss_plane.animate.set_fill_by_checkerboard(GREEN, BLUE, opacity=0.1), run_time = 5)
        self.play(gauss_plane.animate.scale(2), run_time = 3)
        self.begin_ambient_camera_rotation(rate=0.05)
        self.play(gauss_plane.animate.set_fill_by_checkerboard(ORANGE, YELLOW, opacity=0.5), run_time = 2)
        self.wait(10)
        self.stop_ambient_camera_rotation()