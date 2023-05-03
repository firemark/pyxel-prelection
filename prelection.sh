#!/usr/bin/env bash
START=6000aff4aea00a51111c17b90ecd84a391432339
END=c42ec86d9b632452fa6e1905965546f781632ec4
COMMITS=($START $(git log --pretty=tformat:%H $START..$END | tac))

show_commit() {
    #firefox https://github.com/firemark/pyxel-prelection/commit/$2 2> /dev/null

    LINE=$(python3 -c "print('#'*100)")
    FORMAT="format:%n$(expr $1 + 1). %s%n$LINE%n%n"
    git show $2 --pretty="$FORMAT" | delta --dark -w 180 | less -RS
}

LEN="${#COMMITS[@]}"
for ((i=0;i<LEN;i++)); do
    COMMIT=${COMMITS[$i]}
    git checkout $COMMIT 2> /dev/null
    show_commit $i $COMMIT
    pyxel-prelection-game
done

git checkout master
