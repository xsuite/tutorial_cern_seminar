import xtrack as xt
import numpy as np

env = xt.Environment()
env.particle_ref = xt.Particles(kinetic_energy0=200e6)
env.vars.default_to_zero = True

############
# Elements #
############

# Element geometry
n_bends = 16
env['ang_mb'] = 2*np.pi/n_bends
env['l_mb'] = 1.65
env['l_mq'] = 0.35

# Magnet types
env.new('mb', xt.RBend,      length='l_mb', angle='ang_mb', k0_from_h=True)
env.new('mq', xt.Quadrupole, length='l_mq')
env.new('ms', xt.Sextupole, length=0.2)

# Quadrupole families
env.new('qfa', 'mq', k1= 'kqfa')
env.new('qfb', 'mq', k1= 'kqfb')
env.new('qd',  'mq', k1= 'kqd')

# Magnet instances
env.new('msf.1', 'ms', k2='ksf')
env.new('msf.2', 'ms', k2='ksf')
env.new('msd.1', 'ms', k2='ksd')
env.new('msd.2', 'ms', k2='ksd')
env.new('mse',   'ms', k2='kse')

# RF cavity
env.new('rf1', xt.Cavity, voltage='vrf', frequency='frf')

###########
# Lattice #
###########

# Cells
cell_a = env.new_line(length=7.405, components=[
    env.place('qfa', at=0.3875),
    env.place('mb', at=1.8125),
    env.place('qd', at=3.2925),
    env.place('mb', at=5.0475),
    env.place('qfa', at=6.3275),
])

cell_b = env.new_line(name='cell_b', length=8.405, components=[
    env.place('qfb', at=1.2725),
    env.place('mb', at= 2.7275),
    env.place('qd', at=4.8575),
    env.place('mb', at=6.5125),
    env.place('qfb', at=7.7925),
])

# Arc
arc = cell_a + cell_b

# Straight sections
long_straight = env.new_line(length=2., components=[
    env.new('mid.lss', xt.Marker, at=1.)
])
short_straight = env.new_line(length=1., components=[
    env.new('mid.sss', xt.Marker, at=1.)
])

# Ring
ring = 2 * (long_straight
             + arc
             + short_straight
             - arc # mirror symmetric lattice
            )

# Assign unique names to all elements
ring.replace_all_repeated_elements()

# Insert sextupoles
ring.insert([
    env.place('msf.1', at=-0.2, from_='qfb.0@start'),
    env.place('msf.2', at=-0.2, from_='qfb.4@start'),
    env.place('msd.1', at=0.3,  from_='qd.2@end'),
    env.place('msd.2', at=0.3,  from_='qd.6@end'),
    env.place('mse',   at=-0.3, from_='qfa.4@start')
])

# Insert RF
ring.insert('rf1', at=0.5, from_='qfa.3@start')

env.vars.default_to_zero = False
