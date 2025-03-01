# Helloworld

# create enviriment 
```consol
  python3 -m venv jkd-tools-env
  source jkd-tools-env/bin/activate
  pip install -r jkd-tools/requirements.txt

```

Visualizing branch topology in git is hard. I usually use follwoing to udestand whats going on.

on linux :~$  git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
