import xtrack as xt
import numpy as np

env = xt.get_environment()
env.vars.default_to_zero = True

# Element geometry
n_bends = 16
env['ang_mb'] = 2*np.pi/n_bends
env['l_mb'] = 1.65
env['l_mq'] = 0.35

env.new('mb', xt.RBend,      length='l_mb', angle='ang_mb', k0_from_h=True)
env.new('mq', xt.Quadrupole, length='l_mq')

# Quadrupole families
env.new('qfa', 'mq', k1= 'kqfa')
env.new('qfb', 'mq', k1= 'kqfb')
env.new('qd',  'mq', k1= 'kqd')

# Lattice
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

long_straight = env.new_line(length=2., components=[
    env.new('mid.lss', xt.Marker, at=1.)
])
short_straight = env.new_line(length=1., components=[
    env.new('mid.sss', xt.Marker, at=1.)
])

arc = cell_a + cell_b

ring = (long_straight
             + arc
             + short_straight
             - arc
            )
env['ring'] = ring


