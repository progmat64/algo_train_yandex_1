add_phone = input()
phone_1 = input()
phone_2 = input()
phone_3 = input()

arr = [add_phone, phone_1, phone_2, phone_3]
arr_edited = []
arr_edited_2 = []

for phone in arr:
    new_phone = ""
    for i in phone:
        if i == ")" or i == "(" or i == "-":
            continue
        new_phone += i
    arr_edited.append(new_phone)

for phone in arr_edited:
    new_phone = ""
    if len(phone) == 7:
        new_phone = "+7495" + phone
    elif phone[0] == "8":
        new_phone = "+7" + phone[1:]
    else:
        new_phone = phone
    arr_edited_2.append(new_phone)

phone_my = arr_edited_2[0]


if arr_edited_2[0] == arr_edited_2[1]:
    print("YES")
else:
    print("NO")

if arr_edited_2[0] == arr_edited_2[2]:
    print("YES")
else:
    print("NO")

if arr_edited_2[0] == arr_edited_2[3]:
    print("YES")
else:
    print("NO")
