class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output = [0] * len(temperatures)

        for left in range(len(temperatures)):
            right = left

            for right in range(left, len(temperatures)):
                if temperatures[right] > temperatures[left]:
                    output[left] = right - left
                    break
                    print(output, left, right)

        return output
