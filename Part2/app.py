import csv
from collections import Counter

with open('Student_marks_list.csv',newline='\n') as csvfile:
    data = list(csv.reader(csvfile,delimiter=','))

maths_marks = {}
biology_marks = {}
english_marks = {}
physics_marks ={}
chemistry_marks ={}
hindi_marks={}
total_marks = {}

for i in data[1:]:
    maths_marks[i[0]] = int(i[1])
    biology_marks[i[0]] = int(i[2])
    english_marks[i[0]] = int(i[3])
    physics_marks[i[0]] = int(i[4])
    chemistry_marks[i[0]] = int(i[5])
    hindi_marks[i[0]] = int(i[6])
    total_marks[i[0]] = maths_marks[i[0]] + biology_marks[i[0]] + english_marks[i[0]] + physics_marks[i[0]] + chemistry_marks[i[0]] + hindi_marks[i[0]] 


maths_topper = max(zip(maths_marks.values(),maths_marks.keys()))[1]
biology_topper = max(zip(biology_marks.values(),biology_marks.keys()))[1]
english_topper = max(zip(english_marks.values(),english_marks.keys()))[1]
physics_topper = max(zip(physics_marks.values(),physics_marks.keys()))[1]
chemistry_topper = max(zip(chemistry_marks.values(),chemistry_marks.keys()))[1]
hindi_topper = max(zip(hindi_marks.values(),hindi_marks.keys()))[1]

k = Counter(total_marks)
top3 = k.most_common(3)

first_rank,second_rank,third_rank = top3[0][0],top3[1][0],top3[2][0]

print("Toppers in Maths is ",maths_topper)
print("Toppers in Biology is ",biology_topper)
print("Toppers in English is ",english_topper)
print("Toppers in Physics is ",physics_topper)
print("Toppers in Chemistry is ",chemistry_topper)
print("Toppers in Hindi is ",hindi_topper)
print("Best students in the class are ({},{},{})".format(first_rank,second_rank,third_rank))


# Complexities 
# Time - O(n) (n - number of data)
# Space - O(n) (n - every data is restored in the dictionary again)







        

