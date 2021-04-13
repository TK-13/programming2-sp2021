import csv
import matplotlib.pyplot as plt
import numpy as np

# open the csv file (https://www.kaggle.com/mirichoi0218/insurance)
insurance_data = open("../../Resources/insurance.csv")
insurance_data = csv.DictReader(insurance_data)

# read the contents into lists
insurance_data = list(insurance_data)

plt.figure(1)

# plot yes data
xs_yes = [float(data['age']) for data in insurance_data if data['smoker'] == 'yes']
ys_yes = [float(data['charges']) for data in insurance_data if data['smoker'] == 'yes']
plt.scatter(xs_yes, ys_yes, s=5, c='red', label='smoker')  # change s value for large dots

# plot no data
xs_no = [float(data['age']) for data in insurance_data if data['smoker'] == 'no']
ys_no = [float(data['charges']) for data in insurance_data if data['smoker'] == 'no']
plt.scatter(xs_no, ys_no, s=5, c='blue', label='non smoker')  # change s value for large dots


xs_best_fit = [x for x in range(50)]

# find and plot yes best fit line
yes_fit = np.polyfit([int(x) for x in xs_yes], [int(y) for y in ys_yes], 1)
ys_yes_best_fit = [yes_fit[0] * x + yes_fit[1] for x in xs_best_fit]
plt.plot(xs_best_fit, ys_yes_best_fit, label='smoker', color='red')

# find and plot no best fit line
no_fit = np.polyfit([int(x) for x in xs_no], [int(y) for y in ys_no], 1)
ys_no_best_fit = [no_fit[0] * x + no_fit[1] for x in xs_best_fit]
plt.plot(xs_best_fit, ys_no_best_fit, label='non smoker', color='blue')

# add plot details
plt.title('Age vs Insurance Charges')
plt.xlabel("age")
plt.ylabel("Insurance Charges")
plt.legend()

plt.figure(2)

# plot female data
xs_female = [float(data['bmi']) for data in insurance_data if data['sex'] == 'female']
ys_female = [float(data['charges']) for data in insurance_data if data['sex'] == 'female']
plt.scatter(xs_female, ys_female, s=5, c='red', label='female')  # change s value for large dots

# plot male data
xs_male = [float(data['bmi']) for data in insurance_data if data['sex'] == 'male']
ys_male = [float(data['charges']) for data in insurance_data if data['sex'] == 'male']
plt.scatter(xs_male, ys_male, s=5, c='blue', label='male')  # change s value for large dots


xs_best_fit = [x for x in range(50)]

# find and plot yes best fit line
female_fit = np.polyfit([int(x) for x in xs_female], [int(y) for y in ys_female], 1)
ys_female_best_fit = [female_fit[0] * x + female_fit[1] for x in xs_best_fit]
plt.plot(xs_best_fit, ys_female_best_fit, label='female', color='red')

# find and plot no best fit line
male_fit = np.polyfit([int(x) for x in xs_male], [int(y) for y in ys_male], 1)
ys_male_best_fit = [male_fit[0] * x + male_fit[1] for x in xs_best_fit]
plt.plot(xs_best_fit, ys_male_best_fit, label='male', color='blue')

# find and plot the intersection of the two best fit lines
def find_intersection(m1, b1, m2, b2):
    x = (b2-b1)/(m1-m2)
    y = m1*x + b1
    return x, y


x, y = find_intersection(male_fit[0], male_fit[1], female_fit[0], female_fit[1])
plt.annotate("({0}, {1})".format(round(x), round(y)), xy=(x, y), size=15)
plt.scatter([x], [y], s=70, color="orange")

# add plot details
plt.title('BMI vs Insurance Charges')
plt.xlabel("BMI")
plt.ylabel("Insurance Charges")
plt.legend()

plt.show()


