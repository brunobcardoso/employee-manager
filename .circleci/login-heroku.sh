#!/usr/bin/env bash

cat > ~/.netrc << EOF
    machine api.heroku.com
        login $HEROKU_EMAIL
        password $HEROKU_API_KEY
    machine git.heroku.com
        login $HEROKU_EMAIL
        password $HEROKU_API_KEY
EOF

# Add heroku.com to the list of known hosts
mkdir -p ~/.ssh
ssh-keyscan -H heroku.com >> ~/.ssh/known_hosts

echo "Install Heroku CLI"
wget https://cli-assets.heroku.com/branches/stable/heroku-linux-amd64.tar.gz
mkdir -p /usr/local/lib /usr/local/bin
tar -xvzf heroku-linux-amd64.tar.gz -C /usr/local/lib
ln -s /usr/local/lib/heroku/bin/heroku /usr/local/bin/heroku