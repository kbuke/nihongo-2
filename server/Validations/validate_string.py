def validate_string(
    value,
    field_name = "Value"
):
    # 1 - Reject Booleans, None
    if isinstance(value, bool) or value is None or value.strip() == "":
        raise ValueError(f"{field_name} must be a valid string")
    
    # 2 - Convert to string if it is not a string, Boolean None or empty string
    if not isinstance(value, str):
        try:
            value = str(value)
        except Exception:
            raise ValueError(f"{field_name} must be a string")
        
    # 3 - Ensure no empty or white-space strings
    value = value.strip()
    if value == "":
        raise ValueError(f"{field_name} can not be an empty string")
    
    return value