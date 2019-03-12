# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
# Support function for molecular dynamics of the Lennard-Jones fluid
# Functions for setting up the system
#
# Written by Oliver Beckstein for ASU PHY494
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/
# Placed into the Public Domain.

# use LJ reduced units everywhere
#  m* = 1 (so v* = p*, and masses are not used explicitly anywhere)
#  T* = kT/eps

import numpy as np

# constants (note: our units for energy are LJ, i.e., eps)
# kBoltzmann = 1.3806488e-23   # J/K (but is 1 in LJ)

def random_velocities(N):
    """Takes a number of particles to create an array of random velocities"""
    return np.random.rand(N, 3) - 0.5

# note: PBC simulations Nf = 3N - 3  (translation)
#       droplet in vacuo: Nf = 3N - 6 (translation and rotation)
#       droplet with external spherical boundary potential: Nf = 3N-3 (rotation)


def kinetic_temperature(velocities):
    N = len(velocities)
    # sum_i vi**2 / 3N-6
    # For droplet in vacuo (incorrect for others)
    return np.sum(velocities**2)/(3*N-6)

def remove_linear_momentum(velocities):
    """Make total momentum 0:

    v[k]' = v[k] - sum_i m[i]*v[i] / m[k]
    """
    Pavg = np.mean(velocities, axis=0)
    vavg = Pavg   # same in LJ units
    return velocities - vavg

def total_momentum(velocities, masses):
    """Total linear momentum P = sum_i m[i]*v[i]"""
    # velocities = momentum in LJ units
    return np.sum(velocities, axis=0)

def rescale(velocities, temperature):
    """Rescale velocities so that they correspond to temperature T.

    T must be in LJ units!
    """
    current_temperature = kinetic_temperature(velocities)
    return np.sqrt(temperature/current_temperature) * velocities


