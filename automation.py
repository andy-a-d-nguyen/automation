import re


def get_phone_numbers(file_lines):
    for line in file_lines:
        for phone_number_regex_pattern in phone_number_regex_patterns:
            pattern = re.compile(phone_number_regex_pattern)
            phone_number_matches = pattern.findall(line)
            match phone_number_regex_pattern:
                case r"\d{10}":
                    for phone_number_match in phone_number_matches:
                        phone_numbers.append(
                            phone_number_match[0:3] + "-" +
                            phone_number_match[3:6] + "-" +
                            phone_number_match[6:]
                        )
                case r"\d{3}-\d{3}-\d{4}":
                    for phone_number_match in phone_number_matches:
                        phone_numbers.append(phone_number_match)
                case r"\(\d{3}\)\d{3}-\d{4}":
                    for phone_number_match in phone_number_matches:
                        phone_numbers.append(
                            phone_number_match[1:4] + "-" +
                            phone_number_match[5:8] + "-" +
                            phone_number_match[9:]
                        )
                case r"\d{3}\.\d{3}\.\d{4}":
                    for phone_number_match in phone_number_matches:
                        phone_numbers.append(
                            phone_number_match[0:3] + "-" +
                            phone_number_match[4:7] + "-" +
                            phone_number_match[8:]
                        )


def get_emails(file_lines):
    for line in file_lines:
        pattern = re.compile(email_regex_pattern)
        email_matches = pattern.findall(line)
        for email_match in email_matches:
            emails.append(email_match)


phone_number_regex_patterns = [
    r"\d{10}",  # 5599662227
    r"\d{3}-\d{3}-\d{4}",  # 693-728-3320
    r"\(\d{3}\)\d{3}-\d{4}",  # (896)573-1016
    r"\d{3}\.\d{3}\.\d{4}"  # 087.879.4133
]

email_regex_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

phone_numbers = []

emails = []

with open("assets/potential-contacts.txt", "r") as file:
    lines = file.readlines()
    get_phone_numbers(lines)
    get_emails(lines)

unique_phone_numbers = set(phone_numbers)

sorted_phone_numbers = sorted(unique_phone_numbers)

unique_emails = set(emails)

sorted_emails = sorted(unique_emails)

with open("phone_numbers.txt", "w") as file:
    for phone_number in sorted_phone_numbers:
        file.write(phone_number)
        file.write("\n")

with open("emails.txt", "w") as file:
    for email in sorted_emails:
        file.write(email)
        file.write("\n")
