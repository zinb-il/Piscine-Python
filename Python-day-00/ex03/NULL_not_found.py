def NULL_not_found(object: any) -> int:
    if not (isinstance(object, float) and str(object).lower() == "nan") and object:
        print("Type not Found")
        return 1
    if object is None : print("Nothing:", end="")
    elif isinstance(object, float) and str(object).lower() == "nan" : print("Cheese:", end="")
    else:
        match type(object).__name__:
            case "float": print("Zero:", end="")
            case "int": print("Zero:", end="")
            case "str" : print("Empty:", end="")
            case "bool" : print("Fake:", end="")
            case default: print("Squence:", end="")
    print(f" {object} {type(object)}")
    return 0
    
