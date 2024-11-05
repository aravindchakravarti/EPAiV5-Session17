from collections import defaultdict

def merge_with_defaultdict(*arg_dicts):
    merge_dict = defaultdict(int)
    for args in arg_dicts:
        for key, value in args.items():
            merge_dict[key] = merge_dict[key] + value
    
    return merge_dict

def merge_with_counter():
    pass