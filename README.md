# CalliGraph
Draw a graph to make visible which functions are called in a file


## Prepare the environement: 

Setup virtual env for python and install the requiremetns. 

```sh
py -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the file: 

```sh
python3 app/src/main.py example.py 
```

## Output: 

Currently, the app produces the following type of output (text):

```txt
foo:
  ->  bar()
  ->  baz()

baz:
  ->  qux()

examples:
  ->  method()
  ->  example()
  ->  hello.world()
  ->  Hello()

complex:
  ->  MyClass().method()
  ->  MyClass()
  ->  ***.two()
  ->  this.example()
  ->  another.example()
```


## Roadmap
### Definitely 
* support differnet output types 
* file to exclude methods 

### Maybe
* draw graph
* support multi file
