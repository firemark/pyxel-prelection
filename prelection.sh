#!/usr/bin/env bash
START=06d3eaa38ac4101876d1d2101f876350d708a908
END=cbf9ac2fbde4459568d942f9075cddad85fae550
COMMITS=($START $(git log --pretty=tformat:%H $START..$END | tac))

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