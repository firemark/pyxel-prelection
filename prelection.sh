#!/usr/bin/env bash
COMMITS=(
    06d3eaa e91f013 1afc536 5715774 66cdf9a 
    9f86bcd 206c42d 3c95a28 4de16bc fa7fe11 
    db30b07 9aa0904 18a3bf2 cbf9ac2
) 
#COMMITS=(06d3eaa e91f013) 

LEN="${#COMMITS[@]}"
for ((i=0;i<LEN;i++)); do
    COMMIT=${COMMITS[$i]}
    git checkout $COMMIT 2> /dev/null 
    LINE=$(python -c "print('#'*100)")
    FORMAT="format:%n$(expr $i + 1). %s%n$LINE%n%n"
    git show --pretty="$FORMAT" | delta --dark -w 180 | less -RS
    python3 game/game.py
done

git checkout master
