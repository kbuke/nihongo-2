def validate_instance_numbers(
        model, # The actual model you are putting in eg UserModel
        self, 
        noOfInstances, # The max number of instances you can have eg 7 continents
        instance, # The attribute you are checking against. Passed as key
        value # The value of the instance you are assessing. Passed as value
):
    count = model.query.count()

    if self.id is None and count >= noOfInstances:
        raise ValueError(f"Can not have more than {noOfInstances} {instance}")
    return value