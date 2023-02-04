## <center>rofi-radio
### <center>a perfect way to listen to your shitty lofi online radio 
---
## what does it do
generates a bash script that can be bound to a key, that displays a rofi chooser of online radios, then plays the selected one.

## demo
![demo][demo_img]

## did you steal this
of course i did, the original source code is from
[Carbon-Bl4ck][original_repo]

## dependencies
- mpv
- libnotify
- rofi (bruh)

## usage
- get your list of radios that you want, format them in the `urls.txt` file in this way:
```
Station 1 name
http://station1.url/
Station 2 name
http://station2.url/
```

- now run `python exporter.py > rofi-radio`
- make it runnable with `chmod +x rofi-radio`
- now test it by running `./rofi-radio`
- if all is good, install it by running `sudo mv rofi-radio /usr/bin/` (or any directory on your path)

## issues
open an issue, or fix it and submit a pr

## license
wtfpl, too lazy to put it here

[original_repo]: https://github.com/Carbon-Bl4ck/Rofi-Beats
[demo_img]: demo.png