import sys

# convert a big-endian bytecode value to little endian, placing '\' between bytes to appease the wasm gods
def endian_swap_wasm(val, littleEndian=True):
  val = list(val)
  if len(val) % 2 != 0:
    return None

  if littleEndian:
    for i in range(0, len(val), 2):
      end = len(val)-(i+2)

      if i >= end:
        break

      tmp = val[i:i+2]
      val[i:i+2] = val[end:end+2]
      val[end:end+2] = tmp

  res = "" 
  for i in range(0, len(val), 2):
    res += "\\"+"".join(val[i:i+2])

  return res

print(endian_swap_wasm(sys.argv[1], len(sys.argv) > 2 and sys.argv[2] == 'littlendian'))
