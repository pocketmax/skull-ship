# git notes


Git problems to solve
* Fix git merge from remote
* Change user meta data for commits
* Fix merge conflict to remote
* …
* Creating pull request via CLI
* Accepting pull request via CLI


Diff between git and maven

why svn sucked
* spread .svn tracking directories at every directory level
* central repo
*


untracked files: files outside of the repo
staged files: files ready to be committed to the repo
modified files: files git is tracking that have changes outside of the repo

git init		make a new git repo
git status		to see untracked and staged files
git branch		to see what branch your currently on
git fetch 		to grab committees from a remote repo
git pull		to grab committees from another repo and intergrade them into your repo
git stash		temporarily remotes uncommitted changes out of the repo
git pop		puts back previously stashed changes into repo
git checkout -b branchName 	to create and checkout a branch
git merge branchName -m “bla”		to merge branchName into current branch