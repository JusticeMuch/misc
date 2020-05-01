# def selection(data):
#     for i in range(len(data)):
#         for k in range(i ,len(data)):
#             if (data[k] < data[i]):
#                 data[i], data[k] = data[k] , data[i]
#     print(data)

# def selection(data):
#     for i in range(len(data)):
#         minIndex = i
#         for k in range(i ,len(data)):
#             if (data[k] < data[i]):
#                 minIndex = k
#         data[i], data[minIndex] = data[minIndex] , data[i]
#     print(data)

# selection([9 , 8, 7, 6, 5, 15 , 12 , -2])

# def bubble(data):
#     swap = 1
#     while (swap != 0):
#         swap = 0
#         for i in range(len(data)):
#             if (i > 0 and data[i] < data[i - 1]):
#                 data[i], data[i - 1] = data[i - 1], data [i]
#                 swap = swap + 1
#     print(data)

# bubble([9 , 8, 7, 6, 5, 15 , 12 , -2])

# def insertion(data):
#     for i in range(1, len(data)):
#         val = data[i]
#         ind = i
#         for j in range(i - 1, -2, -1) :
#             data[j + 1] = data[j]
#             ind = j
#             if (val > data[j]):
#                 break
#         data[ind + 1] = val
#     print(data)

# insertion([9 , 8, 7, 6, 5, 15 , 12 , -2])

# def combine(d1, d2):
#     res = []
#     count1 = 0
#     count2 = 0
#     len1 = len(d1)
#     len2 = len(d2)
#     while ((count1 < len1) or (count2 < len2)):
#         if (count2 >= len2 or (count1 < len1 and d1[count1] < d2[count2])):
#             res.append(d1[count1])
#             count1 = count1 + 1
#         else:
#             res.append(d2[count2])
#             count2 = count2 + 1
#     return res

# def split(arr, l):
#     ar1 = arr[:int(l/2)]
#     ar2 = arr[int(l/2):]
#     if l >= 4 :
#         return combine (split(ar1, len(ar1)), split(ar2, len(ar2)))
#     elif l == 2:
#         return combine(ar1, ar2)
#     else:
#         return combine (ar1, split(ar2, len(ar2)))

# def merge(data):
#     print(split(data, len(data)))

# merge([9 , 8, 7, 6, 5, 15 , 12 , -2])

# def quickMerge(arr, l):
#     if (l == 1 or l == 0):
#         return arr
#     pivot = arr[int(l/2)]
#     arr1 = []
#     arr2 = [] 
#     for i in arr:
#         if i < pivot:
#             arr1.append(i)
#         elif i > pivot:
#             arr2.append(i)
#     return (quickMerge(arr1, len(arr1)) + [pivot] +  quickMerge(arr2, len(arr2)))

# def quick(data):
#     print(quickMerge(data, len(data)))

# quick([9 , 8, 7, 6, 5, 15 , 12 , -2])

