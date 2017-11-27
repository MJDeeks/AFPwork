print('Rainfall data')
print('--------------------------------')
rainFall = []
monthlyFall = input('write monthly rainfall')
rainFall = monthlyFall.split(',')

for i in range(len(rainFall)):
    rainFall[i] = int(rainFall[i])

total = 0
for x in rainFall:
    total += x

maxFall = max(rainFall)
minFall = min(rainFall)
averageFall = total/len(rainFall)

print('highest rainfall was {0} \n'
      'lowest rainfall was {1} \n'
      'average rainfall was {2}'.format(maxFall, minFall, averageFall))