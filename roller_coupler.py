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

ridge_subtractor = translate([-1.5/2, 40.9/2.0 - 3, 0])(cube([1.5, 30, 30]))

def full(height):
  return (
    cylinder(d = 40.9, h = height)
    - rotate([0, 0, 12])(ridge_subtractor)
    - rotate([0, 0, -12])(ridge_subtractor)
    - rotate([0, 0, 60])(ridge_subtractor)
    - rotate([0, 0, 120])(ridge_subtractor)
    - rotate([0, 0, -60])(ridge_subtractor)
    - rotate([0, 0, -120])(ridge_subtractor)
    - translate([-8/2, -23.4, 0])(cube([8, 5, 10])) 
  )