from PIL import Image
import os

img_path = r'C:\Users\Douglas\.gemini\antigravity\brain\86ccf904-ff87-4fa2-a7aa-2d8ac1d2691c\.user_uploaded\media_1789190997743.png'
dest_dir = r'c:\Users\Douglas\Desktop\Oferta que vai deixar eu rico'

img = Image.open(img_path)
w, h = img.size

# Slicing into 3 columns
w3 = w // 3

# Cropping the 3 cards
card1 = img.crop((0, 0, w3, h))
card2 = img.crop((w3, 0, w3*2, h))
card3 = img.crop((w3*2, 0, w, h))

card1.save(os.path.join(dest_dir, 'aula1.png'))
card2.save(os.path.join(dest_dir, 'aula2.png'))
card3.save(os.path.join(dest_dir, 'aula3.png'))
print('Images cropped successfully.')
