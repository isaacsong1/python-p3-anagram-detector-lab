# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, anagram_list):
        match_list = []
        for word in anagram_list:
            count = 0
            for letter in self.word:
                if letter in word:
                    count += 1
                else:
                    continue
            if count == len(self.word) == len(word):
                match_list.append(word)
        return match_list if len(match_list) else []

listen = Anagram("Word")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))