# @static method 데코레이터
# 인스턴스를 통하지 않고 클래스에서 바로 호출할 수 있는 정적 메서드와 클래스 메서드에 대해 알아보겠습니다.

# 배열은 깔끔하게 구현할 수 있기 때문에, 연결 리스트 때처럼 포인터를 맨 앞으로 돌릴지 비교하는 등의 최적화는 수행할 필요가 없다.
# 아울러 정렬된 리스트 변수를 별도로 선언했던것과 달리 원래 삽입 정렬을 배열로 구현하게 되면, 이처럼 제자리 정려링 가능하여 공간 복잡도를 수행할 수 있다.

class Solution:
    # 문제에 적합한 비교함수
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    # 삽입정렬 구현
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j-1], nums[j]):
                nums[j], nums[j-1] = nums[j-1], nums[j]
            i += 1

        return str(int(''.join(map(str, nums))))
