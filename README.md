# RlTutRev

Following the [Roguelike Tutorial Revised](https://www.reddit.com/r/roguelikedev/comments/8ql895/roguelikedev_does_the_complete_roguelike_tutorial/)

## My Notes

### I'm using

* Windows 10 Pro x64
* Visual Studio Code x64
* Python 3.7.5 (64-bit), installed via exe from python.org
* GitHub

Essentially:

* open the project dir in VSCode
* add/modify files in VSCode
* F5 (or Ctrl-F5) to run
* use VSCode's Source Control panel to Commit locally
* and then VSCode's Status Bar to create new branches and sync to GitHub
* use the built-in Terminal as needed

### Make pylint in VSCode stop showing "unable to import" Errors

plylint was throwing Errors about not being able to import libtcod, even though everything is working fine when I hit Ctrl-F5. This comment fixed it for me:

https://github.com/DonJayamanne/pythonVSCode/issues/1326#issuecomment-384637049

    gopaltirupur commented on Apr 26

    check correct setting of "python.linting.pylintArgs" - example given below

    "python.linting.pylintArgs": [
    "--load-plugins",
    "pylint_django"
    ]

## P.S.

### Markdown Cheatsheet

https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
