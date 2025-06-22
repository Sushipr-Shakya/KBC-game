print("Hello World")

def fact(n):
    if (n>0) :
        i = 1
        facto=1
        while (i<=n):
            facto*=i
            i+=1
        print (facto)    
    elif (n==0):
        print(1)
    else :
        print ("Factorials are not defined for negative integers.")           

a = int ( input ("Enter a number :"))
fact(a)

#Checking whether a given num is even-odd by functions:
def even_odd (n):
    if (n%2==0):
        print("Even")
    else:
        print("Odd")  

even_odd(a)          

#Functions combined with List Comprehensions:->
#To find the factorials of the elements in a list.

def fact_of_list(list):                           
    fact_of_num = [fact(n) for n in list]              #Doubt
    print(fact_of_num)
    
fact_of_list([1,2,3,4,5])


#List Comprehensions
list = [1,2,3,4,5]

print([n**2 for n in list])

def sum_of_list_elem(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    return sum

#Functions giving 2 values:-->
def calc_mean_median(list):
    #for mean:-->
    mean = sum_of_list_elem(list) / len(list)
    
    #for median:-->
    sorted_list = sorted(list)
    
    if len(list)%2==0 :
        len(list)/2                               # {(n/2)th + ((n/2) +1)th obs}/2


list_of_even = [2,4,6,8,10]

calc_mean_median(list_of_even)