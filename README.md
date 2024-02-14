# QuitCommit

Behold !

This great script ask you one general knowledge question. If you answer incorrectly, you get a nice message about your lack of knowledge and no commit. 
Only a good answer will allow you to commit. Commit are for people who know big things like the gestation period of the [Long nosed potoroo](https://en.wikipedia.org/wiki/Long-nosed_potoroo).

## Installation

If you want to install this script, copy and paste the python file with the name 'pre-commit' in your project's .git/hooks directory.

Make it an executable (after having read the script for a potential virus of course...) and you're good to go !

Here is a line to copy / paste brainlessly when you are at the root of your versionned project :

``` bash
curl https://raw.githubusercontent.com/Ereboras/quitcommit/master/quitcommit.py -o .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

## Install with docker

Are you serious ?

## Contributions

Here is my entire CI for the project :
``` bash
cp quitcommit.py .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

This project is very ambitious. I am open to VC submission, but be aware that any offer below a beer at the local pub will be rejected.