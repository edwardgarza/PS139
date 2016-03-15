import os
import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy.stats import chisquare


f = open(os.getcwd() + '/data/' + '2009FinalPlaces.txt')
lines = f.readlines()    

# counts saves the raw number and percs saves the percents for voter turnout 
# and the ballots for each of the candidates
counts, percs = [], []
ignore = 0
for line in lines:
    split = line.split()
    #print split
    if len(split) > 3 and split[-1][-1] in [str(i) for i in range(10)]:
        counts.append(split)
    if len(split) == 3 and split[-1][-1] in [str(i) for i in range(10)]:
        percs.append([float(x) for x in split])

percs = np.array(percs)
firstdig, seconddig, lastdig = [], [], [] 
firstDigObs = [0.0 for i in range(9)]
lastDigObs = [0.0 for i in range(10)]  
count = 0
for county in counts:
    for number in county:
        if number[0] not in [str(x) for x in range(10)] or number == '0':
            continue
        else:
            count += 1
            firstdig.append(int(number[0]))
            firstDigObs[int(number[0]) - 1] += 1
            lastdig.append(int(number[-1]))
            lastDigObs[int(number[-1]) - 1] += 1
            if len(number) > 1:
                seconddig.append(int(number[1]))

firstDigExp = count * np.array(([0.30103, 0.176091, 0.124939, 0.09691, 0.0791812, 0.0669468, 0.0579919, 0.0511525, 0.0457575]))
lastDigExp = count * np.array(([0.1 for i in range(10)]))

print lastDigObs
print chisquare(firstDigObs, f_exp=firstDigExp)
print chisquare(lastDigObs, f_exp=lastDigExp)


# Figures 1-3 pull from the entire data set instead of just the number of votes 
# for each of the candidates

# first digit of all the data
plt.figure(1)
plt.hist(firstdig, bins = 9, normed = True)
plt.xlabel('Digit')
plt.ylabel('Normalized Frequency')
plt.title('Frequency of first digit of all data')

# second digit of all the data
plt.figure(2)
plt.hist(seconddig, normed = True)
plt.xlabel('Digit')
plt.ylabel('Normalized Frequency')
plt.title('Frequency of second digit of all data')

# last digit of all the data
plt.figure(3)
plt.hist(lastdig, normed = True)
plt.xlabel('Digit')
plt.ylabel('Normalized Frequency')
plt.title('Frequency of last digit of all data')

traian = [float(x[-2]) for x in counts]
mircea = [float(x[-1]) for x in counts]
traianperc = np.array(traian)/(np.array(traian) + np.array(mircea))
mirceaperc = np.array(mircea)/(np.array(traian) + np.array(mircea))

#voterturnout = [int(x[-10]) /float(x[-11]) for x in counts[:-1] if x[-11] != '0']

# this figure shows the histogram of the leading digit for the number of votes
# cast for traian by district
plt.figure(4)
plt.hist([int(str(x)[0]) for x in traian if int(x) != 0], bins = 9, normed = True)
plt.xlabel('Digit')
plt.ylabel('Normalized Frequency')
plt.title('Frequency of first digit for vote counts for Traian by district')

# this figure shows the histogram of the leading digit for the number of votes
# cast for mircea by district
plt.figure(5)
plt.hist([int(str(x)[0]) for x in mircea if int(x) != 0], bins = 9, normed = True)
plt.xlabel('Digit')
plt.ylabel('Normalized Frequency')
plt.title('Frequency of first digit for vote counts for Mircea by district')

# this figure shows the histogram of the leading digit for the number of votes
# cast in total by district
plt.figure(6)
plt.hist([int(str(x[-11])[0]) for x in counts if int(x[-11]) != 0], bins = 9, normed = True)
plt.xlabel('Digit')
plt.ylabel('Normalized Frequency')
plt.title('Frequency of first digit for vote counts for all districts')

# this plot shows the histogram for the last digit of votes cast for traian by
# district
plt.figure(7)
plt.hist([int(str(int(x))[-1]) for x in traian], bins = 10, normed = True)
plt.xlabel('Digit')
plt.ylabel('Normalized Frequency')
plt.title('Frequency of last digit for vote counts for Traian by district')

# this shows the 2d plot of the voter turnout vs the votes for the winner
plt.figure(8)
plt.hexbin(percs[:,1], percs[:,0], gridsize=50)
plt.xlabel('Percent of voter for winner')
plt.ylabel('Voter turnout percent by district')
plt.title('Voter turnout vs Votes for winner')
plt.show()
