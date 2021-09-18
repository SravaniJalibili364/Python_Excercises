def histogram(input_list):

    for num in input_list:
        print(num * "#")
    


input_list = list(map(int,input().split()))
histogram(input_list)
