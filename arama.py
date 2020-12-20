import ahocorasick

with open("corpus.txt") as corpus:
    auto = ahocorasick.Automaton()
    for word in corpus:
        word = word.rstrip('\n')
        auto.add_word(word, word)
    auto.make_automaton()

with open("PAROLA_VERISI.txt") as wordlist:
    for no, line in enumerate(wordlist):
        for end_ind, found in auto.iter(line ):
            print(found,line)