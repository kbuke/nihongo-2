def validate_id_int(
    value, # value you are assesing
    key # the attribute (key) you are assessing it against
):
    # This is to ensure in relationships, the id is entered correctly
    try:
        return int(value)
    except Exception:
        raise ValueError(f"{key} must be a valid integer")