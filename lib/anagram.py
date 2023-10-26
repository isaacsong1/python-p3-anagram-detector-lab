# your code goes here!
class Anagram:
    def __init__(self, word):
        # self.word = word
        self.word_letters = sorted([letter for letter in word])

    def match(self, anagram_list):
        # messy My attempt
        # match_list = []
        # for word in anagram_list:
        #     count = 0
        #     for letter in self.word:
        #         if letter in word:
        #             count += 1
        #         else:
        #             continue
        #     if count == len(self.word) == len(word):
        #         match_list.append(word)
        # return match_list if len(match_list) else []

        # Solution
        match_word_list = []

        for word in anagram_list:
            if sorted([letter for letter in word]) == self.word_letters:
                match_word_list.append(word)

        return match_word_list


listen = Anagram("Word")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))