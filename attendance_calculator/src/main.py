from utils import get_classes_needed, get_current_attendance, get_required_classes, get_missable_classes

def main():
    subject_name = input("Enter the subject name: ")
    total_classes = int(input("Enter the total number of classes: "))
    attended_classes = int(input("Enter the number of classes attended: "))
    missed_classes = int(input("Enter the total number of classes you have missed as is: "))
    required_percentage = float(input("Enter the required attendance percentage: "))
    

    current_attendance = get_current_attendance(attended_classes, total_classes)
    classes_needed = get_classes_needed(total_classes, attended_classes, required_percentage)
    required_classes = get_required_classes(total_classes, required_percentage)
    missable_classes = get_missable_classes(total_classes, attended_classes, required_percentage, missed_classes)

    print("\nSubject: {}".format(subject_name))
    print("Number of classes required to achieve {}% attendance : {}".format(required_percentage,required_classes))
    print("Current Attendance: {:.2f}%".format(current_attendance))
    print("Classes needed to maintain {}% attendance: {}".format(required_percentage, classes_needed))

    if missable_classes >= 0:
        print("Number of classes you could miss and still achieve required attendance percentage : {}".format(missable_classes))
    else:
        print("You will not be able to achieve requiured percentage with your current attendance metric. Consider other methods.")

if __name__ == "__main__":
    main()