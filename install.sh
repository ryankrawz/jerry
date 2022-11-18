#!/bin/bash

if ! [ -x $(command -v brew) ]
then
printf "The required library Pillow has dependencies that should be installed via Homebrew. Installing now...\n"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

brew install libjpeg libtiff little-cms2 openjpeg webp
pip3 install -r requirements.txt
