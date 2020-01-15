class Solution:

    #this class consist the solutions for Q-1112

    def __init__(self):
        #created a base dictionary set to count frequency of the letter in the words
        self.base_letters = {chr(i):0 for i in range(ord('a'),ord('z')+1)}


    def countCharacters(self,words,chars):

        #intillizing result
        result = 0

        #count the frequency of each charaters in chars
        for c in list(chars):
            self.base_letters[c] +=1

        for word in words:
            cnt = 0
            new_base_letters = self.base_letters.copy() #copy the dictionary
            for ch in list(word):
                if new_base_letters[ch] >= 1:
                    new_base_letters[ch] -= 1 #decrement the character count
                    cnt +=1
                else:
                    break #break out of the loop

            if cnt == len(word):
                result += len(word)

        return result
