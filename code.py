import sys, os, json, re

def find_subdirs_with_string(dir_array, target_string, search_depth):
    items_array = []
    for dir_path in dir_array:
        for root, dirs, files in os.walk(dir_path, topdown=True):
            # Check if current depth is greater than num_search_depth
            if root[len(dir_path):].count(os.path.sep) > search_depth - 1:
                # If so, remove subdirectories from traversal
                del dirs[:]
            
            for subdir in dirs:
                search_dir = subdir
                if "/" in target_string:
                    # Start search dir
                    fullpath = os.path.join(root, subdir)
                    search_dir = re.sub(rf"^{re.escape(dir_path)}", "", fullpath)

                if target_string in search_dir:
                    fullpath = os.path.join(root, subdir)
                    item = {"uid": fullpath, "type": "file", "title": fullpath, "arg": fullpath, "icon": {"type": "fileicon", "path": fullpath}}
                    items_array.append(item)

    return items_array

# Get dir array from env
dir_array = os.getenv("DIR_ARRAY").split(":")

# Get search depth from env
str_search_depth = os.getenv("SEARCH_DEPTH")
num_search_depth = 2
if str_search_depth is not None:
    try:
        num_search_depth = int(str_search_depth)
    except ValueError:
        print(f"{str_search_depth} not a valid integer")

target_string = "{query}"
items_array = find_subdirs_with_string(dir_array, target_string, num_search_depth)

result = {"items": items_array}
json_str = json.dumps(result, ensure_ascii=False)
print(json_str)
