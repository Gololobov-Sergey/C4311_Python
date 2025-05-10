st = 'm'
st = "програмування на Python 2025"

# for s in st:
#     print(s)
#
#
# print(st[-2])


print(st.upper())
print(st.lower())
print(st.capitalize())
print(st.title())
print(st.count("20", 1, 10))
print(st.startswith("а"))
print(st.endswith("5"))

print(st.find("2"))
print(st.rfind("2"))
# print(st.index("23456"))
print(".jghg".isalnum())
print(".jghg".isalpha())
print(".jghg".isdigit())
print("mama".ljust(20), "papa")
print("mama".rjust(20), "papa")
print("mama".center(20), "papa")

pi = 3.14151293

print(f"{pi:^20.3f}")

m = 12
print(str(m).zfill(2))

import string

print(string.digits)
print(string.ascii_letters)
print(string.punctuation)
print(string.ascii_uppercase)
print(string.ascii_lowercase)


# name = "Голол3453245345обов Се345345345ргій"
# p = name.find(' ')
# name1 = name[p+1:] + " " + name[:p]
# print(name1)

def corrector(string, width, symbol):
    pass

corrector("mama", 10, '+')
# +++mama+++