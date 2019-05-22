#!/usr/bin/env bash

case $CIRCLE_BRANCH in
    $STAGING_BRANCH)
        export HEROKU_REMOTE=${HEROKU_STG_REMOTE}
        export HEROKU_APP=${HEROKU_STG_APP}
        ;;
    $PRODUCTION_BRANCH)
        export HEROKU_REMOTE=${HEROKU_PROD_REMOTE}
        export HEROKU_APP=${HEROKU_PROD_APP}
        ;;
esac