year = int(input())
century = (year // 100 + 1)
if year % 1000 == 0:
    century = century - 1
print (century)