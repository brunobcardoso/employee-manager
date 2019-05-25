#!/usr/bin/env bash

set -e
set -u
source .circleci/setup-env.sh
echo "Pushing branch ${CIRCLE_BRANCH} to app ${HEROKU_APP}"
git remote add $HEROKU_REMOTE https://git.heroku.com/${HEROKU_APP}.git
git push $HEROKU_REMOTE ${CIRCLE_BRANCH}:master