# opt-tool
OpenStack Project Template tool

## Description
This is my project for university graduation work. This tool is templating tool for new OpenStack projects, that allows create empty python packages with predefined structure. All structure describes in config file (this tool uses `yaml` filetype). Project is written in Python 3.

## Table of content
- [Config file](#config)
- [Usage](#usage)
- [Examples](#examples)

## <a name="config"></a>Config file
Config file have a two required keys: `packages` and `output_dir`.
- `output_dir` variable describes in which directory should be used for generated files
- `packages` describes the python packages structure. This key have a two sub-keys - `name` contains a name of generated package, and `components` - a list of subpackages in general package. Each next key (excluding `entity`) describes the name of subdirectory, which will be used as name of directory/name of subpackage. `Entity` key tell us, that next lists (or dicts) will be used for classes or methods naming.


## <a name="usage"></a>Usage
```
> python3 opt_tool/main.py --config <YOUR_CONFIG>.yaml
```

## <a name="examples"></a>Examples
All next examples shows example of config file and output of `tree` command on generated directory
```
> cat etc/opt-tool.yaml 

```
### Task list
- [x] Create directories
- [x] Create empty classes
- [x] Create classes with empty methods
- [x] Create init files
- [x] Create basic setup.py/setup.cfg
- [x] Create basic readme
- [ ] Make sure, that it is installable to binary
- [ ] Use Jinja as templating tool
- [ ] Create validation schema
- [ ] Allow generating setup.cfg with binary, and etc
- [ ] Prepare Dockerfile/Docker-compose
- [ ] Backward compatibility with py2.7
- [ ] Setup travis with basic CI check
- [ ] Prepare draft for "refactoring" (maybe, if I will have a free time)