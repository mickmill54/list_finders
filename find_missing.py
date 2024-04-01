def find_missing_number(num_list):

    sum_list = 0
    sum_total = 0

    n = len(num_list) + 1
    sum_total = n*(n+1)/2
    # print("Sum Total: ", sum_total)
  
    for num in num_list:
        sum_list += num
        print(int(sum_total) - int(sum_list))
    
    # print("Sum Total",int(sum_total) - int(sum_list))
    return int(sum_total) - int(sum_list)        
  