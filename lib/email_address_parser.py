import re

class EmailAddressParser:
    def __init__(self, string):
        self.string = string

    def parse(self):
        # Regex pattern to match email addresses
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        # Find all matches
        emails = re.findall(email_pattern, self.string)
        # Return in reverse order
        return emails[::-1]
