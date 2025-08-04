'''Problem Description : I am provided a string S, There are two players, Player A has to make words starting from consonants, and Player B
                         has to make words starting from vowels, but have to use the letters from the provided string, The no. occurences
                         of the created words in the orignal string will equal to the points gained for each word. The game ends when both pl
                         ayers have made all possible words out of the given string.
                         
                         link : https://www.hackerrank.com/challenges/the-minion-game
                         
Approach : the first thing I will find all the possible combinations of the provided string, then I will filter them based on vowel or 
           consonant as the starting character, then I will iterate through each word into the string to find it's occurences.
           '''




from itertools import combinations

def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


s = input()
minion_game(s)

#Time Complexity : O(n)
#Space complexity : O(1)

