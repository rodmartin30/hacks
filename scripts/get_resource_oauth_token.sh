#!/bin/bash

curl -H 'Authorization: Bearer '$1 http://resource.libcurl.so/api/keys --dump-header -
