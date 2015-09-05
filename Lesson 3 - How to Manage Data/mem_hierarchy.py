speed_of_light_mps = 299792458

lat_cpureg = 0.0000000004
lat_dram = 0.000000012
lat_hdd = 0.007

print speed_of_light_mps * lat_cpureg
print speed_of_light_mps * lat_dram
print (100. / 8800000000000) * 10 ** 9
print speed_of_light_mps * lat_hdd / 1000