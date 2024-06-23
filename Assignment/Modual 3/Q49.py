def check_numbre(check_num, start_num, end_num):
    if check_num in range(start_num, end_num):
        print(f'The {check_num} Number is Between {start_num} to {end_num}')
    else:
        print(f'The {check_num} Number is Not Between {start_num} to {end_num}')


start_num=int(input("Enter Start number: "))
end_num=int(input("Enter End number: "))
check_num=int(input("Enter Number to Check: "))


check_numbre(check_num, start_num, end_num)