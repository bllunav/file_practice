from pathlib import Path
file_path = Path("mobile_brands.txt")
brands = file_path.read_text().rstrip()
brands = brands.splitlines()
brand_text = ""
for i in brands:
    brand_text += i.rstrip()
    brand_text += " "
    print(brand_text)