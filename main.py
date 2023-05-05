def capitalize_words(sentence):
    words = sentence.split()
    if len(words) >= 2:
        words[0] = words[0].capitalize()
        words[1] = words[1].lower()
    return ' '.join(words)

def main():
    sentence = "hello world"
    capitalized_sentence = capitalize_words(sentence)
    print(capitalized_sentence)

if __name__ == "__main__":
    main()

