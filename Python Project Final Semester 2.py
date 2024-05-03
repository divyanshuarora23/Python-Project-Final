import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

def display_menu():
    print(":)")
    print("Name: Divyanshu Arora\nSAP ID: 500121802\nR NO.: R2142231451\nSubmitted To: Ms. Sugandha Sharma.\nTopic: Data Visualization.")
    print()
    print("For Data Visualization")
    print("#1. For checking the data.")
    print("#2. Reading complete file without index.")
    print("===================")
    print(" ")
    print("#3. Line Chart")
    print("\tPress 1 to print the data for Cases Pending as per Crime.")
    print("\tPress 2 to print the data for Cases Reported as per Crime.")
    print("\tPress 3 to print the data for Cases Reopened as per Crime.")
    print("\tPress 4 to print the data for Total Cases as per Crime.")
    print("\tPress 5 to print All data.")
    print(" ")
    print("#4. Bar Graph")
    print("\tPress 1 to print the data for Cases Pending as per Crime.")
    print("\tPress 2 to print the data for Cases Reported as per Crime.")
    print("\tPress 3 to print the data for Cases Reopened as per Crime.")
    print("\tPress 4 to print the data for Total Cases as per Crime.")
    print("\tPress 5 to print the data in form of stack bar chart")
    print("\tPress 6 to print the data in form of multi bar chart")
    print(" ")
    print("#5. Scatter Chart")
    print(" ")
    print("#6. For Exit")
    print("===============")

def Read_CSV():
    print("The Data")
    df=pd.read_csv('D:\Crimes Test.csv')
    print(df)

def No_Index():
    print("Reading the file without index")
    df=pd.read_csv('D:\Crimes Test.csv', index_col=0)
    print(df)

#FOR LINE CHART:)

def line_plot():
    df=pd.read_csv('D:\Crimes Test.csv')
    df['Crimes'] = ['MDR','HOM','DBN','DBR','HAR','OAS','DDR','DDM','DDC','DDO','DDH','AOS','ATM','ATH']
    #MDR=Murder, HOM=Homicide,DBN=Death by negligence,DBR=Death by road accidents,HAR=Hit and run,OAS=Other accidents,
    #DDR=Death due railway accident,DDM=Death due to medical negligence,DDC= Death due to civic bodies,DDO=Death due to other negligence,
    #DDH=Dowry death,AOS=Abetment of Suicide,ATM=Attempt to Commit Murder,ATH=Attempt to commit Culpable Homicide
    Crime=df["Crimes"]
    Pending=df["Cases Pending "]
    Reported=df["Cases Reported"]
    Reopened=df["Cases Reopened"]
    Total=df["Total Cases"]
    plt.xlabel("Crimes")

    
    YC = int(input("Enter the number representing your preferred line chart from the above choices: "))
    
    if YC == 1:
        plt.ylabel("Cases Pending")
        plt.title("Crimes Wise Cases Pending")
        plt.plot(Crime,Pending, color='b')
        plt.show()
    elif YC == 2:
        plt.ylabel("Cases Reported")
        plt.title("Crimes Wise Cases Reported")
        plt.plot(Crime,Reported, color='g')
        plt.show()
    elif YC == 3:
        plt.ylabel("Cases Reopened")
        plt.title("Crimes Wise Cases Reopened")
        plt.plot(Crime,Reopened, color='r')
        plt.show()
    elif YC == 4:
        plt.ylabel("Total Cases")
        plt.title("Crimes Wise Total Cases")
        plt.plot(Crime,Total, color='c')
        plt.show()
    elif YC == 5:
        plt.ylabel("Number of cases")
        plt.plot(Crime, Pending, color='b', label = "Crimes Wise Cases Pending")
        plt.plot(Crime, Reported, color='g', label = "Crimes Wise Cases Reported")
        plt.plot(Crime, Reopened, color='r', label = "Crimes Wise Cases Reopened")
        plt.plot(Crime, Total, color='c', label = "Crimes Wise Total Cases")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")
        

#FOR BAR GRAPH:)

