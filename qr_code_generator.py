import qrcode

# URL to encode
url = "https://nusura-warsaw-web.lovable.app/"

# Generate QR code
qr = qrcode.make(url)

# Save the QR code image
qr.save("nusura_qr_code.png")

print("QR code generated and saved as 'nusura_qr_code.png'.")
