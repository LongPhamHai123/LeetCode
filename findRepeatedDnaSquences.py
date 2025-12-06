#leetcode-187
def findRepeatedDnaSequences(s: str) -> list[str]:
    seen, repeated = set(), set()
    for i in range(len(s) - 9):
        sequence = s[i:i + 10]
        if sequence in seen:
            repeated.add(sequence)
        else:
            seen.add(sequence)
    return list(repeated)