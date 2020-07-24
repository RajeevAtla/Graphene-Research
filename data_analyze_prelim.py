#Import pandas and numpy
import pandas as pd
import numpy as np

import data_import

#Import data
exec(open('data_import.py').read())
#print(data) #for a sanity check

#Name and store all the columns; print for sanity check
numElements = data["number_of_elements"]
#print(numElements) #for a sanity check

atomicMass = data["mean_atomic_mass"]
atomicRadius = data["mean_atomic_radius"]
fie = data["mean_fie"]
density = data["mean_Density"]
electronAffinity = data["mean_ElectronAffinity"]
fusionHeat = data["mean_FusionHeat"]
thermalConductivity = data["mean_ThermalConductivity"]
valence = data["mean_Valence"]
criticalTemp = data["critical_temp"]
superconType = data["Superconductivity Type"]
