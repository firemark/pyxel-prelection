#!/usr/bin/env bash
START=06d3eaa38ac4101876d1d2101f876350d708a908
END=98c2eba3141af413e3fae8e99f9bd476d1c6fdd5
COMMITS=($START $(git log --pretty=tformat:%H $START..$END | tac))

show_commit() {
    #firefox https://github.com/firemark/pyxel-prelection/commit/$2 2> /dev/null

    LINE=$(python -c "print('#'*100)")
    FORMAT="format:%n$(expr $1 + 1). %s%n$LINE%n%n"
    git show $2 --pretty="$FORMAT" | delta --dark -w 180 | less -RS
}

LEN="${#COMMITS[@]}"
for ((i=0;i<LEN;i++)); do
    COMMIT=${COMMITS[$i]}
    git checkout $COMMIT 2> /dev/null 
    show_commit $i $COMMIT
    python3 game/game.py
done

git checkout master
