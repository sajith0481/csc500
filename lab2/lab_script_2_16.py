key_frequency = float(input("Enter the frequency of the key: "))

your_value2 = key_frequency * pow(2, 1/12)
your_value3 = key_frequency * pow(2, 2/12)
your_value4 = key_frequency * pow(2, 3/12)
your_value5 = key_frequency * pow(2, 4/12)

print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(key_frequency, your_value2, your_value3, your_value4, your_value5))