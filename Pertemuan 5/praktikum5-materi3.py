#=================================================
#Nama : Ghazyhibban Kumayl Elbees
#NIM : J0403251136
#Kelas : B1
#=================================================

#=================================================
#Materi Rekursif : Menjumlahkan Elemen List
#=================================================

def jumlah_list(data, index=0):
    #base case
    if index == len(data):
        return 0
    
    #recursive case
    return data[index] + jumlah_list(data, index+1)

print("============Program jumlah data =============")
print(jumlah_list({2,4,5}))