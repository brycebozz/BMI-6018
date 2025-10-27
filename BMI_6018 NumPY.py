import numpy as np
#1
print(np.__version__)
#2
problem_2 = np.array([0,1,2,3,4,5,6,7,8,9])
print(problem_2)


problem_3 = np.genfromtxt('bmi_6018numpy data.csv', delimiter=',', dtype=None) #put the data needed into git hub as bmi_6018 numpy data.csv converted website to csv with chrome's simple scraper extension.
fourth_column = np.array([column[3] for column in problem_3])
problem_4 = np.argmax(fourth_column > 1.0) +1 #add the 1 because python counts starting at 0.
print(f"the first value greater than 1 in the 4th column is {problem_4} and its value is {problem_3[problem_4][3]}")

np.random.seed(100)
a = np.random.uniform(1,50, 20)
print(a)
a[a >30] = 30
a[a<10] = 10
print(a)

