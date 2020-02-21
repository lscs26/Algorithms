#!/usr/bin/python

import sys
from random import randint


rock = ["rock"]
paper = ["paper"]
scissors = ["scissors"]
rps = [rock,paper,scissors]
available_options = ['rock', 'paper', 'scissors']

def rock_paper_scissors(n):
    if n==0:
        return [[]]
    if n==1:
        return rps
    return rps_helper(n,rock)+rps_helper(n,paper)+rps_helper(n,scissors)

def rps_helper(n,list):
    if n ==1:
        return list
    if n ==2:
        l1=list.copy()
        l2=list.copy()
        l3=list.copy()
        l1.extend(rock)
        l2.extend(paper)
        l3.extend(scissors)
        n-=1
        return [rps_helper(n,l1), rps_helper(n,l2), rps_helper(n,l3)]
    else:
        l1=list.copy()
        l2=list.copy()
        l3=list.copy()
        l1.extend(rock)
        l2.extend(paper)
        l3.extend(scissors)
        n-=1
        return rps_helper(n,l1), rps_helper(n,l2), rps_helper(n,l3)
        
print(rock_paper_scissors(3))



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')