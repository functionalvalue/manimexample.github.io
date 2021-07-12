# Written By MD Awlad Hossain
# Youtube Cahnnel Funtional Value
# Channel Link : http://youtube.com/FunctionalValue
# FaceBook Page : http://facebook.com/FunctionalValue
# My Profile : http://facebook.com/aawladd
# CopyRight @ Functional Value


# This Code Will run in Manim CE (Community v0.8.0)
# To run this code type in Terminal  manim -pql 05ParametricCurve03.py

from manim import *

class ParametricCurve(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)  # Set Camera Orientation
        axes = ThreeDAxes()   # 3D Axes
        resolution_curve = 30    # Resolution of curve
        resolution_sphere = 30    #Resolution of Sphere

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
            x = (1.6**v)*np.cos(v)*(1+np.cos(u)) 
            y =  (-1.6**v)*np.sin(v)*(1+np.cos(u))
            z = (-2*1.6**v)*(1+np.sin(u))
            return np.array([x, y, z])

        gauss_plane = ParametricSurface(
            param_gauss,
            resolution=(resolution_curve, resolution_curve),
            v_min=-10,
            v_max= 10,
            u_min=0,
            u_max=TAU,
        )
        gauss_plane.scale_about_point(0.01, ORIGIN)
        self.play(DrawBorderThenFill(axes))
        self.play(Write(sphere))
        self.play(sphere.animate.set_style(fill_opacity=1),sphere.animate.set_style(stroke_color=GREEN),sphere.animate.set_fill_by_checkerboard(GREEN, BLUE, opacity=0.3))
        self.play(ReplacementTransform(sphere, gauss_plane))
        self.play(gauss_plane.animate.set_style(fill_opacity=1),gauss_plane.animate.set_style(stroke_color=GREEN),gauss_plane.animate.set_fill_by_checkerboard(GREEN, BLUE, opacity=0.4))
        self.play(gauss_plane.animate.scale_about_point(2.5, ORIGIN))
        self.play(gauss_plane.animate.scale_about_point(2/5, ORIGIN))
        self.play(gauss_plane.animate.set_fill_by_checkerboard(ORANGE, YELLOW, opacity=1))

