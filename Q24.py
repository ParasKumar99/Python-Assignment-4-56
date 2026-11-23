def vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in "aeiou":
            count += 1
    print("Vowels:", count)

vowels("Python Programming")