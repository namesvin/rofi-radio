with open("urls.txt") as f:
    d = f.read().split('\n')

if len(d)%2: print("sloc not divisible by 2, you fucked something up\ntry checking for URLs with no name and vice versa"); exit()

y = 0
x = 0


print('#!/bin/sh')
print('notification(){')
print('	notify-send "Playing now: " "$@" --icon=media-tape')
print('}')
print()
print('menu(){')
for i in range(1, int(len(d)/2)):
    print('  printf "{}. {}\\n"'.format(i,d[y]));y+=2
print('  printf "{}. {}"'.format(int(len(d)/2), d[len(d)-2]))
print('}')
print()
print('main() {')
print('  choice=$(menu | rofi -dmenu | cut -d. -f1)')
print('  case $choice in')
for i in range(0, int(len(d)/2)):
    station,url = d[x],d[x+1]
    print('    {})'.format(int(i+1)))
    print('      notification "Now playing: {}"'.format(station))
    print('      URL="{}"'.format(url))
    print('      break')
    print('      ;;')
    x += 2

print('  esac')
print('  mpv --title="radio-mpv" $URL')
print('}')
print()
print('pkill -f radio-mpv || main')