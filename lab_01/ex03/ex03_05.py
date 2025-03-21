def demsolanxuathien(lst):
    count_dict ={}
    for item in lst:
        if item in count_dict:
            count_dict[item] +=1
        else:
            count_dict[item]=1
    return count_dict
input_string = input("Nhập danh sách các từ, cách nhau bằng 1 dấu phẩy: ")
word_list = input_string.split()
solanxuathien = demsolanxuathien(word_list)
print("Số lần xuất hiện của các phần tử: ", solanxuathien)