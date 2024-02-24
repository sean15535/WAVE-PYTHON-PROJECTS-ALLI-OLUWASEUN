a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
d = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
e = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
f = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
g = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
h = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
j = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

account_number_elements = [ a[2:9], b[8:9], c[5:9], d[6:9], e[3:6], f[7:9], g[4:8], h[0:6], i[6:9], j[8:9] ]

user_account = ""

for sublist in account_number_elements:
    if len(sublist) > 0:
        user_account += str(sublist[0])
print("Generated Account Number:", user_account)
print("Welcome to Wema Bank Plc. \nHow may we help you today?")
