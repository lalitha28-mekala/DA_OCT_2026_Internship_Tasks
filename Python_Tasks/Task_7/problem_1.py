# Q1 Set .symmetric_difference() Operation
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

E=int(input())
lst_E = set(map(int,input().split()))
F=int(input())
lst_F = set(map(int,input().split()))
print(len(lst_E.symmetric_difference(lst_F)))
