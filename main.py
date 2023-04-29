#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys

from solid import *
from solid.utils import *
import roller_coupler

SEGMENTS = 200

screw_hole_diameter_2_5 = 2.35
screw_hole_diameter_3 = 2.85

INNER_CYLINDER_DIAMETER = 28.9
OUTER_PIPE_HOLE_DIAMETER = 32.3
BEARING_SHAFT = 19.85
BEARING_HOLE_DIAMETER = 27.4

# 13.75 real diameter
MOTOR_COUPLER_DIAMETER = 14.25

# 25.05 real diameter
GEARBOX_DIAMETER = 25.25
# 6.96 real diameter
GEARBOX_HOLE_DIAMETER = 7.30

BEARING_SHAFT_COUPLER_DIAMETER = 19.8
BEARING_SHAFT_COUPLER_HOLE_DIAMETER = 20.2

aluminum_pipe_offset = 25

aluminum_pipe = translate([0, 0, aluminum_pipe_offset])(color('magenta')(
    cylinder(d = OUTER_PIPE_HOLE_DIAMETER , h = 100)
    - translate([0, 0, -1])(cylinder(d = INNER_CYLINDER_DIAMETER, h = 200))
))

motor_coupler = cylinder(d = MOTOR_COUPLER_DIAMETER, h = 5.5, segments = 6)

gearbox = cylinder(d = GEARBOX_DIAMETER, h = 30)

m2_5_screw = (
    cylinder(d = 5, h = 2)
    + cylinder(d = screw_hole_diameter_2_5, h = 8)
)


# 2.5 screw

def bearing_holder_holes(screw_hole):
    hole = translate([15.5, 0, -1])(screw_hole)
    return (
        hole
        + rotate([0, 0, 90])(hole)
        + rotate([0, 0, 180])(hole)
        + rotate([0, 0, 270])(hole)
    )

bearing_holder_both = (
    cylinder(d = 44, h = 3)
    + translate([0, 0, 2])(roller_coupler.full(10))
    - translate([0, 0, 3])(cylinder(d = BEARING_HOLE_DIAMETER, h = 3.9))
#    - translate([0, 0, -0.001])(cylinder(d = 35, h = 6.5 - 3.5))
    - cylinder(d = 24, h = 50)
    #+ translate([0, 0, 2.5])(color('magenta')(cylinder(d = 27, h = 4)))
    #+ bearing_holder_cap
)

bearing_holder_top = translate([0, 0, 9])(
    bearing_holder_both 
    - cylinder(d = 100, h = 3)
    - bearing_holder_holes(cylinder(d = screw_hole_diameter_2_5, h = 12))
)

bearing_holder_bottom = translate([0, 0, 9])(
    bearing_holder_both 
    - translate([0, 0, 3])(cylinder(d = 100, h = 20))
    - bearing_holder_holes(cylinder(d = 2.8, h = 12))
)

wire_hole = rotate([0, 0, 45])(translate([-5/2.0, 5.4, -1])(cube([5, 6, 60])))


m3_pipe_connector = rotate([0, 0, 225])(translate([17, 0, aluminum_pipe_offset + 2.5])(rotate([0, -90, 0])(
        cylinder(d = 5, h = 1)
        + cylinder(d = screw_hole_diameter_3, h = 17)
    )))

m3_pipe_connector_space = rotate([0, 0, 225])(translate([17, 0, aluminum_pipe_offset + 2.5])(rotate([0, -90, 0])(
        cylinder(d = 5, h = 17)
    )))

pipe_connector_m3_hole_1 = rotate([0, 0, 200])(translate([0, 4, 30])(cylinder(d = 3.5, h = 10)))
pipe_connector_m3_hole_2 = rotate([0, 0, -20])(translate([0, 4, 30])(cylinder(d = 3.5, h = 10)))

pipe_connector_m3_screw_hole_1 = rotate([0, 0, 200])(translate([0, 4, 23])(cylinder(d = screw_hole_diameter_3, h = 10)))
pipe_connector_m3_screw_hole_2 = rotate([0, 0, -20])(translate([0, 4, 23])(cylinder(d = screw_hole_diameter_3, h = 10)))


