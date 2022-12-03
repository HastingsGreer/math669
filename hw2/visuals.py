from manim import *
import manim

import math

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait()
        plane = NumberPlane([-10, 10, .5], [-5, 5, .5]).add_coordinates()
        self.play(Create(plane))
        self.wait()

        plane.prepare_for_nonlinear_transform()



        self.play(
                plane.animate.apply_function(
                    lambda p: [
                        p[0] * p[0] - p[1] * p[1], 2 * p[0] * p[1], 0
                        ]
                    )
                )
        self.wait()
        self.play(
                plane.animate.apply_function(
                    lambda p: [
                        p[0], p[1], p[2]
                        ]
                    )
                )
        self.wait()

        


         
