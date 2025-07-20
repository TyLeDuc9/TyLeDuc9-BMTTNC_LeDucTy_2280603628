def dao_nguoc_list(lst):
    return lst[::-1]
input_list=input("Nhap danh sach cac so, cach nhau bang dau phay:")
numbers=list(map(int , input_list.split(',')))
dao_nguoc_list=dao_nguoc_list(numbers)
print("List khi dao nguoc:", dao_nguoc_list)