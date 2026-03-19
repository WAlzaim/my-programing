
# I am using the dummy student ID you specified earlier:
#Student ID = 2542674
#d1 = 1
#d2 = 0
#k = (1 + 0) % 4 + 2 = 3
#shift = 1 - 0 = 1
#rows_keep = (1 % 2) + 2 = 3
#So all personalized outputs below use:
#k = 3
#shift = 1
#rows_keep = 3
#

def main():
    d1 = 1
    d2 = 0
    k = 3
    shift = 1
    rows_keep = 3

    readings = [10.5, 12.0, 9.5, 15.0]

    print("Original readings:", readings)

    if len(readings) > 0:
        print("First reading:", readings[0])
        print("Last reading:", readings[-1])
    else:
        print("The list is empty.")

    if len(readings) >= 4:
        print("Slice from index 1 to index 3:", readings[1:4])
    else:
        print("Not enough values for slice [1:4].")

    total = sum(readings)
    print("Sum of readings:", total)

    shifted = [x + shift for x in readings]
    scaled = [x * k for x in readings]
    zipped_sum = [a + b for a, b in zip(readings, shifted)]

    print("Shifted readings:", shifted)
    print("Scaled readings:", scaled)
    print("Element-wise sum of original and shifted:", zipped_sum)

    print("\nManual check for first 3 elements:")
    for i in range(3):
        print(f"Original={readings[i]}, Shifted={shifted[i]}, Scaled={scaled[i]}, ZipSum={zipped_sum[i]}")


if __name__ == "__main__":
    main()