def bar_plot():
    df=pd.read_csv('D:\Crimes Test.csv')
    df['Crimes'] = ['MDR','HOM','DBN','DBR','HAR','OAS','DDR','DDM','DDC','DDO','DDH','AOS','ATM','ATH']
    #MDR=Murder, HOM=Homicide,DBN=Death by negligence,DBR=Death by road accidents,HAR=Hit and run,OAS=Other accidents,
    #DDR=Death due railway accident,DDM=Death due to medical negligence,DDC= Death due to civic bodies,DDO=Death due to other negligence,
    #DDH=Dowry death,AOS=Abetment of Suicide,ATM=Attempt to Commit Murder,ATH=Attempt to commit Culpable Homicide
    Crime=df["Crimes"]
    Pending=df["Cases Pending "]
    Reported=df["Cases Reported"]
    Reopened=df["Cases Reopened"]
    Total=df["Total Cases"]
    plt.xlabel("Crimes")


    YC = int(input("Enter the number representing your preferred bar graph from the above choices:"))
    
    if YC == 1:
        plt.ylabel("Cases Pending")
        plt.title("Cases Pending")
        plt.bar(Crime, Pending,color='blue',width=0.5)
        plt.show()
    elif YC == 2:
        plt.ylabel("Cases Reported")
        plt.title("Cases Reported")
        plt.bar(Crime, Reported, color='g', width = 0.5)
        plt.show()
    elif YC == 3:
        plt.ylabel("Cases Reopened")
        plt.title("Cases Reopened")
        plt.bar(Crime, Reopened, color='r', width = 0.5)
        plt.show()
    elif YC == 4:
        
        plt.ylabel("Total Cases")
        plt.title("Crimes Wise Total Cases")
        plt.bar(Crime,Total, color='c', width = 0.5)
        plt.show()
    elif YC == 5:
        plt.ylabel("Number of cases")
        plt.bar(Crime, Pending, color='b', width=0.5 , label = "Crimes Wise Cases Pending")
        plt.bar(Crime, Reported, color='g', width=0.5 , label = "Crimes Wise Cases Reported")
        plt.bar(Crime, Reopened, color='r', width=0.5 , label = "Crimes Wise Cases Reopened")
        plt.bar(Crime, Total, color='c', width=0.5 , label = "Crimes Wise Total Cases")
        plt.legend()
        plt.show()
    elif YC == 6:
        D=np.arange(len(Crime))
        # width=0.25
        plt.bar(D, Pending, color='b',width = 0.25, label = "Crimes Wise Cases Pending")
        plt.bar(D+0.25, Reported, color='g',width=0.25, label = "Crimes Wise Cases Reported")
        plt.bar(D+0.50, Reopened, color='r',width=0.25, label = "Crimes Wise Cases Reopened")
        plt.bar(D+0.75, Total , color='c',width=0.25, label = "Crime Wise Total Cases")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")
        
def scatter_chart():
    df=pd.read_csv('D:\Crimes Test.csv')
    df['Crimes'] = ['MDR','HOM','DBN','DBR','HAR','OAS','DDR','DDM','DDC','DDO','DDH','AOS','ATM','ATH']
    #MDR=Murder, HOM=Homicide,DBN=Death by negligence,DBR=Death by road accidents,HAR=Hit and run,OAS=Other accidents,
    #DDR=Death due railway accident,DDM=Death due to medical negligence,DDC= Death due to civic bodies,DDO=Death due to other negligence,
    #DDH=Dowry death,AOS=Abetment of Suicide,ATM=Attempt to Commit Murder,ATH=Attempt to commit Culpable Homicide
    Crime=df["Crimes"]
    Pending=df["Cases Pending "]
    Reported=df["Cases Reported"]
    Reopened=df["Cases Reopened"]
    Total=df["Total Cases"]
    plt.xlabel("Crimes")
    
    SC=plt.gca()
    SC=plt.scatter(Crime, Pending, color="b", label="Crimes Wise Cases Pending")
    SC=plt.scatter(Crime, Reported, color="g", label="Crimes Wise Cases Reported")
    SC=plt.scatter(Crime, Reopened, color="r", label="Crimes Wise Cases Reopened")
    SC=plt.scatter(Crime, Total, color="c", label="Crimes Wise Total Cases")
    
    plt.xlabel("Crimes")
    plt.title("Complete Scatter Chart")
    plt.legend()
    plt.show()
# Function to handle button click event
def on_click():
    choice = int(entry.get())  # Get the choice entered by the user

    if choice == 1:
        Read_CSV()
    elif choice == 2:
        No_Index()
    elif choice == 3:
        line_plot()
    elif choice == 4:
        bar_plot()
    elif choice == 5:
        scatter_chart()
    elif choice == 6:
        print("Thank You for using...")

# Create the main window
root = Tk()
root.title("Data Visualization Menu")

# Create and place the entry field and button
entry_label = Label(root, text="Enter Your Choice:")
entry_label.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="Submit", command=on_click)
button.pack()

