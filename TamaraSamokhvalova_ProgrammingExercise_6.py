import re  # import regular expression module

# Function to validate phone numbers
def validate_phone(phone):
    pattern = r"^(\(\d{3}\)\s?|\d{3}-?)\d{3}-?\d{4}$"
    return re.match(pattern, phone)


# Function to validate Social Security Numbers
def validate_ssn(ssn):
    """
    Valid format:
    123-45-6789
    """
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    return re.match(pattern, ssn)


# Function to validate ZIP codes
def validate_zip(zip_code):
    """
    Valid formats:
    12345
    12345-6789
    """
    pattern = r"^\d{5}(-\d{4})?$"
    return re.match(pattern, zip_code)


# Main function
def main():
    # Get user input
    phone = input("Enter a phone number: ")
    ssn = input("Enter a Social Security Number: ")
    zip_code = input("Enter a ZIP code: ")

    # Validate phone
    if validate_phone(phone):
        print("Phone number is valid")
    else:
        print("Phone number is NOT valid")

    # Validate SSN
    if validate_ssn(ssn):
        print("SSN is valid")
    else:
        print("SSN is NOT valid")

    # Validate ZIP
    if validate_zip(zip_code):
        print("ZIP code is valid")
    else:
        print("ZIP code is NOT valid")


# Run the program
main()