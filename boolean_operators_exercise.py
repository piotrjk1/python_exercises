is_student = input("Are you student? (y/n): ")
if is_student == "y":
    is_student = True
else:
    is_student = False

has_pets = input("Do you have pets? (y/n): ")
if has_pets == "y":
    has_pets = True
else:
    has_pets = False
    
is_smoking = input("Do you smoke? (y/n): ")
if is_smoking == "y":
    is_smoking = True
else:
    is_smoking = False
    
property_available = False

PROPERTY_AVAILABLE_MSG = "Property available"
PROPERTY_UNAVAILABLE_MSG = "Property unavailable"

if is_student:
    if not has_pets and not is_smoking:
        property_available = True
else:
    if (has_pets and not is_smoking) or (not has_pets and is_smoking):
        property_available = True

if property_available:
    print(PROPERTY_AVAILABLE_MSG)
else:
    print(PROPERTY_UNAVAILABLE_MSG)

print("Program finished")
