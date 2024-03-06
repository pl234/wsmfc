# code for not creating and stored data in new_file_path i.e., mergeCodeOP.json

import json

format_file_path=r"C:\Users\101798\OneDrive - UNIPHORE SOFTWARE SYSTEMS PVT LTD\folder_mand_files\FORMAT.json"
user_file_path=r"C:\Users\101798\OneDrive - UNIPHORE SOFTWARE SYSTEMS PVT LTD\folder_mand_files\user1.json"

def func1(format_file_path,user_file_path):
    with open(format_file_path,'r') as file:
        format_data=json.load(file)
    with open(user_file_path,'r') as file:
        user_data=json.load(file)
    def is_key(word, format_data, parent_key=None):
        for key, value in format_data.items():
            if isinstance(value, dict):
                if key == word:
                    return True, parent_key
                found, nested_obj = is_key(word, value, key)
                if found:
                    return True, nested_obj
            elif key == word:
                return True, parent_key
        return False, parent_key
    new_data={}
    for key,value in user_data.items():
        present,nested_key = is_key(key,format_data,parent_key=None)
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

    return new_data


# with open('withoutStore_mandOP.json','w') as file:
#     json.dump(new_data,file,indent=4)









    # def find_key(word, data):
    #     stack = [(key, value) for key, value in data.items()]
    #     while stack:
    #         key, value = stack.pop()
    #         if isinstance(value, dict):
    #             for k, v in value.items():
    #                 if k == word:
    #                     return True, key
    #                 stack.append((k, v))
    #         elif key == word:
    #             return True, None
    #     return False, None