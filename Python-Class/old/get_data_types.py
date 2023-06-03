import ast

def get_data_types(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
    root = ast.parse(code)

    data_types = set()
    for node in ast.walk(root):
        if isinstance(node, ast.Call) and hasattr(node.func, 'id'):
            if node.func.id in ['int', 'float', 'str', 'list', 'dict', 'tuple', 'set', 'bool']:
                data_types.add(node.func.id)

    return data_types


data_types = get_data_types('Security_Tool4.py')

print(data_types)