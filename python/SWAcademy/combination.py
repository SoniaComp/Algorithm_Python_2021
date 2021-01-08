@profile
def solution():
  # x, y, z = 100
  count = 0
  for x in range(1, 100):
    for y in range(1, 100):
      if x + y >= 100:
        break
      for z in range(1, 100):
        if x+y+z == 100:
          count += 1
          print(f'({x}, {y}, {z})')
        if x+y+z > 100:
          break
  print(count)

if __name__ == '__main__':
    solution()

# 전사함수 개수 찾기
# Y의 사이빈틈을 기준으로 찾으면 된다.
# m -> n 전사함수