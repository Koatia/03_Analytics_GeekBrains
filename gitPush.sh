#!/bin/bash

REPO="03_Analytics_GeekBrains.git"
commit_message="commited $date"

# Добавление удаленных репозиториев
git remote add origin git@github.com:Koatia/$REPO
git remote add mirror ssh://git@gitverse.ru:2222/Kostia/$REPO

# Пуш изменений в оба репозитория
for COMM in "git add ." "git commit -m \"$commit_message\"" "git push origin master" "git push mirror master" "git status" "git log --oneline --all --graph"; do
    echo
    echo "*****************************************"
    echo Выполняется "$COMM"
    eval $COMM
done

echo '--------'
echo "Обновление завершено"
