'''
This script is used to read in the binary data
into a human readable csv file
'''

import struct as struct
import glob as glob 

_LORA_PKG_FORMAT = "!BILLHHBBHbbb"
data_size = struct.calcsize(_LORA_PKG_FORMAT)

fname_list = glob.glob('./AF_Data/data*.dat')

for fname_in in fname_list:

    fname_out = fname_in.split('.dat')[0] + '.csv'

    out_str = 'device_id,sequence,sensing_time,tick_diff,small,large,temperature,humidity,noise,c1,c2,c3\n'

    pkg = 1
    with open(fname_in, 'rb') as fin:
        pkg = fin.read(data_size)

        while len(pkg) == 24:


            out_tuple = struct.unpack(_LORA_PKG_FORMAT, pkg)
            out_list = list(out_tuple)

            out_str += ','.join(['%d' % item for item in out_list]) + '\n'
            # print out_str
            pkg = fin.read(data_size)

    with open(fname_out, 'w') as fout:
        fout.write(out_str)
