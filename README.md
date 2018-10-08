# RlTutRev

Following the [Roguelike Tutorial Revised](https://www.reddit.com/r/roguelikedev/comments/8ql895/roguelikedev_does_the_complete_roguelike_tutorial/)

## My Notes

### I'm using

* Windows 10 Pro x64
* Visual Studio Code x64
* Python 3.7 (64-bit), installed via choco
* GitHub

Essentially:

* open the project dir in VSCode
* add/modify files in VSCode
* Ctrl-F5 to run
* use VSCode's Source Control panel to Commit locally
* and then VSCode's Status Bar to create new branches and sync to GitHub
* use the built-in Terminal as needed

## Link to library files instead of copying them to the project folder

I also didn't like copying parts of a library & related files to my project dir, so made some modifications to import the files.

1. Downloaded latest MSVS-compiled x64 libtcod (libtcod-1.7.0-x86_64-msvc.zip) from https://bitbucket.org/libtcod/libtcod/downloads/
2. Extracted to D:\dev\libtcod-1.7.0-x86_64-msvc
3. Modified the top of the main "engine.py" file:

```Python
    libtcod_dir = "/dev/libtcod-1.7.0-x86_64-msvc/"
    fonts_dir = libtcod_dir + "/data/fonts/"

    import sys
    sys.path.append(libtcod_dir + 'python/')

    import libtcodpy as libtcod
    ...
```

and further down for the font image's filepath:

```Python
    libtcod.console_set_custom_font(
        fonts_dir + 'arial10x10.png',
        libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

```

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
