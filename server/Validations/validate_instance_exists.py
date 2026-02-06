def validate_instance_exists(
    model, # actual model eg UserModel
    value, # value always the id you are checking ie checking continent_id 1 exists
    key # The attribute you check the value against
):
    exists = model.query.get(value)

    if not exists:
        raise ValueError(f"{key} {value} does not exist")
    
    return value