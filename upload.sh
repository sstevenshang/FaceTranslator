#!/bin/bash

echo 'hi';

GIT=`which git`
REPO_DIR=/Users/campionfellin/Desktop/hackmit/FaceTranslator
cd ${REPO_DIR};

${GIT} add .;

${GIT} commit -m "uploading woo";

${GIT} push origin head


echo 'done';