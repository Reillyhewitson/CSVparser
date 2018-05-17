import csv
no = 0
csvfile = open('test.csv','w+').close()
headers = int(input('How many columns will you have?'))
header = []
body = []
spamwriter = csv.writer(csvfile, dialect='excel')
print(spamwriter)
for i in range(1,headers + 1):
    print('This is header', str(i)+'. What do you want to call it?')
    value = str(input())
    header.append(value)
    header.append(',')
print(header)
csvfile.write(''.join(header)+'\n')
while True:
    try:
        print('This will be in column',header[no])
        value = str(input())
        no += 2
        body.append(value)
        body.append(',')
        while (len(header)) <= no:
            no = 0
            csvfile.write(''.join(body)+'\n')
            body = []
        print(body)
    except KeyboardInterrupt:
        break
csvfile.close()

