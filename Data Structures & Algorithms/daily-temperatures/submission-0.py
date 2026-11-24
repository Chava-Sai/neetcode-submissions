class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        final = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:

                prev_index = stack.pop()

                final[prev_index] = i - prev_index

            stack.append(i)

        return final









        