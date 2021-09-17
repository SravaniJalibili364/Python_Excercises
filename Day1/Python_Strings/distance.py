'''Write a program to compute the distance between the points (x1, y1) and (x2, y2)'''

#defininf the function to calculate distance between two points
def distance(source_point,destination_point):
    #using abs function we can get absolute value
    print(abs(source_point-destination_point))



source_point = int(input())
destination_point = int(input())
distance(source_point,destination_point)