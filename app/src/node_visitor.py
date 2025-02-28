import ast 
from node_visit_interface import NodeVisitInterface

class NodeVisitor(ast.NodeVisitor): 
    
    def __init__(self, node_visit_listener: NodeVisitInterface): 
        self.node_visit_listener = node_visit_listener

    def visit_FunctionDef(self, node):
        # Notify any listener that the function def was found
        self.node_visit_listener.on_visit_func_def(node.name)

        # visit the reset of the nodes 
        # as we are overwriting the custom 
        # visit for this specific node type 
        super().generic_visit(node) 

    def visit_Call(self, node):
        # if the function is called directly, e.g. foo()
        if isinstance(node.func, ast.Name): 
            self.node_visit_listener.on_visit_func_call(f"{node.func.id}()")
        
        # if the function is called as an attribute, e.g. foo.bar()
        # we also want to resolve the owner first add it to the called 
        # function's complete name 
        if isinstance(node.func, ast.Attribute): 
            self.node_visit_listener.on_visit_func_call(
                ".".join([self.resolve_owner(node), f"{node.func.attr}()"])
            )

        super().generic_visit(node) 

    def resolve_owner(self, node): 
        # Try to resolve the owner of the method

        # This is an object: obj.method()
        if isinstance(node.func.value, ast.Name): 
            return node.func.value.id

        # Class instantiation, e.g., MyClass().method()
        if isinstance(node.func.value, ast.Call): 
            if isinstance(node.func.value.func, ast.Name):
                return f"{node.func.value.func.id}()"

        # fall back if too complex: 
        return "***"
