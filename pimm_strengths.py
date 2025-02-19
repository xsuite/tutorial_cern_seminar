import xtrack as xt

env = xt.get_environment()

# Quadrupole circuits
env["kqfa"] = 0.3370599717739164
env["kqfb"] = 0.5462953319567254
env["kqd"] =  -0.5876756866270778

# Sextupole circuits
env["ksf"] =  0.5853219204643684
env["ksd"] =  -0.7811929408248136

# Extraction_knob
env["on_extr"] = 0.0
env["kse_ref"] = 5.68732
env["kse"] = 'on_extr * kse_ref'
