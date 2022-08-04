Data = {
    "Name": "Shubham Kumar Singh",
    "Age": 24,
    "Salary": 100000,
    "City": "Bihar"
}
# rename key in dictionary
Data["Location"] = Data["City"]
del Data["City"]
# display the dictionary
print(Data)
