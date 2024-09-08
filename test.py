print("hello")

"""
14
4
art ==> art
zone
zip
arts ==> arts
date
z
day
articles ==> articles
data
catch
zoom
article ==> article 
articulate ==> articulate
articulation ==> articulation
catc
art ==> art
da
z



catc:
catch (10)

art:
art (1)
arts (4)
articles (8)
article (12)
articulate (13)

da:
date (5)
day (7)
data (9)

z:
zone (2)
zip (3)
z (6)
zoom (11)
"""

def autocomplete():
    n = int(input()) #number of word
    m = int(input()) # wordd for process

    dictionary = []
    for term in range(n):
        dictionary.append(input().strip())



    prefixes = [] #words to check against dictionary
    for term in range(m):
        prefixes.append(input().strip())



    for prefix in prefixes: #find top 5 for each prefix
        suggestions = []
        for i, word in enumerate(dictionary):
            if word.startswith(prefix):
                suggestions.append((word, i+1)) #save the word and its rank
            if len(suggestions) == 5: #5 suggestion limit
                break

        if suggestions:
            for word, rank in suggestions:
                print(f"{word} {rank}")

        else: # assuming it's not populated
            print("not populated")
autocomplete()

"""
http://go.lyft.com/submit-solution
jcable@lyft.com"""
