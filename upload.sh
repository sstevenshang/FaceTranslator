#!/bin/bash

echo 'hi';

GIT=`which git`
REPO_DIR=/Users/campionfellin/Desktop/hackmit/FaceTranslator

cd ${REPO_DIR};

${GIT} rm -r --cached .;

${GIT} add .;

${GIT} commit -m "uploading woo";

${GIT} push origin master;

sleep 2 

echo 'done';