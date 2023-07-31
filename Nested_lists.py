#Given the names and grades for each student in a class of  students, 
#store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

if __name__ == '__main__':
    alist = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])
second_highest = sorted(set([score for name, score in alist]))[1]
print('\n'.join(sorted([name for name, score in alist if score == second_highest])))