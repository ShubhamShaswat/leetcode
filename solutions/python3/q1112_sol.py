#created a base dictionary set to count frequency of the letter in the words
base_letters = {chr(i):0 for i in range(ord('a'),ord('z')+1)}
                                        

def wordsFormed(words,chars):

#intillizing result
                                        result = 0
                                        
#count the frequency of each charaters in chars
                                        for c in list(chars):
                                            base_letters[c] +=1 #
                                        
                                        for word in words:
                                            cnt = 0
                                            new_base_letters = base_letters.copy() #copy the dictionary
                                            print(new_base_letters)
                                            for ch in list(word):
                                                if new_base_letters[ch] >= 1:
                                                    new_base_letters[ch] -= 1 #derement the character count
                                                    cnt +=1
                                                else:
                                                    break #break out of the loop 
                                            print(cnt)
                                            if cnt == len(word):
                                                result += len(word)
                                        
                                        return result
                                            
                                        
                                        
                                        
                                        