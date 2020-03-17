#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
# Molecular Dynamics of the Lennard Jones Fluid
# Skeleton code --- incomplete.
#
# Written by Oliver Beckstein for ASU PHY494
# http://asu-compmethodsphysics-phy494.github.io/ASU-PHY494/
# Placed into the Public Domain

import time

import numpy as np

import mdIO
import mdInit



def initial_velocities(atoms, T0):
    """Generate initial velocities for *atoms*.

    - random velocities
    - total momentum zero
    - kinetic energy corresponds to temperature T0

    Parameters
    ----------
    atoms : list
         list of atom names, e.g. `['Ar', 'Ar', ...]`
    T0 : float
         initial temperature in K

    Returns
    -------
    velocities : array
         Returns velocities as `(N, 3)` array.
    """
    Natoms = len(atoms)
    v = mdInit.random_velocities(Natoms)
    v[:] = mdInit.remove_linear_momentum(v)
    return mdInit.rescale(v, T0)


def dynamics(atoms, x0, v0, dt, nsteps=100, filename="trajectory.xyz"):
    """Integrate equations of motions.

    Parameters
    ----------
     atoms : list
         list of atom names
     x0 : array
         Nx3 array containing the starting coordinates of the atoms.
         (Note that x0 is changed and at the end of the run will
         contain the last coordinates.)
     v0 : array
         Nx3 array containing the starting velocities, eg np.zeros((N,3))
         or velocities that generate a given temperature
     dt : float
         integration timestep
     nsteps : int, optional
         number of integrator time steps
     filename : string
         filename of trajectory output in xyz format

    Writes coordinates to file `filename`.
    """

    raise NotImplementedError


if __name__ == "__main__":
    # LJ setup module
    import system


    #------------------------------------------------------------
    # initialization
    #------------------------------------------------------------
    atoms, coordinates, box = system.generate_droplet(density,
                                                      R,
                                                      atomname=atom_name,
                                                      lattice="cubic")
    velocities = initial_velocities(atoms, initial_temperature)


    #------------------------------------------------------------
    # MD
    #------------------------------------------------------------
    results = dynamics(atoms, coordinates, velocities, dt,
                       nsteps=nsteps,
                       filename="trajectory.xyz")




