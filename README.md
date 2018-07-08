# RlTutRev
Following the [Roguelike Tutorial Revised](https://www.reddit.com/r/roguelikedev/comments/8ql895/roguelikedev_does_the_complete_roguelike_tutorial/)


## My Notes

### Markdown Cheatsheet
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

### I'm using:
* Windows 10 Pro x64
* Visual Studio Code x64
* Python 3 (64-bit), from VS2017 install
* GitHub

Essentially open the project dir in VSCode, add/modify files directly, Ctrl-F5 to run, and using the built-in Terminal as needed.

I also didn't like copying parts of a library & related files to my project dir, so made some modifications to import the files.

1. Downloaded latest MSVS-compiled x64 libtcod (libtcod-1.7.0-x86_64-msvc.zip) from https://bitbucket.org/libtcod/libtcod/downloads/
2. Extracted to C:\dev\libtcod-1.7.0-x86_64-msvc
3. Modified the top of the main "engine.py" file:
```
    libtcod_dir = "/dev/libtcod-1.7.0-x86_64-msvc/"
    fonts_dir = libtcod_dir + "/data/fonts/"

    import sys
    sys.path.append(libtcod_dir + 'python/')

    import libtcodpy as libtcod
    ...
```
and further down for the font image's filepath:
```
    libtcod.console_set_custom_font(
        fonts_dir + 'arial10x10.png',
        libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

```
