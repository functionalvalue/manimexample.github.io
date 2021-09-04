
# Written By MD Awlad Hossain
# Youtube Cahnnel Funtional Value
# Channel Link : http://youtube.com/FunctionalValue
# FaceBook Page : http://facebook.com/FunctionalValue
# My Profile : http://facebook.com/aawladd
# CopyRight @ Functional Value


# This Code Will run in Manim CE (Community v0.10.0)


from manim import *

class DrawMatrix(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # First Cube
        s1 = Cube(fill_opacity=0.1, stroke_width=4)
        s1.set_color(YELLOW)
        s1.set_stroke(WHITE)
        s1.scale(0.5)
        self.play(DrawBorderThenFill(s1), run_time = 3)
        self.wait()



        # Second Cube
        s2 = s1.copy()
        s2.shift(UP, s1.get_arc_length())
        s2.set_color(BLUE)
        s2.set_stroke(WHITE)
        self.play(ReplacementTransform(s1.copy(), s2), s1.animate.set_opacity(0.5), run_time = 3)
        self.wait()
        
        # Third Cube
        s3 = s1.copy()
        s3.shift(DOWN, s1.get_arc_length())
        s3.set_color(RED)
        s3.set_stroke(WHITE)
        self.play(ReplacementTransform(s1.copy(), s3), s2.animate.set_opacity(0.5), run_time = 3)
        self.play(s3.animate.set_opacity(0.5))
        self.wait()
        
        
        
        # Row 1
        row1 = VGroup(s1, s2, s3)
        self.play(Rotate(row1, 2*PI), run_time = 5)
        self.wait()

        # Row 2
        row2 = row1.copy()
        row2.set_opacity(0.1)
        row2.shift(IN, s2.get_arc_length())
        self.play(ReplacementTransform(row1.copy(), row2), run_time = 3)
        self.play(row2.animate.set_opacity(0.5))

        # Row 3
        row3 = row1.copy()
        row3.set_opacity(0.1)
        row3.shift(OUT, s2.get_arc_length())
        self.play(ReplacementTransform(row1.copy(), row3), run_time = 3)
        self.play(row3.animate.set_opacity(0.5))
        self.wait()
        
        
        # Matri1
        mat1 = VGroup(row1, row2, row3)
        self.play(Rotate(mat1, 2*PI), run_time = 5)
        self.wait()



        # Matrix 2
        mat2 = mat1.copy()
        mat2.set_opacity(0.1)
        mat2.shift(RIGHT,s2.get_arc_length())
        self.play(ReplacementTransform(mat1.copy(), mat2), run_time = 3)
        self.play(mat2.animate.set_opacity(0.5))
        self.wait()


        # Matrix 3
        mat3 = mat1.copy()
        mat3.set_opacity(0.1)
        mat3.shift(LEFT,s2.get_arc_length())
        self.play(ReplacementTransform(mat1.copy(), mat3), run_time = 3)
        self.play(mat3.animate.set_opacity(0.5))
        self.wait()

        # Tensor 1
        ten1 = VGroup(mat1, mat2, mat3)
        self.play(Rotate(ten1, 2*PI), run_time = 15)
