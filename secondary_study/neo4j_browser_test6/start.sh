#!/bin/bash
source pui/bin/activate
nohup neo4j console &
python app.py &
nohup brave-browser http://localhost:8003/browser/ &