outside_holder = (
    cylinder(d = 22.4, h = 11.5)
    - translate([-13.15/2, -2.5/2, 0])(cube([13.15, 2.5, 11]))
    + translate([0, 0, 11.5])(cylinder(d = BEARING_SHAFT, h = 3.85))
    + translate([0, 0, 11.5 + 3.85])(cylinder(d = BEARING_SHAFT_COUPLER_DIAMETER, h = 17, segments = 4))
    - translate([9, -3/2.0, 11.5 + 3.85])(cube([3, 3, 40]))
    - rotate([0, 0, 90])(translate([9, -3/2.0, 11.5 + 3.85])(cube([3, 3, 40])))
    - rotate([0, 0, 180])(translate([9, -3/2.0, 11.5 + 3.85])(cube([3, 3, 40])))
    - rotate([0, 0, 270])(translate([9, -3/2.0, 11.5 + 3.85])(cube([3, 3, 40])))
    - translate([-5.5, 5.3, 11.5 + 3.85])(cube([3, 3, 40]))
    - translate([-8.5, 2.5, 11.5 + 3.85])(cube([3, 3, 40]))
    - translate([-7, 6.3, 11.5])((cube([3, 3, 40])))
    - translate([-9.1, 4.15, 11.5])((cube([3, 3, 40])))
    - wire_hole
    - m3_pipe_connector_space
    - pipe_connector_m3_screw_hole_1
    - pipe_connector_m3_screw_hole_2
)

pipe_connector = translate([0, 0, 12 + 3.5])(
    (cylinder(d = 22.4, h = 7.5))
    + translate([0, 0, 7.5])(cylinder(d = 34, h = 2))
    + translate([0, 0, 7.5])(cylinder(d = INNER_CYLINDER_DIAMETER, h = 14.5))
    - cylinder(d = BEARING_SHAFT_COUPLER_HOLE_DIAMETER, h = 18, segments = 4)
    - rotate([0, 0, 110])(translate([5, -3/2.0, 0])(cube([3, 3, 18])))
    - rotate([0, 0, 160])(translate([5, -3/2, 0])(cube([3, 3, 18])))
    - wire_hole

) - m3_pipe_connector - pipe_connector_m3_hole_1 - pipe_connector_m3_hole_2

hole_helper = rotate([0, 0, 45])(translate([0, 0, 22.5])(color('magenta')(
    cylinder(d = 36, h = 10))
) + translate([27, 0, 27.5])(rotate([0, -90, 0])(
        cylinder(d = 10, h = 55)
    )) - translate([0, 0, 22.5])(aluminum_pipe) - translate([50, 0, 27.5])(rotate([0, -90, 0])(
        cylinder(d = 3.5, h = 100)
    )))


motor_coupler_full = (
    cylinder(d = 11, h = 12)
    + translate([0, 0, 12])(motor_coupler)
    + translate([0, 0, 5.3])(rotate([0, 90, 0])(cylinder(d = 3, h = 60)))
    + translate([0, 0, 12])(cylinder(d = 4.5, h = 20))
)

motor = color('magenta')(
    cylinder(d = GEARBOX_DIAMETER, h = 30)
    + translate([0, 0, 30])(cylinder(d = GEARBOX_HOLE_DIAMETER, h = 2.6))
    + translate([0, 0, 30 + 2.6])(cylinder(d = 4, h = 9.6))
    + translate([0, 0, 30 + 2.7])(motor_coupler_full)
    + translate([0, 16.8/2, 30])(cylinder(d = 3.3, h = 2))
    + translate([0, 16.8/2, 32])(cylinder(d = 5.6, h = 15))
    + translate([0, -16.8/2, 30])(cylinder(d = 3.3, h = 2))
    + translate([0, -16.8/2, 32])(cylinder(d = 5.6, h = 15))
)

def motor_holder(use_placeholders = False):
    pipe_holes = translate([-30, 0, 21])(rotate([0, 90, 0])(cylinder(d = screw_hole_diameter_2_5, h = 60)))

    holder = (
      cylinder(d = INNER_CYLINDER_DIAMETER, h = 24)
      + translate([0, 0, 24])(cylinder(d = 24, h = 1.5))
      + translate([0, 0, 25.5])(cylinder(d = BEARING_SHAFT, h = 4.5))
      - translate([0, 0, 20])(cylinder(d = 12.5, h = 20))
      - pipe_holes
    ) - translate([0, 0, -12])(motor)

    if use_placeholders:
      return holder + pipe_holes
    else:
      return holder     

