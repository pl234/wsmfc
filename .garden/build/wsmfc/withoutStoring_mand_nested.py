import json

def func2(format_file_path,user_file_path):
    with open(format_file_path,'r') as file:
        format_data=json.load(file)
    with open(user_file_path,'r') as file:
        user_data=json.load(file)
    def is_key(word, data):
        list = [(key, value) for key, value in data.items()]
        while list:
            key, value = list.pop()
            if isinstance(value, dict):
                for k, v in value.items():
                    if k == word:
                        return True, key
                    list.append((k, v))
            elif key == word:
                return True, None
        return False, None
    
    def process_user_input(user_data,new_data):
        for key,value in user_data.items():
            if isinstance(value,dict):
                process_user_input(value,new_data)
            else:
                present,nested_key = is_key(key,format_data)
                if present:
                    if nested_key:
                        if nested_key not in new_data:
                            new_data[nested_key] = {}
                        new_data[nested_key][key] = value
                    else:
                        new_data[key]=value
                    
                else:
                    if 'metadataMap' not in new_data:
                        new_data['metadataMap'] = {}
                    new_data['metadataMap'][key] = value

    new_data={}    
    process_user_input(user_data,new_data)
    return new_data









# def process_user_input(user_data, new_data):
#         for key, value in user_data.items():
#             if isinstance(value, dict):
#                 new_data.setdefault(key, {})
#                 process_user_input(value, new_data[key])
#             else:
#                 present, nested_key = find_key(key, format_data)
#                 if present:
#                     if nested_key:
#                         new_data.setdefault(nested_key, {})
#                         new_data[nested_key][key] = value
#                     else:
#                         new_data[key] = value
#                 else:
#                     new_data.setdefault('metadataMap', {})
#                     new_data['metadataMap'][key] = value

#     new_data = {}
#     process_user_input(user_data, new_data)
#     return new_data