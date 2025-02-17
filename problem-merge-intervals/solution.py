def merge(intervals):
  if not intervals:
    return []

  intervals.sort(key=lambda x: x[0])

  merged = [intervals[0]]

  for i in range(1, len(intervals)):
    prev_start, prev_end = merged[-1]
    curr_start, curr_end = intervals[i]

    if curr_start <= prev_end:
      merged[-1][1] = max(prev_end, curr_end)
    else:
      merged.append(intervals[i])

  return merged

if __name__ == '__main__':
  intervals = [[1,3],[2,6],[8,10],[15,18]]
  print(merge(intervals))