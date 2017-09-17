#!/bin/bash

echo 'hi';


REPO_DIR=/Users/campionfellin/Desktop/hackmit/FaceTranslator;
cd ${REPO_DIR};


git add .;

git commit -m "uploading woo";

git push origin head


echo 'done';