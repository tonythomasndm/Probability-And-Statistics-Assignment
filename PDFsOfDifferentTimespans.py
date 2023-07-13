#Long code with much clarity
from random import randint #importing random Library
import statistics,numpy as np,matplotlib.pyplot as plt #importing numpy and matplotlib Library
from math import e,pi #importing math Library

#Randomly selecting any 30 numbers between 1 and 50 which will be our 30 observed timespans
set_of_observations=[]
for i in range(30):
    set_of_observations.append(randint(1,50))
set_of_observations.sort()

#Calculating Relative Frequencies of 30 timespans
relative_frequencies=[]
for x in set_of_observations:
    relative_frequencies.append(set_of_observations.count(x)/30)

#Calculating the mean and variance for each new lists
sum_of_terms=0
number_of_terms=0
exponential_pdfs=[]
normal_pdfs=[]
sample=[]
for x in set_of_observations:

    #Calculating mean
    sum_of_terms+=x
    number_of_terms+=1
    mean=sum_of_terms/number_of_terms
    print("Mean of "+str(number_of_terms)+" elements = "+str(mean))

    #Calculating variance
    sample.append(x)
    try:
        variance=statistics.variance(sample)
    except:
        variance=0
    print("Variance of "+str(number_of_terms)+" elements = "+str(variance))
print("Graphs of the Relative Frequencies vs Timespans, Exponential PDFs vs Timespans, and Normal PDFs vs Timespans")

for x in set_of_observations:
#Calculating Exponential PDFs
    expdf=(pow(e,(-x/mean)))/mean
    exponential_pdfs.append(expdf)
#Calculating Normal PDFs
    norpdf=(1/((2*pi*variance)**0.5))*(pow(e,(-pow(x-mean,2)/(2*variance))))
    normal_pdfs.append(norpdf)

#Making Dynamic Arrays in machine based language for relative plotting
xpoints=np.array(set_of_observations)
y1points=np.array(relative_frequencies)
y2points=np.array(exponential_pdfs)
y3points=np.array(normal_pdfs)

#I dont know about your choice, you may choose as per your choice Sir
#Plotting Graphs
print("\nIf you want all in one graph,enter any number else enter \"0\" for different graphs")
count=int(input())
if count==0:
#Graph of Relative Frequencies vs Timespans
    plt.plot(xpoints,y1points)
    plt.title("Relative Frequencies vs Timespans")
    plt.ylabel("Relative Frequencies")
    plt.xlabel("Timespans")
    plt.plot()
    plt.show()
#Graph of Exponential PDFs vs Timespans
    plt.plot(xpoints,y2points)
    plt.title("Exponential PDFs vs Timespans")
    plt.ylabel("Exponential PDFs")
    plt.xlabel("Timespans")
    plt.plot()
    plt.show()
#Graph of Normal PDFs vs Timespans
    plt.plot(xpoints,y3points)
    plt.title("Normal PDFs vs Timespans")
    plt.ylabel("Normal PDFs")
    plt.xlabel("Timespans")
    plt.plot()
    plt.show()
else:
# Graphs between Relative Frequencies vs Timespans, Exponetial PDFs vs Timespans and Normal PDFs vs Timespans all in one graph
    plt.plot(xpoints,y1points,xpoints,y2points,xpoints,y3points)
    plt.title("Relative Frequencies, Exponential PDFs and Normal PDFs vs Timespans")
    plt.ylabel("Relative Frequencies-Blue Exponential PDFs-Orange Normal PDFs-Green")
    plt.xlabel("Timespans")
    plt.plot()
    plt.show()
#GOOD DAY :)