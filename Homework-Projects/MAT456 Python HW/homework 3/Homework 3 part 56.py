#Homework 3 part 5-6 Nicholas Wilk
import csv
import numpy as np
import matplotlib.pyplot as plt

def main():
      with open('Lehman_collisions.csv', 'rb') as f:
        reader = csv.DictReader(f)
        month = [row['DATE'] for row in reader]
        monthCount = {}
        f.close()
        

        for dateString in month:
            date = int(dateString[:2])
            monthCount[date] = monthCount.get(date,0)+1

        print monthCount

        #Makea a histogram of the maximum temps:
        plt.bar(monthCount.keys(), monthCount.values(), align='center')
        plt.title("Distribution of Accidents in 10468 zipcode by Month")
        plt.xlabel("Month of Accident Occurence")
        plt.ylabel("Number of Accidents")
        plt.xticks(monthCount.keys())
        plt.axis([0,13,200,400])
 #       plt.yticks(np.arange(0, 50, 5))
        plt.show()
    
main()
