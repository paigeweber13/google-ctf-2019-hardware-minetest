import sqlite3

DB_NAME = 'google-ctf-2019-hardware-minetest-map/map.sqlite'

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

def load_blocks():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM blocks')
    # print(c.fetchone()[1].decode('ascii'))
    return c.fetchall()

def main():
    blocks = load_blocks()
    first_block = blocks[0]
    print('pos:', getIntegerAsBlock(first_block[0]))
    print('block data:', first_block[1])

if __name__ == '__main__':
    main()
