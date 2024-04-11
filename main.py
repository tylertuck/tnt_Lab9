def encode(num):
    ans=num+3
    return ans

def main():
    storeNum = None
    menu=True
    while menu:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            encodedNum=""
            password = input("Please enter your password to encode: ")
            storeNum = int(password)
            for num in password:
                encodedNum+=str(encode(int(num)))
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            print("The encoded password is "+encodedNum +", and the original password is "+password+".\n")
        elif choice == 3:
            menu=False


if __name__ == "__main__":
    main()
