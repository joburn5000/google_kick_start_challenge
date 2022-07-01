def has_2_vowel(s):
    vowel_count = 0
    for l in s:
        if l in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1
            if vowel_count > 2: return False
    return vowel_count > 1
def has_vowel(s):
    for l in s:
        if l in ['a', 'e', 'i', 'o', 'u']:
            return True
    return False
def is_spell(phrase):
    length = len(phrase)
    for i in range(length):
        for j in range(i,length+1)[::-1]:
            for size in range(1,int((j-i+1)/2)):
                first = phrase[i:i+size]
                middle = phrase[i+size:j-size]
                last = phrase[j-size:j]
                if not first == last: continue
                if not has_vowel(middle): continue
                if not has_2_vowel(first): continue
                return "Spell!"
    return "Nothing."

for i in range(1,int(input())+1):
    print("Case #" + str(i) + ": " + is_spell(input()))
