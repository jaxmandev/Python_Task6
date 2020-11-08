class AccountHolderDetails:
    def __init__(self, name, address, age):
        self.__name = name
        self.__address = address
        self.__age = age

    # property prevents editing of key user information
    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    @property
    def age(self):
        return self.__age

    # displaying user account details
    def display_account_details(self):
        print("")
        print("="*20)
        print(f"Name: {self.__name}")
        print(f"Address: {self.__address}")
        print(f"Age: {self.__age}")
        print("=" * 20)
        print("")
