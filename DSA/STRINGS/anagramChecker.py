
s1 = "Silent"
s2 = "Listen"

s1_arr = list(s1.lower())
s1_arr.sort()
s2_arr = list(s2.lower())
sorted_s2 = s2_arr.sort()

if s1_arr == s2_arr:
    print("The strings are anagrams.")