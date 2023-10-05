#!/bin/sh
#set -e

while getopts s:p:r:u:t: flag
do
    case "${flag}" in
        s) server="${OPTARG}" ;;
        p) project=${OPTARG};;
        u) user=${OPTARG};;
        r) repository=${OPTARG};;
        t) token=${OPTARG};;
    esac
done

if [ -z "${server}" ]; then echo "Please provide a server name" >&2; exit 1; fi
if [ -z "$project" ]; then echo "owner variable needed" >&2; exit 1; fi
if [ -z "$repository" ]; then echo "repository variable needed" >&2; exit 1; fi
if [ -z "$user" ]; then echo "username variable needed" >&2; exit 1; fi
if [ -z "$token" ]; then echo "personal access token needed" >&2; exit 1; fi

echo "received vars:"
echo "project: $project"
echo "user: $user"
echo "repository: $repository"

echo "Adding remote"

cloneurl="https://$user:$token@$server/scm/$project/$repository.git"
echo $cloneurl

git init

git remote add "$repository" $cloneurl
 
echo "pulling latest"
#git pull "$repository" main --no-rebase

echo "adding files"
git add nodejs-examples/
git commit -m "init commit"

echo "pushing to repo $repository"
git push "$repository" HEAD:main

echo "removing remote"
 git remote remove "$repository"