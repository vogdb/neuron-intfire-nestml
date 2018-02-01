#!/usr/bin/env bash

cd build
find . \! -name '.gitkeep' -delete
cd ../

NESTML_INSTALL_DIR="${NESTML_INSTALL_DIR:-$HOME/workspace/3rdparty/nestml/target}"
if [ ! -f $NESTML_INSTALL_DIR/nestml.jar ]; then
    echo "Please set a correct NESTML_INSTALL_DIR" 1>&2
    exit 1
fi
java -jar $NESTML_INSTALL_DIR/nestml.jar research_team_models/ --target build/

cd build
cmake -Dwith-nest=$NEST_INSTALL_DIR/bin/nest-config .
make all
make install

