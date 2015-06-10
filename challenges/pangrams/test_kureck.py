from kureck import pangram

sentence_1 = "We promptly judged antique ivory buckles for the next prize"
assert(pangram(sentence_1) == "pangram")

sentence_2 = "We promptly judged antique ivory buckles for the prize"
assert(pangram(sentence_2) == "not pangram")
