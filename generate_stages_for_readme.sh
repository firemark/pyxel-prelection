#!/usr/bin/env bash
START=06d3eaa38ac4101876d1d2101f876350d708a908
END=e943556e6d5114dbebe798d5a081ca5571abe05c
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
