# Example trajectory

You can use these data to prototype analysis code. They were generated
by simulating the LJ fluid for 5 time units at dt=0.01, starting from
a spherical droplet with R=2.5.


## Trajectory file

The trajectory file `md_argon_R2.5.xyz` is in XYZ format, as described
in [project_2.pdf](../project_2.pdf).

To read the first frame and get the list of atoms and the initial
coordinates use the functions in [mdIO](../code/mdIO.py) (copy
`mdIO.py` into your working directory so that it can be imported):
```python
import mdIO
atoms, coordinates = mdIO.read_xyz_single("./md_argon_R2.5.xyz")

# number of atoms in the simulation
N = len(atoms)
```

To read *all* coordinates in a big numpy array:
```python
>>> import mdIO
>>> trajectory = mdIO.read_xyz("./md_argon_R2.5.xyz")
>>> print(trajectory.shape)
(250, 44, 3)
```

The first axis is the time, the second axis the particle, and the
third axis the XYZ coordinate of the particle.



## Energy file

The energy file `energy_argon_R2.5.dat` contains values of the
observables `["time", "E", "Tkin", "U", "T", "Ptot"]` in LJ units:
- time: time of the frame
- E: total energy
- Tkin: kinetic energy
- U: potential energy
- T: temperature
- Ptot: absolute value of the total linear momentum

It can be loaded as a large numpy array with
```python
>>> import numpy as np
>>> observables = np.loadtxt('energy_argon_R2.5.dat', unpack=True)
>>> print(observables.shape)
(6, 250)
```

With `unpack=True`, the array is transposed so that it becomes
convenient to access the columns. For example, to calculate the
average energy per particle, given `N` atoms:
```python
energy = observables[1]
e_avg_particle = energy.mean() / N
```




