import math

"""
def better_than_average(class_points, your_points):
    # Your code here

There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return True if you're better, else False!
Note:

Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!

average = (sum total of all the scores in the class(don't forget your own)) / (# of students (also don't forget your own)) 


"""

def better_than_average(class_points, your_points):
    total_points = sum(class_points)
    average_pts = (total_points + your_points) / (len(class_points) + 1)

    if average_pts < your_points:
        print("you are surrounded by the less competent. ", your_points, "is your score.  This is above the class average: ", average_pts)
        return True
    if average_pts > your_points:
        print("You are not even average! ", average_pts, "is the class averate ", your_points, "is your score.")
        return False

            
            
    


better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 8)