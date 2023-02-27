import os

filename = "/home/malik/Musik/output.txt" # write the directory you want to put the text file

# Open the output file in write mode
with open(filename, "w") as f:
    # Write all lines to the output file
    for i in range(1, 10000):
        s = str(i).zfill(4)  # Fill up zeros to get a X-digit number (where the 4 is)
        f.write(f"DELAY 500\nSTRING {s}\nENTER\n")
        f.write(f"DELAY 500\nSTRING {str(i + 1).zfill(4)}\nENTER\n")

# Run the bash script that executes the output.txt file
os.system(f"bash {filename}")
