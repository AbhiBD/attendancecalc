import math

def get_classes_needed(total_classes, attended_classes, required_percentage):
    required_classes = (required_percentage / 100) * total_classes
    classes_needed = required_classes - attended_classes
    classes_needed = int(math.ceil(classes_needed))
    return max(0, classes_needed)

def get_current_attendance(attended_classes, total_classes):
    if total_classes == 0:
        return 0
    return (attended_classes / total_classes) * 100

def get_required_classes(total_classes, required_percentage):
    required_classes = (required_percentage / 100) * total_classes
    required_classes = int(math.ceil(required_classes))
    return max(0, required_classes)

def get_missable_classes(total_classes,attended_classes, required_percentage,missed_classes):
    required_classes = (required_percentage / 100) * total_classes
    classes_needed = required_classes - attended_classes
    classes_needed = int(math.ceil(classes_needed))
    missable_classes = total_classes-classes_needed-attended_classes-missed_classes
    if missable_classes >= 0:
        
        return(max(0, missable_classes))
    
    else:
        return -1