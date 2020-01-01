import array
import os
import sqlite3
import zlib

DB_NAME = 'google-ctf-2019-hardware-minetest-map/map.sqlite'
MAP_DOWNLOAD_URL = 'https://capturetheflag.withgoogle.com/#challenges/hardware-minetest'
BLOCK_DIM = 16

def getBlockAsInteger(p):
    return int64(p[2]*16777216 + p[1]*4096 + p[0])

def int64(u):
    while u >= 2**63:
        u -= 2**64
    while u <= -2**63:
        u += 2**64
    return u

def getIntegerAsBlock(i):
    x = unsignedToSigned(i % 4096, 2048)
    i = int((i - x) / 4096)
    y = unsignedToSigned(i % 4096, 2048)
    i = int((i - y) / 4096)
    z = unsignedToSigned(i % 4096, 2048)
    return x,y,z

def unsignedToSigned(i, max_positive):
    if i < max_positive:
        return i
    else:
        return i - 2*max_positive

def getNodeAsInteger(p):
    return p[2]*BLOCK_DIM*BLOCK_DIM + p[1]*BLOCK_DIM + p[0]

def getIntegerAsNode(i):
    x = i % BLOCK_DIM
    i = int((i-x) / BLOCK_DIM)
    y = i % BLOCK_DIM
    i = int((i-x) / BLOCK_DIM)
    z = i % BLOCK_DIM
    i = int((i-x) / BLOCK_DIM)
    return x, y, z

def load_blocks():
    if os.path.isfile(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute('SELECT * FROM blocks')
        # print(c.fetchone()[1].decode('ascii'))
        return c.fetchall()
    else:
        print('couldn\'t find map file at ' + DB_NAME + '.')
        print('you can download the map at ' + MAP_DOWNLOAD_URL)
        return None

def parse_map(blocks):
    for block in blocks:
        pos = getIntegerAsBlock(block[0])
        block_data = zlib.decompress(block[1][6:])

        content_width = block[1][5]
        if content_width == 2:
            # then we parse the map

            pass
        else: 
            print('only map format versions 24 and greater are supported.')

def test_map_edit(blocks):
    test_node_locations = [
        (0, 0, 4), # should be stone
        (0, 1, 4), # should be insulated mesecons
    ]

    for block in blocks:
        if block[0] == getNodeAsInteger((0,0,0)):
            block_data = zlib.decompress(block[1][6:])

            node_params = [
                # my suspicion is that this first param is the type of block
                array.array('H', block_data[:8192]), 
                array.array('H', block_data[8192:12288]),
                array.array('H', block_data[12288:16384]),
            ]

            for test_node_loc in test_node_locations:
                print('node at location', test_node_loc)
                for param in node_params:
                    print ('param:', param[getNodeAsInteger(test_node_loc)])

            print('changing location', test_node_locations[0])
            # TODO: change location

            break

def main():
    print(array.typecodes)
    blocks = load_blocks()
    if blocks == None:
        return
    
    # parse_map(blocks)
    test_map_edit(blocks)
    # TODO: save edits

if __name__ == '__main__':
    main()
