'''
def checknode(v):
  if promising(v):
    if there is a solution at v:
      write the solution
    else:
      for u in each child of v:
        checknode(u)
'''

'''
부분집합의 상태 공간트리
a[0...n-1]: 집합에 대한 비트 표현 저장, 크기는 원소의 수
k: 선택한 횟수(현재 노드의 높이)
n: 모든 선택수(트리의 높이)

def subset(a, k, n):
  if k==n: # 단말 노드에 도달
    process_solution(a, n)
  else:
    a[k] = 0 # 포함하지 않는 경우
    subset(a, k+1, n)

    k: 지금까지 한 선택
    n: 총 선택 수
    a[k] = 1 # 포함하는 경우
    subset(a, k+1, n)

'''

'''
순열
order[]: 순열의 순서를 저장

def permutation(order, k, n):
  if k == n:
    print_order_array(order, n)
  else:
    check = [False] * n -> 어떤 선택 조사
    for i in range(k): -> k 개 만큼 선택
      check[order[i]] = True
    for i in range(n): -> 원소의 수만큼 조사
      if check[i] == False: -> i가 아직 선택되지 않았을 경우
        order[k] = i
        permutation(order, k+1, n)
'''