#!/usr/bin/env bash
START=6000aff4aea00a51111c17b90ecd84a391432339
END=d09df36ce9eb72b5edcc9ef0ec7f682c0d30f46f
COMMITS=($START $(git log --pretty=tformat:%H $START..$END | tac))

show_commit() {
    URL=https://github.com/firemark/pyxel-prelection/commit/$2
    FORMAT="format:$(expr $1 + 1). [%s]($URL)"
    git show $2 --pretty="$FORMAT" | head -n1
}

LEN="${#COMMITS[@]}"
for ((i=0;i<LEN;i++)); do
    COMMIT=${COMMITS[$i]}
    show_commit $i $COMMIT
done
