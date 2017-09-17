#!/bin/bash

echo 'hi';

GIT=`which git`
REPO_DIR=/Users/campionfellin/Desktop/hackmit/FaceTranslator

cd ${REPO_DIR};

${GIT} config --global user.name "campionfellin";
${GIT} config --global user.email "campionfellin@gmail.com";


${GIT} add .;

${GIT} commit -m "uploading woo";

${GIT} push -u origin master;

sleep 2; 

echo 'done';