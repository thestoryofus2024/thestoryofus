### compile

```
renpy.sh launch set_project /path/to/my/project # do only once
renpy.sh --compile
```

### deploy

```
# custom prespash page:
cp The\ Story\ of\ Us/game/presplash.png TheStoryofUs-1.0-dists/TheStoryofUs-1.0-web/web-presplash.jpg

# push to gh-pages
git subtree push --prefix TheStoryofUs-1.0-dists/TheStoryofUs-1.0-web/ origin gh-pages
```
