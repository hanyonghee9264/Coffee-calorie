#!/usr/bin/env bash
git add -f .secrets/
git add -f .static/
git add -f .tool/
eb deploy --profile eb-coffeecalorie --staged
git reset HEAD .secrets/
git reset HEAD .static/
git reset HEAD .tool/