# Run the Tkinter event loop
root.mainloop()


def display_menu():
    print(":)")
    print("Name: Divyanshu Arora\nSAP ID: 500121802\nR NO.: R2142231451\nSubmitted To: Ms. Sugandha Sharma.\nTopic: Data Visualization.")
    print()
    print("For Data Visualization")
    print("#1. For checking the data.")
    print("#2. Reading complete file without index.")
    print("===================")
    print(" ")
    print("#3. Line Chart")
    print("\tPress 1 to print the data for Cases Pending as per Crime.")
    print("\tPress 2 to print the data for Cases Reported as per Crime.")
    print("\tPress 3 to print the data for Cases Reopened as per Crime.")
    print("\tPress 4 to print the data for Total Cases as per Crime.")
    print("\tPress 5 to print All data.")
    print(" ")
    print("#4. Bar Graph")
    print("\tPress 1 to print the data for Cases Pending as per Crime.")
    print("\tPress 2 to print the data for Cases Reported as per Crime.")
    print("\tPress 3 to print the data for Cases Reopened as per Crime.")
    print("\tPress 4 to print the data for Total Cases as per Crime.")
    print("\tPress 5 to print the data in form of stack bar chart")
    print("\tPress 6 to print the data in form of multi bar chart")
    print(" ")
    print("#5. Scatter Chart")
    print(" ")
    print("#6. For Exit")
    print("===============")


def Read_CSV():
    print("The Data")
    df=pd.read_csv('D:\Crimes Test.csv')
    print(df)

def No_Index():
    print("Reading the file without index")
    df=pd.read_csv('D:\Crimes Test.csv', index_col=0)
    print(df)

#FOR LINE CHART:)

def line_plot():
    df=pd.read_csv('D:\Crimes Test.csv')
    df['Crimes'] = ['MDR','HOM','DBN','DBR','HAR','OAS','DDR','DDM','DDC','DDO','DDH','AOS','ATM','ATH']
    #MDR=Murder, HOM=Homicide,DBN=Death by negligence,DBR=Death by road accidents,HAR=Hit and run,OAS=Other accidents,
    #DDR=Death due railway accident,DDM=Death due to medical negligence,DDC= Death due to civic bodies,DDO=Death due to other negligence,
    #DDH=Dowry death,AOS=Abetment of Suicide,ATM=Attempt to Commit Murder,ATH=Attempt to commit Culpable Homicide
    Crime=df["Crimes"]
    Pending=df["Cases Pending "]
    Reported=df["Cases Reported"]
    Reopened=df["Cases Reopened"]
    Total=df["Total Cases"]
    plt.xlabel("Crimes")

    
    YC = int(input("Enter the number representing your preferred line chart from the above choices: "))
    
    if YC == 1:
        plt.ylabel("Cases Pending")
        plt.title("Crimes Wise Cases Pending")
        plt.plot(Crime,Pending, color='b')
        plt.show()
    elif YC == 2:
        plt.ylabel("Cases Reported")
        plt.title("Crimes Wise Cases Reported")
        plt.plot(Crime,Reported, color='g')
        plt.show()
    elif YC == 3:
        plt.ylabel("Cases Reopened")
        plt.title("Crimes Wise Cases Reopened")
        plt.plot(Crime,Reopened, color='r')
        plt.show()
    elif YC == 4:
        plt.ylabel("Total Cases")
        plt.title("Crimes Wise Total Cases")
        plt.plot(Crime,Total, color='c')
        plt.show()
    elif YC == 5:
        plt.ylabel("Number of cases")
        plt.plot(Crime, Pending, color='b', label = "Crimes Wise Cases Pending")
        plt.plot(Crime, Reported, color='g', label = "Crimes Wise Cases Reported")
        plt.plot(Crime, Reopened, color='r', label = "Crimes Wise Cases Reopened")
        plt.plot(Crime, Total, color='c', label = "Crimes Wise Total Cases")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")
        

#FOR BAR GRAPH:)

