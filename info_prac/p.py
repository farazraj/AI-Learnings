import threading

def odd(nums = (1,2,3,4,5)):
    for i in nums:
        i % 2 !=0
        print(f"Odd:{i}") 


def even(nums = (1,2,3,4,5)):
    for i in nums:
        i % 2 ==0
        print(f"Even:{i}")


t1 = threading.Thread(target=odd)
t2 = threading.Thread(target=even)

t1.start()
t2.start()

t1.join()
t2.join()


 