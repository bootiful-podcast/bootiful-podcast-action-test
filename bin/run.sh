#!/usr/bin/env bash

set -e

echo "Loaded repository utils"

function deploy_system_app() {

  ## fetch the latest version and rewrite the build file
  ## VERSION=$(curl https://raw.githubusercontent.com/bootiful-podcast/bootiful-podcast-action/main/version )

  $(dirname $0)/replace_version.py
  git commit -am updating\ version\ to\ $VERSION && git push || echo "nothing to commit and push "

  APP_NAME=bootiful-podcast-action-test
  echo "Deploying $APP_NAME to environment $BP_MODE_LOWERCASE "

  if [ -z "${GH_PERSONAL_ACCESS_TOKEN}" ]; then
    echo "The Github personal access token is empty!"
    exit 1
  fi

  echo "Trying to invoke the deployment for ${APP_NAME}."

  PAYLOAD='{"event_type":"deploy-event"}'

  #  if [ "$BP_MODE_LOWERCASE" = "production" ]; then
  #    PAYLOAD='{"event_type":"deploy-production-event"}'
  #  fi

  echo $(curl -X POST -H "Accept: application/vnd.github.v3+json" \
    -H "Authorization: token ${GH_PERSONAL_ACCESS_TOKEN}" https://api.github.com/repos/bootiful-podcast/${APP_NAME}/dispatches -d $PAYLOAD)
}

deploy_system_app
