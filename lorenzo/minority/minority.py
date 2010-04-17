#! /usr/bin/python

def minority(T):
    if len(T) <=  1:
        return T
    mid = len(T) / 2
    left = T[:mid]
    right = T[mid:]
    left = minority(left)
    right = minority(right)
    
    if left == []:
        return right
    elif right == []:
        return left
    elif left[-1] >= right[0]:
        result = eliminate(left, right)
    else:
        result = left.extend(right)

    return result
        
def eliminate(left, right):
    len_left = len(left)
    len_right = len(right)
    while len_left > 0 and len_right > 0: 
        left = left[1:]
        right = right[1:]
        len_left -= 1
        len_right -= 1

    if len_left == 0:
        return right
    else:
        return left










# def majority(T):
#     length = len(T)
#     low = length / 2
#     if length != 1:
#         m_element = majority(T[:low])
#     else:
#         return (T[0],1)

#     count = 0
#     for x in T[low:]: #parte derecha de la lista
#         if x != m_element[0]:
#             continue
#         else:
#             count += 1
#             break

#     if count == 0:
#         return (m_element[0], m_element[1])
        
#     # Se busca el elemento en la derecha
#     m_element = majority(T[low:]) 
#     count = 0

#     for x in T[:low]: #parte izquierda de la lista
#         if x != m_element[0]:
#             continue
#         else:
#             count += 1
#             break

#     if count == 0:
#         return (m_element[0], m_element[1])
#     else:
#         return (0,0)
    
