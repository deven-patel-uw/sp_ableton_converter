'''

This test script reads the first 1024 bytes of a .SMP file and prints the first 800 bytes (200 samples * 4 bytes/sample) in hexadecimal format. 
This is useful for inspecting the raw data of the .SMP file to verify its contents and structure.

'''


with open(r"C:\Users\dish7\Documents\ROLAND\SP-404MKII\PROJECT_PROJECT_07\SMPL\BANK2-16.SMP", "rb") as f:
    data = f.read(1024)

# show first 800 bytes as hex (200 samples * 4 bytes/sample = 800 bytes)
for i in range(0, 800, 16):
    chunk = data[i:i+16]
    print(f"{i:04x}: " + " ".join(f"{b:02x}" for b in chunk))