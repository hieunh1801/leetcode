"""
https://leetcode.com/problems/defanging-an-ip-address/

input:  address = "1.1.1.1"
output: "1[.]1[.]1[.]1"
"""


def defangIPaddr(address: str) -> str:
    arr_num_of_address: list = address.split(".")
    separator = "[.]"
    defang_address = separator.join(arr_num_of_address)
    return defang_address


def defangIPaddr2(address: str) -> str:
    return address.replace(".", "[.]")


if __name__ == "__main__":
    address = "1.1.1.1"
    defangIPaddr(address=address)
