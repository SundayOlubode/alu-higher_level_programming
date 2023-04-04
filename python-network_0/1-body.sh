#!/bin/bash
# curl to end
curl -sI "$1" | grep '200';
