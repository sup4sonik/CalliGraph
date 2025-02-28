class NodeVisitInterface(): 

    def on_visit_func_def(self, func_name): 
        raise NotImplementedError("Function must be defined in sublcass")

    def on_visit_func_call(self, func_call): 
        raise NotImplementedError("Function must be defined in sublcass")
