import sys

def endian_swap(val):
  val = list(val)
  if len(val) % 2 != 0:
    return None

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

print(endian_swap(sys.argv[1]))
