import json
from pathlib import Path

weather_info = {
    "city": "Isfahan",
    "temp": 24,
    "status": "sunny"
}

file_path = Path("weather.json")
json_data = json.dumps(weather_info, indent = 4)
file_path.write_text(json_data)
print("data saved successfully!")

try:
    raw_text = file_path.read_text()
    data = json.loads(raw_text)
    print(f"City: {data["city"]}")
    print(f"Current tempreture: {data["temp"]}C")
except FileNotFoundError:
    print("File Not Found!")