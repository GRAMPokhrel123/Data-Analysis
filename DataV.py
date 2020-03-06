import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
def banner():
    for i in range(90):
        print("*", end="")
    print()
    print("\n\t\t\tThe Australian Tax Office(ATO): TOOTH FAIRY")
    print('\t\t\t\t\t\tName: Parminder Pal Singh')
    print('\t\t\t\t\t\tID:   30377649')
    print('\n')

    for i in range(90):
        print("*", end="")
    print()
    print("\t1.Statistics")
    print("\t2.Export Children details who haven't lost any Teeth")
    print("\t3.Display Number of Claims per State")
    print("\t4.Compare Two States")
    print("\t5.Exit")
    print()
    for i in range(90):
        print("*", end="")
    print()
banner()

while(True):
    # banner()
    Data = pd.read_csv('addresses.csv')
    choice = int(input("Enter the The Number to Choice:"))
    print()
    if choice == 1:

        def total_children():
            Children = Data['Total number of teeth lost'].count()
            print("1:Total number of children in list:",Children)
        total_children()


        def Average_teeth():
            sum_totalAvarage = Data['Total number of teeth lost'].mean()
            print("2:Average number of Teeth claims over the years:", sum_totalAvarage)

        Average_teeth()

        def Never_lost():
            total_number_of_teeth_lost =Data['Total number of teeth lost']
            never1 = Data.loc[total_number_of_teeth_lost== 0,'Total number of teeth lost'].count()
            print("3:Number of Children who have never loss a  Tooth:", never1)

        Never_lost()

        def total_number():
            total_number_of_teeth_lost = Data['Total number of teeth lost']
            never1 = Data.loc[total_number_of_teeth_lost == 20, 'Total number of teeth lost'].count()
            print("4:Number of Children who have lost all their Baby Teeth:", never1)

        total_number()

        def Amount_expenditure():

            total_number_of_teeth_lost = Data['Total number of teeth lost']
            never1 = Data.loc[total_number_of_teeth_lost == 1, 'Total number of teeth lost'].count()
            never2 = Data.loc[total_number_of_teeth_lost > 1, 'Total number of teeth lost'].count()
            # print("Total amount for one teeth lost is $1:", never1*1)
            # print("Total amount for more than one teeth is $0.5:", never2*0.5)
            total= never1*1 + never2 *0.5
            print("5:Total Amount Expenditure for this year:$",total)

        Amount_expenditure()

        print()


    elif choice == 2:
        total_number_of_teeth_lost = Data['Total number of teeth lost']
        never1 = Data.loc[total_number_of_teeth_lost == 0, 'Total number of teeth lost'].count()
        # never2 =never1


        Enter = input("Enter the File Name in text:")
        print()
        df = DataFrame(columns=[never1])
        df.to_csv(Enter)
        print(never1,"Children has been save to",Enter)
        print()
    elif choice == 3:
        def graph_perstate():
            TAS1 = Data[Data.State == 'TAS']
            data1 = TAS1['Total number of teeth lost'].count()

            QLD1 = Data[Data.State == 'QLD']
            data2 = QLD1['Total number of teeth lost'].count()

            WA1 = Data[Data.State == 'WA']
            data3 = WA1['Total number of teeth lost'].count()

            NSW1 = Data[Data.State == 'NSW']
            data4 = NSW1['Total number of teeth lost'].count()

            SA1 = Data[Data.State == 'SA']
            data5 = SA1['Total number of teeth lost'].count()

            VIC1 = Data[Data.State == 'VIC']
            data6 = VIC1['Total number of teeth lost'].count()

            NT1 = Data[Data.State == 'NT']
            data7 = NT1['Total number of teeth lost'].count()

            data8 = [data1, data2, data3, data4, data5, data6, data7]
            x = ["TAS", "QLD", "WA", "NSW", "SA", "VIC", "NT"]
            plt.bar(x, data8)
            plt.grid(True, linewidth=1)
            plt.show()


        graph_perstate()

    elif choice == 4:
        def two_state():
            TAS = Data[Data.State == 'TAS']
            data1 = TAS['Total number of teeth lost'].mean()

            NSW = Data[Data.State == 'NSW']
            data2 = NSW['Total number of teeth lost'].mean()

            data3 = [data1, data2]
            x = ["TAS", "NSW"]

            plt.bar(x, data3)
            plt.grid(True, linewidth=1)
            plt.show()

        two_state()


    else:
        print("GoodBye and Take Care!!")
        break