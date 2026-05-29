class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        l, r = 0, 0

        for t in temps:



        '''

        output = [0]*len(temperatures)

        for left in range(len(temperatures)):
            right = left

            for right in range(left, len(temperatures)):
                if temperatures[right] > temperatures[left]:
                    output[left] = right-left
                    break
                    print(output, left, right)

        return output