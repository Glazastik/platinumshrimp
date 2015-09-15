
import json
import os.path

# Helper method for reading json and envoding data to UTF-8
def read_json(filename):
    def encode_dict(data):
        if type(data) == dict:
            return dict(map(encode_dict, pair) for pair in data.items())
        #elif type(data) == unicode:
        #    return data.encode('utf-8')
        else:
            return data
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            return json.load(f, object_hook=encode_dict)

