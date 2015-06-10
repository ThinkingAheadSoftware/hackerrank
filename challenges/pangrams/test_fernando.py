from fernando import pangram

sentence_1 = "We promptly judged antique ivory buckles for the next prize"
print pangram(sentence_1)
assert(pangram(sentence_1) == "pangram")

sentence_2 = "We promptly judged antique ivory buckles for the prize"
print pangram(sentence_2)
assert(pangram(sentence_2) == "not pangram")
