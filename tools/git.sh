#!/bin/bash

# Git Repository
git remote add gitlab git@gitlab.com:progwebapp/partysearch.git
git remote set-url --add --push origin git@gitlab.com:progwebapp/partysearch.git

git remote add github git@github.com:ProgWebApp/PartySearch.git
git remote set-url --add --push origin git@github.com:ProgWebApp/PartySearch.git

# Display Config
git remote show origin
git config --list
