'''
Title:           Weather Prediction
Files:           p1_weather.py
Course:          CS540, Spring 2020

Author:          Yeochan Youn
Email:           yyoun5@wisc.edu
'''
import math

'''
get three data from data 1 and 2 to calculate euclidean distance between two data points

inputs: first data point, second data point
return: euclidean distance between two points 
'''
def euclidean_distance(data_point1, data_point2):
    a1 = data_point1.get('TMAX') # three data from data_point1
    b1 = data_point1.get('PRCP')
    c1 = data_point1.get('TMIN')

    a2 = data_point2.get('TMAX') # three data from data_point2
    b2 = data_point2.get('PRCP')
    c2 = data_point2.get('TMIN')

    return math.sqrt((a1 - a2)**2 + (b1 - b2) **2 + (c1 - c2)**2) # euclidean distance between two point

'''
read txt file to get dictionary form of data from each line
input: name of file to open
return: array of dictionary which defines date, tmax, prcp, tmin, and rain of each line
'''
def read_dataset(filename):
    fin = [] # final array to return
    dic = {} # dictionary to store data of each line
    ls = [] # array to get splited data on each line
    count = 0
    with open(filename, 'r') as f:
            for line in f:
                ls = line.split()
                dic["DATE"] = ls[0]
                dic['TMAX'] = float(ls[2])
                dic['PRCP'] = float(ls[1])
                dic['TMIN'] = float(ls[3])
                dic['RAIN'] = ls[4]
                fin.append(dic.copy())
    return fin

'''
get majority vote from nearest neighbors
input: number of nearest neighbors
return: majority vote of true and false
'''
def majority_vote(nearest_neighbors):
    count = 0
    for i in nearest_neighbors:
        if i.get('RAIN') == 'TRUE': # count increase by 1 for true
            count += 1
        elif i.get('RAIN') == 'FALSE': # count decrease by 1 for false
            count -= 1
    if count >= 0: # return true if count is 0 or positive number, return false otherwise 
        return 'TRUE'
    elif count < 0:
        return 'FALSE'

'''
esiamte it will rain or not at the test point
input: filename for opening file, test point to estimate, distance of nearest neighbors
return: true or false of rain possibility at the test point
'''
def k_nearest_neighbors(filename, test_point, k):
    dataset = read_dataset(filename)
    distance = []
    for i in dataset:
        dist = euclidean_distance(test_point, i) # get euclidean distance
        distance.append((i, dist)) # store each data with euclidean distance to compare
    distance.sort(key = lambda i:i[1]) # sort each data by euclidean distance
    fin = [] # array to store nearest neighbors
    for i in range(k): # run through k nearest data
        fin.append(distance[i][0]) # get data k nearest data and store in final array
    return majority_vote(fin) # return majority vote from final array
    

