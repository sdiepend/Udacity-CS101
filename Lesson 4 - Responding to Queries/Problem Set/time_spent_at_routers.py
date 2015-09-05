#How long does the data spend at the routers

# Information given in question

total_time = 75  # milliseconds traceroute, round trip Birmingham -> Sundsvall
one_way_distance = 2500. #km, Birmingham -> Sundsvall
optic_speed = 200000 # km/optic_speed
ms_per_second = 1000 # conversion from ms to seconds (ms/sec)

# Calculations
time_on_the_wires = (2*one_way_distance / optic_speed)*ms_per_second #km /

total_time_at_routers = total_time - time_on_the_wires
print total_time_at_routers