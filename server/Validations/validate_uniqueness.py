def validate_uniqueness(
    value,
    self,
    model,
    key,
    field_name = "Value" # Can change it to unqiue text such as "Continent" does not always have to be "Value"
):
    # 1 - Check value exists in the model
    column = getattr(model, key)

    existing_value = model.query.filter(column == value).first()

    if existing_value and existing_value.id != self.id:
        raise ValueError(f"{field_name} already has {value} registered under {key}")
    
    return value