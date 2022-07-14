readable_files = {"c":"#ff0000","cpp":"#ff0000","cxx":"#0000ff","h":"#00ff00"}

COLORBYEXTENSION = 1
COLORBYLOCATION = 2

def coloring_by_extension(node):
    ext = node["id"].slip(".")[-1]
    if ext in readable_files:
        return readable_files[ext]
    else:
        return "#ff00ff"

def coloring_by_location(node):
    path = node["title"].split("\\")
    depth = 0
    for x in path:
        depth = depth + 1000
    return hex(1000)

def coloring(node,type = COLORBYEXTENSION):
    if type == COLORBYLOCATION:
        return coloring_by_location(node)
    return coloring_by_extension(node) 
        