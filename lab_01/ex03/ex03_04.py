def truycapphantu(tuple_data):
    first_element= tuple_data[0]
    last_element= tuple_data[-1]
    return first_element, last_element
input_tuple = eval(input("Nhập tuple: "))
first, last = truycapphantu(input_tuple)
print("Phần tử đầu tiên: ", first)
print("Phần tử cuối cùng: ", last)
