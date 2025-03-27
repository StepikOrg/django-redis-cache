#!/bin/bash

: ${REDIS_VERSION:="7.4.2"}

test -d redis || git clone https://github.com/redis/redis
git -C redis checkout $REDIS_VERSION
make -C redis
