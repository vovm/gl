#!/bin/sh

# create a minimal bash/sh script returned a names of local files
# what were changed yourself into a current folder for last week.
# A result has to be sorted by changed date.

find . -type f -mtime -7 -printf '%T+ %u %g %TR %TD %p\n' | sort -r | grep $(whoami)
