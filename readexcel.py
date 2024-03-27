import pandas as pd


input_data = 6732
#read excel table
filePath = "/home/ek/Downloads/5305_1.xls"
saveCsvDocument = "/home/ek/Downloads/savecsvdocument.csv"

faila_saturs = pd.read_excel(filePath)
faila_saturs.to_csv("savecsvdocument.csv", sep=",", index=False)

#num_rows = len(faila_saturs)

#print(f"Number of rows: {num_rows}")
# Lai zinatu cik ir aktivi row panemu num_rows un no ta noskaitu -3 no beigam un saku no 2row - derigie index no 2 lidz (30-3) = 2 lidz 27

#chosen_row_index = 0
#chosen_row = faila_saturs.iloc[chosen_row_index]

#print(f"Content of row {chosen_row_index}: {chosen_row.values}")

#print("------------------------------------------------------------")

#chosen_column_index = 3
#chosen_column = faila_saturs.loc[chosen_column_index]

#print(target_code)
#print("------------------------------------------------------------")
target_code = faila_saturs["Unnamed: 1"]
destinationCodeList = []

number_for_column = 0
number_for_row = 0
countDestinationCode = 0
condition_met = False

for value in target_code:
    if not isinstance(value, int):
        continue
    destinationCodeList.append(value)
    #print(value)
    countDestinationCode = countDestinationCode + 1
    #print(countDestinationCode)

    if value == input_data:
        number_for_row = countDestinationCode + 1
        number_for_column = countDestinationCode + 4
        result = faila_saturs.iloc[number_for_row,number_for_column]
        continueResult = faila_saturs.iloc[number_for_row +1,number_for_column]
        #print(faila_saturs.iloc[number_for_row,number_for_column])
        #print(continueResult)
        #print(f"Lidz nakamajai pieturai - {value} bus jamaksa papildus: {continueResult}")
        #print(number_for_row)
        number_for_row = number_for_row - 1
    number_for_row = number_for_row + 1
    price_for_next_row = faila_saturs.iloc[number_for_row, number_for_column]
    #print(number_for_row, number_for_column, )

    if value == input_data and countDestinationCode == price_for_next_row:
        if not condition_met:
            condition_met = True
            continue
        #te kaut kas jadara?
        if value == input_data:
            number_for_row = number_for_row -1
            #print(number_for_row)
            updated_number_for_column = number_for_column - countDestinationCode + 1
            price_for_next_row = faila_saturs.iloc[number_for_row, updated_number_for_column]
            #print(updated_number_for_column)
            #print(number_for_column)
            #print(countDestinationCode)
        

    if not (isinstance(price_for_next_row, (int, float))):
        continue
    

    print(f"no pieturas - {input_data} Lidz pieturai - {value} bus jamaksa papildus: {price_for_next_row}")
    #print(number_for_row)


 