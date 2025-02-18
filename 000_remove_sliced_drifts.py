import xtrack as xt

env = xt.Environment.from_json('./pimm.json')
env.vars.load_json('./pimm_strengths.json')

line = env.ring

tt = line.get_table()

rr = env.new_builder(name='rr')

for nn in tt.name:
    if nn == '_end_point':
        continue
    if 'Drift' not in tt['element_type', nn]:
        rr.place(nn, at=tt['s_center', nn])

rr = rr.build()
del env.lines['ring']
env['ring'] = rr

env.to_json('./pimm_extr.json')
