class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            results= []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results
        # 문자열 형태이더라도 숫자가 저장된 num의 경우에는 isdigit에서 True값이 리턴되었고
        if input.isdigit():
            return [int(input)]
        
        results = []
        for index, value in enumerate(input):
            if value in "-+*":
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index+1:])
                
                results.extend(compute(left, right, value))
        
        return results