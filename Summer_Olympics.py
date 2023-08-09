import csv
import matplotlib.pyplot as plt
from matplotlib import figure
from collections import OrderedDict
from collections import Counter
# acces route to database in csv format
file = "/Users/sbaca/Desktop/Códigos/Python/SummerOlympics/3_summer_olympics.csv"
rawData = []
with open(file, newline="") as content:  # data reader
    rawData = list(csv.reader(content))


def dataConverter(database):
    data = []
    for i in range(1, len(database)):
        row = []
        row.append(int(database[i][0]))  # Year
        row.append(database[i][1])  # City
        row.append(database[i][2])  # Sport
        row.append(database[i][3])  # Discipline
        row.append(database[i][4])  # Athlete
        row.append(database[i][5])  # Country
        row.append(database[i][6])  # Gender
        row.append(database[i][7])  # Event
        row.append(database[i][8])  # Medal
        data.append(row)
    return data


data = dataConverter(rawData)


def option_1(initialYear, finalYear):
    disciplinesList = []
    check = False
    for i in data:
        if i[0] in range(initialYear, finalYear+1):
            disciplinesList.append(i[3])
            check = True
    if check == True:
        for i in disciplinesList:
            print(i)
    else:
        print("We're sorry. No edition of the Olympic Games was held in those years. \nTry again.")


def option_2(initialYear, finalYear):
    sportsList = []
    check = False
    for i in data:
        if i[0] in range(initialYear, finalYear+1):
            sportsList.append(i[2])
            check = True
    sportsList = list(OrderedDict.fromkeys(sportsList))  # delete duplicates
    if check == True:
        for i in sportsList:
            print(i)
    else:
        print("We're sorry. No edition of the Olympic Games was held in those years. \nTry again.")


def option_3(year):
    check=False 
    sportsList=[]
    for i in data:
       if i[0] == year:
           check=True
           sportsList.append(i[2])
    fixedSportsList = list(OrderedDict.fromkeys(sportsList)) # delete duplicates for printing
    if check == True:
        MedalsCount = []
        for i in fixedSportsList:
            MedalsCount.append(sportsList.count(i)) # we can calculate the number of medals by counting the number of times each sport name is repeated
        for i in range(len(fixedSportsList)):
            print(f"{fixedSportsList[i]}: {MedalsCount[i]} medallas")
    else:
        print("We're sorry. No edition of the Olympic Games was held in that year. \nTry again.")

"""         
    years = []
    for i in data:
        years.append(i[0])
    years = list(OrderedDict.fromkeys(years))
    if year in years:
        SportsInAYear = []
        MedalsCount = []
        for i in data:
            if i[0] == year:
                SportsInAYear.append(i[2])
        fixedSIAY = list(OrderedDict.fromkeys(SportsInAYear))
        for i in fixedSIAY:
            n = (SportsInAYear.count(i))
            MedalsCount.append(n)
        for i in range(len(fixedSIAY)):
            print(f"{fixedSIAY[i]}: {MedalsCount[i]} medallas")
    else:
        print("Lo sentimos. No se celebró ninguna edición de los juegos olímpicos en ese año.\nVuelva a intentarlo.")
"""


def option_4():
    print("GOLD:")
    for i in data:
        if i[5] == "MEX" and i[8] == "Gold":
            print(f"{i[0]}:  {i[4]};  {i[2]}")
    print("")
    print("SILVER:")
    for i in data:
        if i[5] == "MEX" and i[8] == "Silver":
            print(f"{i[0]}:  {i[4]};  {i[2]}")
    print("")
    print("BRONZE:")
    for i in data:
        if i[5] == "MEX" and i[8] == "Bronze":
            print(f"{i[0]}:  {i[4]};  {i[2]}")


