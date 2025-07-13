'''Problem Description : I am hotel manager, my task is to find captain's room .There are a group of families each with n members, 
                         each family is alloted one room, I have an unordered list of room alloted to each member of each group, and the 
                         captain's room is also one among them, I need to find that:
                         e.g  : rooms : [12,13,12,13,12,13,24,45,45,45]  O/p : Captain's room : 24
                         Link : https://www.hackerrank.com/challenges/py-the-captains-room
                         
Approach : I am planning to create a set of the list, to eliminate duplicates and then apply a for loop in list
           and apply the formula total2 =  family_size * i, for each i in set, and also calculate the total from list,
           using sum(list), and then apply captain = (total2 - total)//(family_size-1). '''

family_size = int(input())
rooms = list(map(int, input().split()))
total = sum(rooms)
distinct_rooms = set(rooms)
total2 = 0
for i in distinct_rooms:
    total2 += family_size*i
captain = (total2 - total)//(family_size-1)

print(captain)

#Time complexity : O(n)
#Space Complexity : O(n)
