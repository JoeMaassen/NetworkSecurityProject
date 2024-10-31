#!/bin/sh
docker exec -it target /bin/bash  -c "
python3 IDS.py -m 10000 -t 20
"
