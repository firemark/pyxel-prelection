#!/usr/bin/env bash
set -e
trap "git checkout master --force" EXIT
START=6000aff4aea00a51111c17b90ecd84a391432339
END=d09df36ce9eb72b5edcc9ef0ec7f682c0d30f46f
COMMITS=($START $(git log --pretty=tformat:%H $START..$END | tac))

show_commit() {
    LINE=$(python3 -c "print('#'*100)")
    FORMAT="format:%n$(expr $1 + 1). %s%n$LINE%n%n"
    git show $2 --pretty="$FORMAT" | delta --line-numbers --true-color never --dark --paging=always
}

LEN="${#COMMITS[@]}"
for ((i=0;i<LEN;i++)); do
    COMMIT=${COMMITS[$i]}
    git checkout $COMMIT 2> /dev/null
    show_commit $i $COMMIT
    set +e
    pyxel-prelection-game
    set -e
done
