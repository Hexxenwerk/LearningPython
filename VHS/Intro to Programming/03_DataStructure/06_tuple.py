# Tuples are read-only container (list)

teilnehmer_tuple = ('Sven', 'Frank', 'Thomas', 'Lena', 'Julia')
mixed_data = ('Thomas', 45, True, 36.9)

print(teilnehmer_tuple, type(teilnehmer_tuple))
print(mixed_data, type(mixed_data))

# Loop
for tn in teilnehmer_tuple:
    print(tn)

# Slicing
print(teilnehmer_tuple[0])
print(teilnehmer_tuple[-1])

# Change tuple --> NOT possible
##############################################################
# Indirect change via new create
print(teilnehmer_tuple)
teilnehmer_tuple = ('Sara', 'Lena', 'Julia', 'Frank', 'Julia')
print(teilnehmer_tuple)

##############################################################
# Indirect change vie conversion
teilnehmer_tuple = ('Thomas', 'Ingo', 'Sven')
tmp_list = list(teilnehmer_tuple)
tmp_list.append('Bernd')
tmp_list.append('Mikey')
teilnehmer_tuple = tuple(tmp_list)
print(teilnehmer_tuple)
