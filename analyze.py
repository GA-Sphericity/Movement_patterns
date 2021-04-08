from math import pi, sin, cos, sqrt
from random import shuffle
import turtle as t
import json

def diff(x, y, m):
    d = [ abs(x-y), abs(x+m-y), abs(y+m-x) ]
    return min(d)

def diff_to_deg(d, total):
    deg = round(d/total*180, 10)
    return deg

def dtg(x, y, m): #diff to deg shortened
    d = diff(x, y, m)
    deg = diff_to_deg(d, m)
    return deg

def dfs(a): #Difference For Sequence
    #returns the circular difference in degrees between every element in a sequence.
    b = [ dtg(a[i], a[i+1], len(a)) for i in range(len(a)-1) ]
    return b

def avg(a):
	return sum(a)/len(a)

def deltaavg(a):
    return avg(dfs(a))

def repetivitet_raw(a):
    diffs = {}
    for i in range(len(a)):
        for r in range(len(a)):
            if r+1 in diffs:
                if i + r + 1< len(a):
                    diffs[r+1].append( dtg(a[i], a[i+r+1], len(a)) )
            else:
                if i + r + 1< len(a):
                    diffs[r+1] = []
                    diffs[r+1].append( dtg(a[i], a[i+r+1], len(a)) )

    diffs_avg = {}
    for i in diffs:
        diffs_avg[i] = avg(diffs[i])

    return diffs_avg

def repetivitet(a):
    diffs_avg = repetivitet_raw(a)
    rep = {}
    for i in diffs_avg:
        rep[i] = (90-diffs_avg[i])/90

    return rep

def repetivitet_viktad(a):
    rep = repetivitet(a)
    rep_v = {}
    for i in rep:
        rep_v[i] = (rep[i] * (len(a)-i))/len(a)

    return rep_v

def sort_rep(rep):
    repsort = sorted(rep, key = lambda x : rep[x], reverse = True)
    return repsort

def rvs(a):
    return sort_rep(repetivitet_viktad(a))

def rs(a):
    return sort_rep(repetivitet(a))




    
    




    