def option_5():
    athletes = []
    for i in range(len(data)):
        athletes.append(data[i][4])
    MVP = (Counter(athletes).most_common()[0][0]) # counter for finding the most repeated value
    noMedals = athletes.count(MVP) # count the number of medals by counting the times the athlete is repeated
    print(f"The athlete who has won the most medals is: \n{MVP} with a total of {noMedals}.")
    print("")

    MVP_results = []
    MVP_years = []
    MVP_cities=[]
    for i in data:
        row = []
        if i[4] == MVP:
            MVP_years.append(i[0])
            MVP_cities.append(i[1])
            row.append(i[0])
            row.append(i[1])
            row.append(i[3])
            row.append(i[7])
            row.append(i[8])
            MVP_results.append(row)
    MVP_years = list(OrderedDict.fromkeys(MVP_years))
    MVP_cities = list(OrderedDict.fromkeys(MVP_cities))

    for i in range(len(MVP_years)):
        print(f"On {MVP_years[i]} in the city of {MVP_cities[i]}, got the following medals: ")
        for j in MVP_results:
            if j[0]==MVP_years[i]:
                print(f"    {j[4]}:  {j[2]}, {j[3]}.")
        print("")


def option_6():
    countries = []
    x = []
    y = []
    for i in range(len(data)):
        countries.append(data[i][5])
    TopCountries = (Counter(countries).most_common()[:7:])
    for i in TopCountries:
        x.append(i[0])
        y.append(i[1])
    colors = ["blue", "r", "orange", "navy", "y", "limegreen", "darkgrey"]
    plt.figure(figsize=(10, 5))
    plt.bar(x, y, color=colors, edgecolor='black', width=.8, linewidth=1.4)
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha="center", size=10, weight="heavy")
    plt.title("Top 7 countries with the most medals won",
              size=20, y=1.1, weight="bold")
    plt.xlabel("Countries", size=17, color="#00008B")
    plt.ylabel("Number of Medals", size=17, color="#00008B")
    plt.show()


def option_7():
    champs = []
    x = []
    y = []
    for i in data:
        if i[2] == "Boxing":
            champs.append(i[5])
    champs = (Counter(champs).most_common()[:7:])
    for i in champs:
        x.append(i[0])
        y.append(i[1])
    explodenums = []
    for i in range(len(x)):
        explodenums.append(0.1)
    colors = ['royalblue', 'r', 'deepskyblue',
              'firebrick', "limegreen", "palevioletred", "gold"]
    plt.figure(figsize=(20, 8))
    plt.pie(y, labels=x, colors=colors, autopct="%1.1f%%", textprops={
            'fontsize': 12}, shadow=True, explode=explodenums)
    plt.title("Top 7 countries with the most Olympic medalists in Boxing",
              size=14, weight="bold")
    plt.show()


def main():
    exit = False
    print("Welcome to our interactive Olympics menu! \n Here you will find everything you want to know about the Olympic Games from 1896 to 2012!!!")
    while exit == False:
        print("")
        print("Which option do you want to perform?")
        print(f"  Option 1: Obtain a list of disciplines participating in the Olympic Games between two given years.")
        print(f"  Option 2: Get a list of sports, without duplicates, in the Olympic games between two given years.")
        print(f"  Option 3: Display the total medals won by sport in a given year.")
        print(f"  Option 4: Display the complete list of the great Mexican medal winners.")
        print(f"  Option 5: Calculate the competitor with the most wins in the history of the Olympic Games;\n  showing each year, city, discipline and medal per event.")
        print(f"  Option 6: Obtain the graph of the 7 countries with the highest number of medals achieved.")
        print(f"  Option 7: Make the graph of the 7 countries that have had the most medalists in Boxing.")
        print(f"  Option 8: Exit.")
        print("")
        opt = int(input("Please, enter only the number of the option: "))
        print("")
        if opt > 0 and opt < 8:
            if opt == 1:
                print(f"  Option 1")
                initialYear = int(input("Starting year: "))
                finalYear = int(input("Ending year: "))
                print("")
                option_1(initialYear, finalYear)
            if opt == 2:
                print(f"  Option 2")
                initialYear = int(input("Starting year: "))
                finalYear = int(input("Ending year: "))
                print("")
                option_2(initialYear, finalYear)
            if opt == 3:
                print(f"  Option 3")
                year = int(input("Year to display: "))
                print("")
                option_3(year)
            if opt == 4:
                print(f"  Option 4")
                print("")
                option_4()
            if opt == 5:
                print(f"  Option 5")
                print("")
                option_5()
            if opt == 6:
                print(f"  Option 6")
                option_6()
            if opt == 7:
                print(f"  Option 7")
                option_7()
        elif opt == 8:
            exit = True
            print("Thanks for using our services. Come back soon :)")
        else:
            print("Out of range. Try again")


main()
