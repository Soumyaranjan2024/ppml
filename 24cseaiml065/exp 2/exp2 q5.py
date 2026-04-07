# Create a dictionary and store sample data
student_info = {
    "name": "ashish palo",
    "age": 19,
    "cource": "Computer Science(aiml)",
    "city": "Rayagada"
}
# Display the key-value pairs of the dictionary
print("Student Information:")
for key, value in student_info.items():
    print(f"{key.capitalize()}: {value}")