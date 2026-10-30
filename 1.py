from pathlib import Path
file_path = Path("mobile_brands.txt")
brands = file_path.read_text()
brands = brands.splitlines()
for i in brands:
    print(f"brand: {i}\ncharacters: {len(i)}")