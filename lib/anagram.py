class Anagram:
    def __init__(self,word):
        self.word = word

    def match(self, word_list):
        sorted_word = sorted([letter for letter in self.word])
        # matches = []
        # for w in word_list:
        #     sorted_w = sorted([letter for letter in w])
        #     if sorted_word == sorted_w:
        #         matches.append(w)
        # return matches
        return [w for w in word_list if sorted([letter for letter in w]) == sorted_word]