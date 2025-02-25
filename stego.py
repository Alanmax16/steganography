import cv2
import os

# Read image (ensure correct path)
img = cv2.imread("C:/Users/AlanM/Downloads/New folder 1/Stenography-main/Stenography-main/catimage.jpg")
if img is None:
    print("Error: Image not found.")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Character mappings
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Image dimensions
height, width, _ = img.shape
max_chars = height * width * 3  # Maximum chars that can be stored

if len(msg) > max_chars:
    print("Error: Message too long for the image.")
    exit()

# Encode message in image
n, m, z = 0, 0, 0
for char in msg:
    img[n, m, z] = d[char]
    z += 1
    if z == 3:
        z = 0
        m += 1
        if m == width:
            m = 0
            n += 1

# Save and open encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")

# Decryption
message = ""
n, m, z = 0, 0, 0
pas = input("Enter passcode for Decryption: ")

if password == pas:
    for _ in range(len(msg)):
        message += c[img[n, m, z]]
        z += 1
        if z == 3:
            z = 0
            m += 1
            if m == width:
                m = 0
                n += 1
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
