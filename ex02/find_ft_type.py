def all_thing_is_obj(obj: any) -> int:
    if(type(obj).__name__ == 'list'):
        print(f"List : {type(obj)}")
    elif(type(obj).__name__ == 'tuple'):
        print(f"Tuple : {type(obj)}")
    elif(type(obj).__name__ == 'set'):
        print(f"Set : {type(obj)}")
    elif(type(obj).__name__ == 'dict'):
        print(f"Dict : {type(obj)}")
    elif(type(obj).__name__ == 'str'):
        print(f"{obj} is in the kitchen : {type(obj)}")
    else:
        print("Type not found")
    return 42