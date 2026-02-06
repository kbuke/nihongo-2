import re 

def validate_email(
    value
):
    # regex patterns for legitimate emails
    email_pattern = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$" 

    if not re.match(email_pattern, value):
        raise ValueError("Please enter a valid Email Address")
    
    return value