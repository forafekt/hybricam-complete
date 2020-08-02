#!/bin/bash
echo "Beginning to render AngularJS files to Django static."
sleep 5
ng build --prod --output-path ../serve/dist/temp --output-hashing none

sleep 1
echo "Angular static assets have been rendered to '../serve/dist/temp' successfully!"


sleep 2
echo "Moving 'assets'..."
mv ../serve/dist/temp/assets ../serve/dist/

sleep 3
echo "Beginning to move file-types to respective directory..."
sleep 2
echo "Moving CSS files to ng_css directory..."
  if [ ! -d ../serve/dist/temp/ng_css/ ]; then
    mkdir ../serve/dist/temp/ng_css/ \
    && mv ../serve/dist/temp/*.css ../serve/dist/temp/ng_css/
  fi
  echo "CSS files have been moved to '../serve/dist/temp/ng_css/'."
sleep 2

echo "Moving JS files to ng_js directory..."
sleep 2

if [ ! -d ../serve/dist/temp/ng_js/ ]; then
    mkdir ../serve/dist/temp/ng_js/ \
    && mv ../serve/dist/temp/*.js ../serve/dist/temp/ng_js/
  fi
  sleep 2
echo "JS files have been moved to '../serve/dist/temp/ng_js/'"
sleep 2

echo "Moving all files to static 'assets'...'"
mv ../serve/dist/temp/* ../serve/dist/assets
sleep 2

echo "Removing temp build directory...'"
sudo rm -r ../serve/dist/temp
sleep 2

echo "Build is complete."
sleep 5
