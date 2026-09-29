# _pythonprog_ Python examples and tutorials

Git repo. with a collection of Python modules for learning/experimenting.  
Open in _VS Code_ as `code .`  
**Note:**  
Note all Python examples can be run in _VS Code_ from this root! 
Subprojects with `.vscode` projects shall be run in separate _VS Code_ IDEs. 

## Git configuration

To connect to the git remote repository we need to configure:
``` shell
# We use f.@....de
git config --global user.email "user@yuser-domain.com"
# We use f.....tb
git config --global user.name "user-name"
```

# Thematic grouping

## Simple Python
The chapters listed here are using the Python basic libs.
Other chapters with more complexity (e.g. requiring `venv` or `pytest`) are listed below. 
- ctypesXxx: Python examples using the `ctypes` lib.
- classXxx: Python class examples
- decoratorXxx: Explaining in deep the decorator-syntax `@some_decorator`.
- Root level modules: All Python modules in root DIR are hopefully self explained by their name. 


## Complex Python
Contains Python modules with external dependencies (e.g. native C++ code), requiring `venv` or `pytest` etc.
- *ctypesDllExample*: Real `ctypes` examples accessing native DLLs, as this is the **purpose** of `cytypes`!
- *tk_gui*: TK based GUI examples which requires a (`venv` based) TK installation
