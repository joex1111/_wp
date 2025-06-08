def most_common(nums):
    if not nums:
        return None  # 空清單回傳 None

    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1

    max_count = max(counts.values())

    # 找出所有出現次數等於 max_count 的數字（如果有多個並列）
    most_frequents = [num for num, cnt in counts.items() if cnt == max_count]

    # 如果只想回傳其中一個，這裡回傳第一個
    return most_frequents[0]

# 範例測試
nums = [1, 3, 2, 3, 4, 1, 3, 2, 2, 2]
print(most_common(nums))  # 輸出：2
