#  sort hexadecimal
hexa = [0x1, 0x10, 0x4]
sort_hex = [i for i in sorted(hexa)]
new_hex = []
for i in sort_hex:
    new = hex(i)
    new_hex.append(new)
print(new_hex)


# rotate array
def solution(A,k):
    for i in range(k+1):
        # slice first items
        first_item = A[0:len(A)-k]
        # set empty rotation list
        rotated_list =[]
        # loop through array
        for j in A:
            # remove last item
            last_item = A.pop(-1)
            # insert last item in front
            rotated_list.insert(0,last_item)
        # return joine first and last
        joined_list =rotated_list+first_item
        # return joined
        return joined_list

         
    

print (solution([3,8,9,7,6],3))

            


