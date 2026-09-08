# Attendance Percentage Calculator

total_classes = int(input("Enter total number of classes: "))
attended_classes = int(input("Enter number of classes attended: "))

attendance = (attended_classes / total_classes) * 100

print("Attendance Percentage:", attendance, "%")