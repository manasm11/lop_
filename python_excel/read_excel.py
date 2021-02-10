from pandas import read_excel

excel_file = read_excel('../meet_discussions/Graph_DB_Structure.xlsx')
print(excel_file)

print(excel_file.iloc[:,:])

# excel_file.to_excel('testing.xls', index=0)