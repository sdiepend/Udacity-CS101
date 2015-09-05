# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

# print 2 ** 10      # one kilobit, kb
# print 2 ** 10 * 8  # one kilobyte, kB

# print 2 ** 20      # one megabit, Mb
# print 2 ** 20 * 8  # one megabyte, MB

# print 2 ** 30      # one gigabit, Gb
# print 2 ** 30 * 8  # one gigabyte, GB

# print 2 ** 40      # one terabit, Tb
# print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).
def convert_seconds(n):
    """
    Convert a number(in seconds) into hours, minutes and seconds.
    """

    # The strings that are represented in the output
    str_hours = " hours"
    str_min = " minutes"
    str_sec = " seconds"

    hour, rest = n / 3600, n % 3600
    hour = int(hour)
    if hour == 1:
        str_hours = " hour"

    minute = rest / 60
    minute = int(minute)
    if minute == 1:
        str_min = " minute"

    sec = rest % 60.
    if sec == 1:
        str_sec = " second"

    return str(hour) + str_hours + ", " + str(minute) + str_min + ", " + str(sec) + str_sec

def download_time(file_size, f_unit, bandwith, b_unit):
    #I'm using the position of a unit in the list as the power of 1024. This way I avoid implementing multiple if-structures.
    units = ["k", "M", "G", "T", "Y", "Z"]
    f_size_kb = file_size * 1024. ** (units.index(f_unit[0]))

    # if the size is in Bytes multiply by 8
    if f_unit[1] == "B":
        f_size_kb = f_size_kb * 8
    # print f_size_kb

    # if the bandwith is in Bytes multiply by 8
    b_kb = bandwith * 1024 ** (units.index(b_unit[0]))
    if b_unit[1] == "B":
        b_kb = b_kb * 8
    # print b_kb 
    
    total_seconds = f_size_kb / b_kb
    return convert_seconds(total_seconds)


print download_time(1024,'kB', 1, 'MB')
# #>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
# #>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
# #>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
# #>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
# #>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB', 5, 'MB')

