
import adi

# Set up AD5770r
myad5770r = adi.ad5770r(uri="ip:analog.local")

for ch in myad5770r.channel:
    print("Channel Name: ", ch.name)

    raw_val = ch.raw
    print("\traw: {}".format(raw_val))

    scale_val = ch.scale
    print("\tscale: {}".format(scale_val))

    low_pass_filter_val = ch.filter_low_pass_3db_frequency
    print("\tfilter_low_pass_3db_frequency: {}".format(low_pass_filter_val))

    low_pass_filter_avail_val = ch.filter_low_pass_3db_frequency_available
    print("\tfilter_low_pass_3db_frequency_available: {}".format(low_pass_filter_avail_val))

    offset_val = ch.offset
    print("\toffset: {}".format(offset_val))

    powerdown_val = ch.powerdown
    print("\tpowerdown: {}".format(powerdown_val))






