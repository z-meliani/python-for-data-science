def all_thing_is_obj(object: any) -> int:

    if type(object) in [list, set, tuple, dict]:
        print(f"{type(object).__name__.capitalize()} : {type(object)}")
    elif type(object) is str:
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")

    return 42
