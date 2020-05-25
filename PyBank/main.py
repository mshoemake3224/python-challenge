import os
import csv

csvpath = os.path.join('..', 'PyBank',"Resources", 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    total = 0
    months_total = 0
    previous = 0
    delta = []
    max_num = ["",0]
    min_num = ["",99999]
    change = 0
    header = next(csvreader)

    # The total number of months included in the dataset
    months_total = sum(1 for row in csvreader)
    print ("Financial Analysis")
    print (" ----------------------------")
    print ("Total Months:" , months_total)

    csvfile.seek(0)
    next(csvreader)
    for x in csvreader:
    # The net total amount of "Profit/Losses" over the entire period
        total = total + int(x[1])
    
        # The average of the changes in "Profit/Losses" over the entire period
        #Create a new column called delta
        change = int(x[1]) - previous #867884-0
        previous = int(x[1])
        delta.append(change) #[867884,116771]
        length = len(delta)-1

        if change > max_num[1]:
            max_num[0] = x[0]
            max_num[1] = change

        if change < min_num[1]:
            min_num[0] = x[0]
            min_num[1] = change

    total_average = sum(delta[1:])/length
        #Find delta for row[1]
        #Sum total of the delta column output
        #take delta_sum and divide by months_total
    print ("Total: $" , total)
    #print (delta)
    print("Average Change: $" , total_average)

    # The greatest increase in profits (date and amount) over the entire period
    #Inside of new column delta locate the maximum
    print("Greatest Increase in Profits:" , max_num[0],max_num[1])
   
    # The greatest decrease in losses (date and amount) over the entire period
    #Inside of new column delta locate the minimum
    print("Greatest Decrease in Profits:" , min_num[0],min_num[1])

# Example of Output:
    #     Financial Analysis
    # ----------------------------
    # Total Months: 86
    # Total: $38382578
    # Average  Change: $-2315.12
    # Greatest Increase in Profits: Feb-2012 ($1926159)
    # Greatest Decrease in Profits: Sep-2013 ($-2196167)

with open('PYBank_results.txt', 'w') as text:
    text.write("----------------------------------------------")
    text.write("Financial Analysis")
    text.write("-----------------------------------------------")
    text.write("Total: $" , total)
    text.write("Average Change: $" , total_average)
    text.write("Greatest Increase in Profits:" , max_num[0],max_num[1])
    text.write("Greatest Decrease in Profits:" , min_num[0],min_num[1])
    text.write("------------------------------------------------")