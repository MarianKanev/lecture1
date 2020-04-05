# Define own function

def square(x):
    return x * x

def main():
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))

if __name__ == "__main__":
    main()
    
# The result is
# 0 squared is 0
# 1 squared is 1
# 2 squared is 4
# 3 squared is 9
# 4 squared is 16
# 5 squared is 25
# 6 squared is 36
# 7 squared is 49
# 8 squared is 64
# 9 squared is 81