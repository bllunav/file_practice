from pathlib import Path
file_path = Path("mobile_model.txt")
model_text = ""

while True:
    model = input("enter model or exit to exit: ")
    if model == "exit":
        print("exited!")
        break
    else:
        model_text += model
        model_text += "\n"


file_path.write_text(model_text)
print(file_path.read_text())