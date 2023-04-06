#Q1:
Names = ["Amal", "Mohammed", "Khadijah", "Abdullah", "Rawan", "Faisal", "Layla"]
Numbers = ["0568323222", "0522222232", "0545341144", "0545534556", "0560664566", "0567917077"]
Phone_book = {"Number" : Numbers, "Name" : Names }

number = input(" Enter the phone Number")

if not number.isdigit():
    print("This is invalid number, use only number.")
elif not number in Phone_book:
    print("sorry, the phone number is not found")
elif len(number) < or len(number) > 10:
    print("This is invalis number")
else:
    print("The phone Number is for:", Phone_book[number])




#Q2:
List = [5, 0, 34, 9, 0, 13, 8]
NewList = List.sort()