import qrcode

# saving our site's link
website_link = "https://store.steampowered.com/"

# creating QR code
qr_code = qrcode.make(website_link)

# saving with png format
qr_code.save("qr_img.png")

print("Your QR Code was successfully created !")