teilnehmer_list = ('Sven', 'Frank', 'Thomas', 'Lena', 'Julia')

counter = 1
for tn in teilnehmer_list:
    print(counter, tn)
    counter += 1

print('~' * 30)
##############################################################
# enumerate ---> tuple (index, value)
for tn in enumerate(teilnehmer_list):
    print(tn)
    print(tn[0], tn[1])
    print()

##############################################################
# enumerate with unpacking
for idx, val in enumerate(teilnehmer_list):
    print(idx, val)
    print()

print('~' * 30)

# enumerate with unpacking and start-number
for idx, val in enumerate(teilnehmer_list, start=100):
    print(idx, val)
    print()
