def endian_swap(val):
  val = list(val)
  if len(val) % 2 != 0:
    return None

  for i in range(0, len(val), 2):
    end = len(val)-(i+2)

    if i >= end:
      return "".join(val)

    tmp = val[i:i+2]
    val[i:i+2] = val[end:end+2]
    val[end:end+2] = tmp

if __name__ == "__main__":
  assert endian_swap("1234") == "3412"
  assert endian_swap("123") == None
