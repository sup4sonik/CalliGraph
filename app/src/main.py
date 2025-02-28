
import sys 
import ast 
from node_visitor import NodeVisitor
from node_visit_interface import NodeVisitInterface
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

class CalliGraph(NodeVisitInterface): 

    def __init__(self): 
        self.callmap = {}
        self.current_function = None 
        
        self.exclude_list = [
            "print()", "len()", "sys.exit()"
        ]


    # @override 
    def on_visit_func_def(self, func_name): 
        # set the current function name 
        self.current_function = func_name

    # @override 
    def on_visit_func_call(self, func_call):
        
        # we can exclude some function calls here.. 
        if func_call in self.exclude_list: 
            return

        # add the call to the function map for the current function 
        if self.current_function in self.callmap.keys(): 
            self.callmap[self.current_function].append(func_call)
        else: 
            self.callmap[self.current_function] = [func_call]

    def analyze(self, asttree):
        visitor = NodeVisitor(self)
        visitor.visit(asttree)

        print("finished analyzing file...")
        self.pretty_print()

    def pretty_print(self): 
        for func, calls in self.callmap.items():
            print(Fore.GREEN + Style.BRIGHT + f"\n{func}:")
            for call in calls:
                print(Fore.LIGHTBLACK_EX + f"  ->  " + Fore.RESET + f"{call}")
            if not calls:
                print("    No calls")


def readfile(filename): 
    with open(filename, "r") as f:
        return ast.parse(f.read(), filename)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app/main.py <python_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    print(f"Parsing {filename}...")
    asttree = readfile(filename)

    # run program 
    CalliGraph().analyze(asttree)