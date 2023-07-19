#!/bin/bash

# Reset the branch to the first commit
git checkout main
git reset --soft $(git rev-list --max-parents=0 HEAD)

# Add all changes to the staging area
git add .

# Commit all changes with a single commit message
git commit -m "Compress all changes into a single commit"
