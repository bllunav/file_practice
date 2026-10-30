from pathlib import Path
file_path = Path("mobile_brands.txt")
brands = file_path.read_text()
brands += "LG\nMotorola"
file_path.write_text(brands)