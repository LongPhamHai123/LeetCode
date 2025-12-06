def merge_intervals(intervals):
    if not intervals:
        return []
    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last_merged = merged[-1]
        if current[0] <= last_merged[1]:  # Overlap
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)
    return merged

if __name__ == "__main__":
    intervals = [[1, 3], [2, 4], [5, 7], [6, 8]]
    merged_intervals = merge_intervals(intervals)
    print("Merged Intervals:", merged_intervals)  # Output: [[1, 4], [5, 8]]