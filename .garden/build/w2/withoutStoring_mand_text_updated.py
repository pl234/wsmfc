import json

def func3(format_file_path,input_text_file):

    with open(format_file_path,'r') as file:
        format_data=json.load(file)
    with open(input_text_file,'r') as file:
        ip_data=file.read()
        ip_data=ip_data.replace('\n','')
    with open(input_text_file,'w') as file:
        file.write(ip_data)

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

    with open(input_text_file,'r') as file:
        lines = file.readlines()
        for line in lines:
            key_value_pairs = line.strip().split(',')
            for pair in key_value_pairs:
                key, value = pair.split(':')
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
    
