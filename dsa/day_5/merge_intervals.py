def merge_intervals(intervals):
    output = [intervals[0]]
    for i in range(1,len(intervals)):
        if intervals[i][0] <= output[-1][1]:
            output[-1][1] = max(intervals[i][1], output[-1][1])
        else:
            output.append(intervals[i])
    return output


tests = [[[1,3],[2,6],[8,10],[15,18]], [[1,4],[4,5]], [[4,7],[1,4]], [[1,4],[2,3]], [[1,2]]]
for t in tests:
    print(t, merge_intervals(t))
        