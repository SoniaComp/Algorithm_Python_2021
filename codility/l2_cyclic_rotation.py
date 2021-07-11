def solution(A, K):
  if len(A) == 0: # 예외 처리
    return A
  K = K % len(A)
  return A[-K:] + A[:-K]