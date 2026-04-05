# lab8.py
# Student Id: 2542674
# Personalized values
d1 = 4
d2 = 7
k = 5
shift = -3
rows_keep = 2

import csv
import math
import os

# Create data folder
DATA_FOLDER = "Lab8_Data"
os.makedirs(DATA_FOLDER, exist_ok=True)

# -----------------------------
# Component A: Read CSV files
# -----------------------------
def read_oscillatory_wave_data(filename):
    amplitudes = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # skip header
        for row in reader:
            amplitudes.append(float(row[1]))
    mean_amp = sum(amplitudes)/len(amplitudes)
    max_amp = max(amplitudes)
    print(f"Oscillatory Wave ({filename}):")
    print(f"  Mean Amplitude = {mean_amp}")
    print(f"  Max Amplitude = {max_amp}\n")
    return mean_amp, max_amp

def read_standing_wave_data(filename):
    speeds = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # skip header
        for row in reader:
            tension = float(row[1])
            v = math.sqrt(tension/1)  # μ = 1
            speeds.append(v)
    print(f"Standing Wave ({filename}):")
    print("  Wave Speeds =", [round(s,2) for s in speeds], "\n")
    return speeds

# -----------------------------
# Component B: Create personalized files
# -----------------------------
def create_personalized_oscillatory_file(original, newfile):
    rows = []
    with open(original, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for i,row in enumerate(reader):
            if i >= 5 + d2:
                break
            length = float(row[0])
            amplitude = float(row[1]) + shift
            rows.append([length, amplitude])
    with open(newfile, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(rows)
    return read_oscillatory_wave_data(newfile)

def create_personalized_standing_file(original, newfile):
    rows = []
    with open(original, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for i,row in enumerate(reader):
            if i >= 4 + rows_keep:
                break
            length = float(row[0])
            tension = float(row[1]) * k
            rows.append([length, tension])
    with open(newfile, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(rows)
    return read_standing_wave_data(newfile)

# -----------------------------
# Helper: Generate sample CSV files
# -----------------------------
def generate_sample_files():
    osc_file = os.path.join(DATA_FOLDER, "oscillatory_2542674.csv")
    stand_file = os.path.join(DATA_FOLDER, "standing_2542674.csv")

    # Create sample oscillatory file if it doesn't exist
    if not os.path.exists(osc_file):
        with open(osc_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["time","amplitude"])
            for i in range(10):
                writer.writerow([i*0.1, i*0.2])
    
    # Create sample standing wave file if it doesn't exist
    if not os.path.exists(stand_file):
        with open(stand_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["length","tension"])
            for i in range(5):
                writer.writerow([i, (i+1)*10])

    return osc_file, stand_file

# -----------------------------
# Main function
# -----------------------------
def main():
    osc_file, stand_file = generate_sample_files()

    # Read original files
    read_oscillatory_wave_data(osc_file)
    read_standing_wave_data(stand_file)

    # Create personalized files
    create_personalized_oscillatory_file(osc_file, os.path.join(DATA_FOLDER, "osc_new.csv"))
    create_personalized_standing_file(stand_file, os.path.join(DATA_FOLDER, "stand_new.csv"))

if __name__ == "__main__":
    main()