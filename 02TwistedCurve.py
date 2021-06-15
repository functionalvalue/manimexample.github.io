# Written By MD Awlad Hossain
# Youtube Cahnnel Funtional Value
# Channel Link : http://youtube.com/FunctionalValue
# FaceBook Page : http://facebook.com/FunctionalValue
# My Profile : http://facebook.com/aawladd
# CopyRight @ Functional Value


# This Code Will run in Manim CE (Community v0.7.0)

from manim import *

class TwistedCurve(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)  # Set Camera Orientation
        axes = ThreeDAxes()   # 3D Axes
        resolution_curve = 150      # Resolution of curve
        resolution_sphere = 80    #Resolution of Sphere

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
            checkerboard_colors=[RED_D, RED_E], resolution=(resolution_sphere,resolution_sphere)
        )                                                                                                       # Sphere Function 
        sphere.scale_about_point(1.5, ORIGIN)

        def param_gauss(u, v):                                                                                     # Curve Function 
            x = np.cos(v) * (10 - (5/4 + np.sin(3*u))* np.sin(u-3*v))
            y = (10 - (5/4 + np.sin(3*u))* np.sin(u-3*v))*np.sin(v)
            z = -np.cos(u - 3*v) * (5/4 + np.sin(3*u))
            return np.array([x, y, z])

        gauss_plane = ParametricSurface(
            param_gauss,
            resolution=(resolution_curve, resolution_curve),
            v_min=-6,
            v_max=+6,
            u_min=-6,
            u_max=+6,
        )
        gauss_plane.scale_about_point(0.2, ORIGIN)

        self.play(DrawBorderThenFill(axes), run_time = 1.5)
        self.play(Write(sphere), run_time = 5)
        self.play(ReplacementTransform(sphere, gauss_plane), run_time = 15)
        self.play(gauss_plane.animate.set_style(fill_opacity=1),gauss_plane.animate.set_style(stroke_color=GREEN),gauss_plane.animate.set_fill_by_checkerboard(GREEN, BLUE, opacity=0.1), run_time = 5)
        self.play(gauss_plane.animate.scale_about_point(1.5, ORIGIN), run_time = 3)
        self.begin_ambient_camera_rotation(rate=0.05)
        self.play(gauss_plane.animate.set_fill_by_checkerboard(ORANGE, YELLOW, opacity=0.5), run_time = 2)
        self.wait(10)
        self.stop_ambient_camera_rotation()