def insertInterval(intervals, newInterval):
    result = []
    inserted = False
    
    for current in intervals:
        # Trường hợp 1: current nằm trước newInterval
        if current[1] < newInterval[0]:
            result.append(current)
        
        # Trường hợp 2: current nằm sau newInterval
        elif current[0] > newInterval[1]:
            if not inserted:
                result.append(newInterval)
                inserted = True
            result.append(current)
        
        # Trường hợp 3: chồng lấn → gộp lại
        else:
            newInterval[0] = min(newInterval[0], current[0])
            newInterval[1] = max(newInterval[1], current[1])
    
    # Nếu newInterval chưa được thêm
    if not inserted:
        result.append(newInterval)
    
    return result

if __name__ == "__main__":
    intervals = [[1, 2], [5, 7]]
    newInterval = [3, 4]
    print("Updated Intervals:", insertInterval(intervals, newInterval))  # Output: [[1, 5], [6, 9]]