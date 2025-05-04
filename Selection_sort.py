def SelectionSort(arr):
    n=len(arr)
    
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
             
        arr[i],arr[min_index]=arr[min_index],arr[i]
             
        print(f"step{i+1}: {arr}")
        
    return arr   

arr = [144,123,4545,342,75,23]
print("Original array :",arr)

sorted_arr = SelectionSort(arr)

print("sorted array",sorted_arr)