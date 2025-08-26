def get_classes_needed(total_classes, attended_classes, required_percentage):
    required_classes = (required_percentage / 100) * total_classes
    classes_needed = required_classes - attended_classes
    return max(0, classes_needed)

def get_current_attendance(attended_classes, total_classes):
    if total_classes == 0:
        return 0
    return (attended_classes / total_classes) * 100