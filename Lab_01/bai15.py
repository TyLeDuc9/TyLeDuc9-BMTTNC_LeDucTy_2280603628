def dem_so_lan_xuat_hien(lst):
    count_dic={}
    for item in lst:
        if item in count_dic:
           count_dic[item]+=1
        else:
           count_dic[item]=1
    return count_dic
input_string=input("Nhap danh sach cac tu, cach nhau bang dau cach:")
word_list=input_string.split()

so_lan_xuat_hien=dem_so_lan_xuat_hien(word_list)
print("So lan xuat hien cua cac phan tu:", so_lan_xuat_hien)