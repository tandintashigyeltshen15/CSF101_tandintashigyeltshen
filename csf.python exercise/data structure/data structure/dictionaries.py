name = "tandin"  # Use the same name as in strings.py
age = 18  # Use the same age as in numbers.py
height = 1.75  # Use the same height as in numbers.py
is_student = True  # Use the same value as in booleans.py

person_info = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student
}
print(person_info)
person_info["favorite_color"] = "green"
print(person_info)
try:
    print(person_info["weight"])
except KeyError as e:
    print(f"Error: {e}")


