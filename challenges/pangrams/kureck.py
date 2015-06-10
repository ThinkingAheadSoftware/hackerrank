def pangram(sentence):
    new_sentence = sentence.replace(" ", '').lower()
    return "pangram" if len(set(new_sentence)) == 26 else "not pangram"


def run():
    sentence = raw_input()
    print pangram(sentence)

if __name__ == "__main__":
    run()
