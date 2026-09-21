# Xsuite tutorial (seminar)

This folder contains a small, self-contained set of Jupyter notebooks used for an Xsuite tutorial.
The examples are based on the PIMM lattice (proton and ion therapy synchrotron, [CERN/PS 99-010](https://cds.cern.ch/record/385378/)).

## Notebooks

The notebooks are meant to be run in order:

- `notebook_00_environment.ipynb` – the Xtrack environment: variables, deferred expressions, elements and lines
- `notebook_01_lattice_design.ipynb` – building the PIMM lattice (cells, arcs, ring, sextupoles, RF) and saving it to `pimm.json`
- `notebook_02_load_lattices.ipynb` – loading lattices from Python, JSON and MAD-X files, loading optics/strength files
- `notebook_03_optics_matching.ipynb` – twiss, tune/dispersion matching, chromaticity correction, saving strengths to `pimm_strengths.json`
- `notebook_04_tracking.ipynb` – tracking with turn-by-turn monitor: phase space close to the 3rd order resonance (slow extraction)
- `notebook_05_rf_wakefield_beamstatsmon.ipynb` – RF and longitudinal phase space, transverse wakefield, beam statistics monitor

## Data files

- `pimm_seq.py`, `pimm.json`, `PIMM.seq` – the PIMM lattice as Python script, Xsuite JSON and MAD-X sequence
- `pimm_extr.json` – PIMM lattice used in the tracking example
- `pimm_strengths.json`, `example_strengths.json`, `example_strengths.madx` – optics/strength files

## Running

Requires `xtrack`, `xpart`, `xwakes`, `matplotlib` and Jupyter. From this directory:

```bash
jupyter notebook
```
