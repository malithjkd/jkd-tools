# Helloworld

Visualizing branch topology in git is hard. I usually use follwoing to udestand whats going on.

on linux :~$  git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
