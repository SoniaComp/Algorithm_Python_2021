def solution(board, moves):
  stacklist = []
  answer = 0

  for i in moves:
    for j in range(len(board)):
      if board[j][i-1] != 0:
        stacklist.append(board[j][i-1])
        # 먼저 스택에 넣고 비교한다.
        board[j][i-1] = 0
        
        if len(stacklist) > 1:
          if stacklist[-1] == stacklist[-2]:
            stacklist.pop(-1)
            stacklist.pop(-1)
            answer += 2
        break
  return answer
