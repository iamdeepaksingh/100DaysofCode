list1 = [1,2,3]

list2 =[i+1 for i in list1]
#print(list2)
list3 = [i*2 for i in range(1, 5) if i%2 == 0]
#print(list3)

student_dict = {
    "student": ["Deepak", "Vinay"],
    "score": [89, 99]
                }
import pandas
pd = pandas.DataFrame(student_dict)
for (k, v) in student_dict.items():
    #print(v)
    print(v)

print(pd)
print('\n')

for (k,v) in pd.items():
    print(v)
print('\n')
for (index,row) in pd.iterrows():
    print(row)
    print(row.student)

