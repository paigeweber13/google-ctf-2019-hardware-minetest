#include <cstdint>
#include <vector>

using namespace std;

/*
 * from https://github.com/minetest/minetest/blob/master/doc/world_format.txt
 * 
 * The key
 * --------
 * "pos" is created from the three coordinates of a MapBlock using this
 * algorithm, defined here in Python:
 * 
 *   def getBlockAsInteger(p):
 *       return int64(p[2]*16777216 + p[1]*4096 + p[0])
 * 
 *   def int64(u):
 *       while u >= 2**63:
 *           u -= 2**64
 *       while u <= -2**63:
 *           u += 2**64
 *       return u
 * 
 * It can be converted the other way by using this code:
 * 
 *   def getIntegerAsBlock(i):
 *       x = unsignedToSigned(i % 4096, 2048)
 *       i = int((i - x) / 4096)
 *       y = unsignedToSigned(i % 4096, 2048)
 *       i = int((i - y) / 4096)
 *       z = unsignedToSigned(i % 4096, 2048)
 *       return x,y,z
 * 
 *   def unsignedToSigned(i, max_positive):
 *       if i < max_positive:
 *           return i
 *       else:
 *           return i - 2*max_positive
 */

uint64_t getBlockAsInteger(vector<uint64_t> p){
  return uint64_t(p[2]*16777216 + p[1]*4096 + p[0]);
}

vector<uint64_t> getIntegerAsBlock(uint64_t i){
  uint64_t x, y, z;
  x = unsignedToSigned(i % 4096, 2048);
  i = int((i - x) / 4096);
  y = unsignedToSigned(i % 4096, 2048);
  i = int((i - y) / 4096);
  z = unsignedToSigned(i % 4096, 2048);
  return vector<uint64_t>({x,y,z});
}

int64_t unsignedToSigned(uint64_t i, uint64_t max_positive){
  if (i < max_positive){
    return i;
  }
  else {
    return i - 2*max_positive;
  }
}
