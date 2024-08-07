print(" + |", end="")
for top in range(1, 7):
    print(f"{top:3}", end=" ")
print()
print("=" * 27)  # Replace with a cleaner separator if desired

for left in range(1, 7):
    print(f"{left:2} |", end="")
    for top in range(1, 7):
        print(f"{left + top:3}", end=" ")
    print()
# For larger tables, consider using a library like <prettytable> to create more complex and customizable tables.
