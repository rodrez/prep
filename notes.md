# Things I learned while doing this

## Create file in current and all subdirectories
```bash
find . -type d exec touch {}/main.py \;
```
