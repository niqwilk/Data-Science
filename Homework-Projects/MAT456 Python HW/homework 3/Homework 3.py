#Homework 3 Nicholas Wilk
import csv
import numpy as np
import matplotlib.pyplot as plt

def main():
      with open('NYPD_Motor_Vehicle_Collisions.csv', 'rb') as f:
        reader = csv.DictReader(f)
        time = [row['TIME'] for row in reader]
        hourCount = {}
        print time

        for timeString in time:
            c = timeString.find(":")
            hour = int(timeString[:c])
            hourCount[hour] = hourCount.get(hour,0)+1

        print hourCount

        #Makea a histogram of the maximum temps:
        plt.bar(hourCount.keys(), hourCount.values(), align='center')
        plt.title("Distribution of Accidents in NYC by Hour on 11/07/2015")
        plt.xlabel("Hours in Military Time")
        plt.ylabel("Number of Accidents")
        plt.xticks(hourCount.keys())
        plt.axis([-1,24,0,50])
        plt.yticks(np.arange(0, 50, 5))
        plt.show()
    
main()


