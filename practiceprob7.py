'''
Author: Abantika
Date: 07-07-2021
Purpose: Practice Problem
'''
def matchingWords(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score

if __name__ == '__main__':
    # matchingWords("This is good", "python is good")
    sentences = ["python is a good", "this is snake", "amaya is a good girl", "subscribe to code with amaya"]
    query = input("Please enter the query string: ")
    scores = [matchingWords(query, sentence) for sentence in sentences]
    # print(scores)
    sortedSentScore = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True)]
    # print(sortedSentScore)
    print(f"{len(sortedSentScore)} results found!")
    for score, item in sortedSentScore:
        print(f"\"{item}\": with a score of {score}")

