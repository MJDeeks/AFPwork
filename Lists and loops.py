words = []
sentence = input('Enter a sentence')
words = sentence.split(' ')
print(words)

points = []
gamepoints = input('Enter the points for each game played')
points = gamepoints.split(',')
print(points)

total = 0
for x in points:
    total += int(x)
    print(total)
