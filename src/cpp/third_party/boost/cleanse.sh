#!/bin/bash

rm -rf doc tools more
find . | grep example | xargs rm -rf
find . | grep html$ | xargs rm -rf
find . | grep htm$ | xargs rm -rf
find . | grep css$ | xargs rm -rf
rm -rf  libs/math/doc
