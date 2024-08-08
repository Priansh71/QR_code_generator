import qrcode
 
with open('urls.txt') as file:
#The urls.txt file is read line by line, and each URL is stored in the lines list.
  urls = file.readlines()
  count = 1
  for line in lines:
    img = qrcode.make(urls)
    img.save(f"{count}.png")
    count += 1
#The loop in the code ends when it has iterated over all the lines in the lines list.

# OR #

import qrcode

with open('urls.txt', 'r') as file:
    urls = file.read().splitlines()

for i, url in enumerate(urls, start=1):
    img = qrcode.make(url)
    img.save(f'qr_code_{i}.png')
    print(f"QR code for {url} saved as qr_code_{i}.png")


