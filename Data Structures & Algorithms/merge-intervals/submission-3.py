class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEndValue = output[-1][1]

            if start <= lastEndValue:
                output[-1][1] = max(lastEndValue, end)

            else:
                output.append([start, end])
        return output