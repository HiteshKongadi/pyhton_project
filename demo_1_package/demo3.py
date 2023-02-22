data = "Hello world"
for i in data:
    print(i)

print(data[0::2])
print(data[-5:])

for a in data[0::2]:
    print(a)


mail_id = "john.dev@gmail.com"
print(mail_id[:mail_id.index("@")])

print((mail_id.split("@")))