motor_holder_cutout = (
    cylinder(d = 80, h = 10)
    - cylinder(d = 25, h = 11)
)    

def motor_holder_cap():
    return translate([0, 0, 24.5])((roller_coupler.solid(17)
    - cylinder(d = 24, h = 8)
    - cylinder(d = BEARING_HOLE_DIAMETER, h = 4.3)
    - translate([0, 0, 9])(motor_coupler)
    - translate([0, 0, 7])(motor_coupler)
    - translate([0, 0, 12])(cylinder(d = 4.5, h = 20))
    #- translate([0, 0, 11])(motor_holder_cutout)
    + translate([0, 0, -10])(roller_coupler.extension(10))
    ))

hole_helper_motor = translate([0, 0, 117])(color('magenta')(
    cylinder(d = 36, h = 10))
) + translate([27, 0, 117 + 5])(rotate([0, -90, 0])(
        cylinder(d = 10, h = 55)
    )) - translate([0, 0, 22.5])(aluminum_pipe) - translate([50, 0, 117 + 5])(rotate([0, -90, 0])(
        cylinder(d = 2.6, h = 100)
    ))

pipe_cutting_helper = (
    cylinder(d = 34, h = 10)
    - translate([0, 0, -30])(aluminum_pipe)
    - translate([0, 0, -10])(cylinder(d = 30, h = 30))
)


#motor_outer_coupler = (
#    translate([0, 0, 12])(roller_coupler.full(8))
#    - motor_coupler_full
#    - translate([0, 0, 20])(cylinder(d = 100, h = 40))
#)

full = (aluminum_pipe - translate([-50, -50, -1])(cube([50, 100, 200]))
    + outside_holder
    + pipe_connector
    #+ bearing_holder_bottom
    #+ bearing_holder_top
    + translate([0, 0, 101])(motor_holder(False))
   # + hole_helper_motor
    #+ hole_helper
    - cube([50, 50, 200])
)

test_rig = (
    translate([-30/2, -15, 11.9])(cube([30, 100, 20]))
    - translate([0, 0, 0])(motor)
    #+ translate([0, 0, 0])(cylinder(d = 60, h = 5))
    - translate([0, 70, 0])(motor)
    #+ translate([0, 70, 0])(cylinder(d = 60, h = 5))
    + translate([-15, -15 + (100/2) - 20/2, -40])(cube([2, 20, 70]))
    + translate([-13, -13 + (100/2 -1), -38])(rotate([90, 0, 0])(linear_extrude(height= 2)(polygon([[0,0],[20,50], [0, 50]]))))
)

test_cylinder = (
    cylinder(h = 4, d1 = 60, d2 = 57)
    + translate([0, 0, 4])(cylinder(h = 4, d1 = 57, d2 = 60))
    - translate([0, 0, -45])(motor)
    - translate([20, 0, -1])(cylinder(d = 5, h = 10))
    - translate([30, 0, -1])(cylinder(d = 5, h = 10))
)

#full = test_rig
#full = test_cylinder
#full = m3_pipe_connector + m3_pipe_connector_space
#full = motor_holder(False)
#full = pipe_connector
#full = outside_holder
#full = bearing_holder_top
#full = bearing_holder_bottom
#full = (
#    motor_holder_cap() + motor_holder()
#    - cube([60, 60, 80])
#)
#full = motor_holder()
#full = motor_holder_cap()
#full = roller_coupler.full(20)
#full = roller_coupler.extension(10)
#full = motor_outer_coupler
#full = bearing_holder_both
#full = motor

#full = pipe_cutting_helper
#full = hole_helper_motor


if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
    file_out = os.path.join(out_dir, 'roller-blinds-motor.scad')

    a = full

    print("%(__file__)s: SCAD file written to: \n%(file_out)s" % vars())

    # Adding the file_header argument as shown allows you to change
    # the detail of arcs by changing the SEGMENTS variable.  This can
    # be expensive when making lots of small curves, but is otherwise
    # useful.
    scad_render_to_file(a, file_out, file_header='$fn = %s;' % SEGMENTS)