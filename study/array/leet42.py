class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0
        
        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다.
                top = stack.pop()
                
                if not len(stack):
                    break
                
                # 이전과의 높이 만큼 물처리ㅣ
                distance = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]]) - height[top]
                
                volume += distance * waters
                
            stack.append(i)
        return volume
                