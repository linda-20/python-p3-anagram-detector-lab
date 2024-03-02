# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        
        matches = []

        
        for anagram in possible_anagrams:
            
            anagram_lower = anagram.lower()

            
            if anagram_lower != self.word:
            
                if sorted(anagram_lower) == sorted(self.word):
                    
                    matches.append(anagram)

        
        return matches
