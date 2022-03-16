gewicht = float(input('Gib dein Körpergewicht in kg an: '))
groesse = float(input('Gib deine Körpergröße in m an: '))

bmi = gewicht / groesse ** 2

print(f'Dein BMI liegt bei: {bmi:.2f}')