def bar_plot():
    df=pd.read_csv('D:\Crimes Test.csv')
    df['Crimes'] = ['MDR','HOM','DBN','DBR','HAR','OAS','DDR','DDM','DDC','DDO','DDH','AOS','ATM','ATH']
    #MDR=Murder, HOM=Homicide,DBN=Death by negligence,DBR=Death by road accidents,HAR=Hit and run,OAS=Other accidents,
    #DDR=Death due railway accident,DDM=Death due to medical negligence,DDC= Death due to civic bodies,DDO=Death due to other negligence,
    #DDH=Dowry death,AOS=Abetment of Suicide,ATM=Attempt to Commit Murder,ATH=Attempt to commit Culpable Homicide
    Crime=df["Crimes"]
    Pending=df["Cases Pending "]
    Reported=df["Cases Reported"]
    Reopened=df["Cases Reopened"]
    Total=df["Total Cases"]
    plt.xlabel("Crimes")


    YC = int(input("Enter the number representing your preferred bar graph from the above choices:"))
    
    if YC == 1:
        plt.ylabel("Cases Pending")
        plt.title("Cases Pending")
        plt.bar(Crime, Pending,color='blue',width=0.5)
        plt.show()
    elif YC == 2:
        plt.ylabel("Cases Reported")
        plt.title("Cases Reported")
        plt.bar(Crime, Reported, color='g', width = 0.5)
        plt.show()
    elif YC == 3:
        plt.ylabel("Cases Reopened")
        plt.title("Cases Reopened")
        plt.bar(Crime, Reopened, color='r', width = 0.5)
        plt.show()
    elif YC == 4:
        
        plt.ylabel("Total Cases")
        plt.title("Crimes Wise Total Cases")
        plt.bar(Crime,Total, color='c', width = 0.5)
        plt.show()
    elif YC == 5:
        plt.ylabel("Number of cases")
        plt.bar(Crime, Pending, color='b', width=0.5 , label = "Crimes Wise Cases Pending")
        plt.bar(Crime, Reported, color='g', width=0.5 , label = "Crimes Wise Cases Reported")
        plt.bar(Crime, Reopened, color='r', width=0.5 , label = "Crimes Wise Cases Reopened")
        plt.bar(Crime, Total, color='c', width=0.5 , label = "Crimes Wise Total Cases")
        plt.legend()
        plt.show()
    elif YC == 6:
        D=np.arange(len(Crime))
        # width=0.25
        plt.bar(D, Pending, color='b',width = 0.25, label = "Crimes Wise Cases Pending")
        plt.bar(D+0.25, Reported, color='g',width=0.25, label = "Crimes Wise Cases Reported")
        plt.bar(D+0.50, Reopened, color='r',width=0.25, label = "Crimes Wise Cases Reopened")
        plt.bar(D+0.75, Total , color='c',width=0.25, label = "Crime Wise Total Cases")
        plt.legend()
        plt.show()
    else:
        print("Enter valid input")
        
def scatter_chart():
    df=pd.read_csv('D:\Crimes Test.csv')
    df['Crimes'] = ['MDR','HOM','DBN','DBR','HAR','OAS','DDR','DDM','DDC','DDO','DDH','AOS','ATM','ATH']
    #MDR=Murder, HOM=Homicide,DBN=Death by negligence,DBR=Death by road accidents,HAR=Hit and run,OAS=Other accidents,
    #DDR=Death due railway accident,DDM=Death due to medical negligence,DDC= Death due to civic bodies,DDO=Death due to other negligence,
    #DDH=Dowry death,AOS=Abetment of Suicide,ATM=Attempt to Commit Murder,ATH=Attempt to commit Culpable Homicide
    Crime=df["Crimes"]
    Pending=df["Cases Pending "]
    Reported=df["Cases Reported"]
    Reopened=df["Cases Reopened"]
    Total=df["Total Cases"]
    plt.xlabel("Crimes")
    
    SC=plt.gca()
    SC=plt.scatter(Crime, Pending, color="b", label="Crimes Wise Cases Pending")
    SC=plt.scatter(Crime, Reported, color="g", label="Crimes Wise Cases Reported")
    SC=plt.scatter(Crime, Reopened, color="r", label="Crimes Wise Cases Reopened")
    SC=plt.scatter(Crime, Total, color="c", label="Crimes Wise Total Cases")
    
    plt.xlabel("Crimes")
    plt.title("Complete Scatter Chart")
    plt.legend()
    plt.show()
    
display_menu()
YC = int(input("Enter Your Choice: "))

while YC == 1 or YC == 2 or YC == 3 or YC == 4 or YC == 5 or YC == 6:

    if YC == 1:
        Read_CSV()
        break
    elif YC == 2:
        No_Index()
        break
    elif YC == 3:
        line_plot()
        break
    elif YC == 4:
        bar_plot()
        break
    elif YC == 5:
        scatter_chart()
        break
    elif YC == 6:
        print("Thank You for using...")
        break
    else:
        print("Enter valid input")
        break
