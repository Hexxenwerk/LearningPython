# Define a single-line string
course_name = "Python Einführung"
print(course_name)

# Define a multi-line string
message = """
Hallo Thomas,
Wie geht es dir?
Schöne Grüße,
Tobias
"""
print(message)

#########################################
# Funktionen (auch für Strings)
print(len(course_name))

# Slicing
course_name = "Einführung in Python"
print(course_name[0])
print(course_name[1])
print(course_name[-1])
print(course_name[0:9])  # Einführun
print(course_name[0:10])  # Einführung
print(course_name[14:20])  # Python
print(course_name[14:2000])  # Python (und kein Fehler)
print(course_name[-20:-10])  # Einführung
print(course_name[-6:])  # Von -6 bis Ende
print(course_name[:10])  # Von 0 bis 9
print(course_name[:])  # Vollständig
print(course_name)  # Vollständig
print(course_name[0:10:2])  # Von 0 bis 9 in 2er Schritten

course_name = 'pyTHoN scHUluNG'
print(course_name.upper())
print(course_name.lower())
print(course_name.title())
print(course_name.capitalize())
print(course_name.find('scH'))
print(course_name.replace('py', 'jy').title())
print(course_name.strip().upper())

#########################################
# String formatting
first_name = 'Thomas'
last_name = 'Maier'

# String concatenation
full_name = first_name + " " + last_name
print(full_name)

# f: format (modern)
print(f'Vorname: {first_name} - Nachname: {last_name}')

# .format()
print('Vorname: {} - Nachname: {}'.format('Sven', 'Meyer'))
print('Vorname: {} - Nachname: {}'.format(first_name, last_name))