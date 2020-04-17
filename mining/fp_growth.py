import pyfpgrowth

from data.data_loader import load_data

transactions = load_data()
sup = 0.055  # float(input("Enter support %: "))
patterns = pyfpgrowth.find_frequent_patterns(transactions, int(len(transactions) * sup))
for k, v in patterns.items():
    print(k, v)
print(len(patterns))
rules = pyfpgrowth.generate_association_rules(patterns, 0.00001)
print(rules)
print(len(rules))
