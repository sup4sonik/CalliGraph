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

![Screenshot from 2025-03-01 00-29-34](https://github.com/user-attachments/assets/bd56b6ca-eb7d-4569-97dc-bbacc5b49963)


## Roadmap
### Definitely 
* support differnet output types 
* file to exclude methods 

### Maybe
* draw graph
* support multi file
