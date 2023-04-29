#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys

from solid import *
from solid.utils import *

SEGMENTS = 200

INNER_CYLINDER_DIAMETER = 29
OUTER_PIPE_HOLE_DIAMETER = 32.3
BEARING_SHAFT = 19.9
BEARING_HOLE_DIAMETER = 27.25

INNER_BLIND_ROLLER_DIAMETER = 40.75

ridge_subtractor = (
  translate([-1.5/2, INNER_BLIND_ROLLER_DIAMETER/2.0 - 3, 0])(cube([1.7, 30, 100]))
  + translate([0, 18.9, 0])(rotate([0, 0, 45])(cube([3, 3, 100])))
)

ridges = (
    rotate([0, 0, 12])(ridge_subtractor)
    + rotate([0, 0, -12])(ridge_subtractor)
    + rotate([0, 0, 60])(ridge_subtractor)
    + rotate([0, 0, 120])(ridge_subtractor)
    + rotate([0, 0, -60])(ridge_subtractor)
    + rotate([0, 0, -120])(ridge_subtractor)
    + translate([-8/2, -23, 0])(cube([8, 5, 40]))     
  )

def solid(height):
  return (
    cylinder(d = INNER_BLIND_ROLLER_DIAMETER, h = height)
#    + translate([0, 0, height])(cylinder(d = INNER_BLIND_ROLLER_DIAMETER, h = 10))
#    - translate([0, 0, height])(cylinder(d = INNER_BLIND_ROLLER_DIAMETER - 4, h = 11))
    - ridges
  )

def extension(height):
  return (
    cylinder(d = INNER_BLIND_ROLLER_DIAMETER, h = height)
    - cylinder(d = INNER_BLIND_ROLLER_DIAMETER - 4, h = 11)
    - ridges 
  )  

def full(height):
  return (
    solid(height)
    + translate([0, 0, height])(extension(11))
  )