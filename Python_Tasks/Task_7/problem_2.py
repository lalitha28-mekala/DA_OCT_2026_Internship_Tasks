# Q2 The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem

K=int(input())
rooms= list(map(int,input().split()))
unique_sum=sum(set(rooms))
total_sum= sum(rooms)
captain = (unique_sum*K - total_sum)//(K-1)
print(captain)
