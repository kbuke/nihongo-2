def exclude_info(relation, *fields):
    return tuple(f"-{relation}.{field}" for field in fields)