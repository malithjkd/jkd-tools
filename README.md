# Helloworld

Visualizing branch topology in git is hard. I usually use follwoing to udestand whats going on.

on linux :~$  git log --stat --summary --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset) %C(cyan)(committed: %cD)%C(reset) %C(auto)%d%C(reset)%n''%C(bold white)%s%C(reset)%n''%C(dim white)- %an <%ae> %C(reset) %C(dim white)(committer: %cn <%ce>)%C(reset)'
