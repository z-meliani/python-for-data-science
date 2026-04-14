
def NULL_not_found(object: any) -> int:
    name = 0

    match object:
        case None:
            name = "Nothing"
        case False:
            name = "Fake"
        case 0:
            name = "Zero"
        case "":
            name = "Empty"
        case _ if (isinstance(object, float) and object != object):
            name = "Cheese"

    if name:
        print(f"{name}: {object} {type(object)}")
    else:
        print("Type not Found")

    return 1
