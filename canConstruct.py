# leetcode - 377
from collections import Counter
def canConstruct(ransomNote: str, magazine: str) -> bool:   
    ransom_count = Counter(ransomNote)
    magazine_count = Counter(magazine)
    for char, count in ransom_count.items():
        if magazine_count[char] < count:
            return False
    return True
def canConStruct2(ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine):
        return False
    for char in set(ransomNote):
        if ransomNote.count(char) > magazine.count(char):
            return False
    return True
if __name__ == "__main__":
    ransomNote = "a"
    magazine = "b"
    print("Can construct:", canConstruct(ransomNote, magazine))  # Output: False