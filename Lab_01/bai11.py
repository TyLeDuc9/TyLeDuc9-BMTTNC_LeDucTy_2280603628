def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong+=num
    return tong

input_list = input("Nhap danh sach cac so, cach nhau bang dau phay:")
numbers=list(map(int, input_list.split(',')))

tong_chan=tinh_tong_so_chan(numbers)
print("Tong cac so chan trong List la:", tong_chan)
        