#========================================
# Nama : Ghazyhibbban Kumayl Elbees
# NIM : J0403251136
# Kelas : B1
#========================================

#========================================
# Merge Sort dengan tracing
#========================================

def merge_sort(data, depth= 0):
    indent = " " * depth
    print(f"{indent}merge_sort({data})")

    #base case
    if len(data) <= 1:
        return data
    
    #Divide : membagi data menjadi 2 bagian
    mid = len(data) //2
    left = data[:mid] #slicing bagian kiri
    right = data[mid:] #slicing bagian kanan

    #recursive call
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    merged = merge(left_sorted, right_sorted)
    print(f"{indent}merge -> {left_sorted} + {right_sorted} = {merged}")

    return merged

def merge(left,right):

    result = []
    i= 0
    j= 0

    #Membandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):  
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    #Menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])

    return result 

angka = [20,15,29,44,76,26]
x = merge_sort(angka)
print(x)