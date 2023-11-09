def all_thing_is_obj(object: any) -> int:
    if type(object) == str : 
        print(f"{object} is in the kitchen : {type(object)}")
    elif type(object).__name__ in ['int', 'float', 'bool', 'NoneType']: 
        print("Type not found")
    else : 
        print(f"{type(object).__name__.capitalize()} : {type(object)}")
    return 42