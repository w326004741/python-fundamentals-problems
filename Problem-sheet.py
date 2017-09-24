#Problems-Sheet-Python
1. print('Hello,world!')

2. import datetime
   now = datetime.datetime.now()
   print ("Current date and time: ")
   print (now.strftime("%Y-%m-%d %H:%M:%S"))
/  import time
   print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

3. for n in range(1,21):
    string = ""
    if n % 3 == 0:
        string = string + "Fizz"
    if n % 5 == 0:
        stirng = string + "Buzz"
    if n % 5 != 0 and n % 3 != 0:
        string = string  + str(n)
    print(string)

4. 