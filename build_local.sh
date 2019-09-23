#!/bin/bash
export CONAN_USERNAME=rhololkeolke
export CONAN_LOGIN_USERNAME=rhololkeolke
export CONAN_CHANNEL=stable
export CONAN_UPLOAD=https://api.bintray.com/conan/rhololkeolke/public-conan
export CONAN_STABLE_BRANCH_PATTERN='stable/*'
export CONAN_UPLOAD_ONLY_WHEN_STABLE=1
export CONAN_ARCHS=x86_64
export CONAN_BUILD_POLICY=outdated
export CONAN_REMOTES="https://api.bintray.com/conan/bincrafters/public-conan"
export CONAN_UPLOAD_DEPENDENCIES=all

export PATH=$PATH:/usr/games

if type cowsay >/dev/null
then function cowsay { cowsay "$@" ;}
else function cowsay { echo "$@" ;}
fi

export PATH=$PATH:$HOME/bin

if type pokemonsay >/dev/null
then function pokesay { pokemonsay "$@" ;}
else function pokesay { cowsay "$@" ;}
fi

pokesay "Installing prereqs"
.travis/install.sh

pokesay "Building Clang 8 Versions"
export CONAN_CLANG_VERSIONS=8
export CONAN_DOCKER_IMAGE=rhololkeolke/clang8
.travis/run.sh
