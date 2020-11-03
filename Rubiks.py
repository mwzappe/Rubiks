#!/usr/bin/env python3

import numpy as np

WHITE=0
ORANGE=1
BLUE=2
RED=3
GREEN=4
YELLOW=5

CubeInitial = [
    [ [ WHITE for i in range(3) ] for i in range(3) ],
    [ [ ORANGE for i in range(3) ] for i in range(3) ],
    [ [ BLUE for i in range(3) ] for i in range(3) ],
    [ [ RED for i in range(3) ] for i in range(3) ],
    [ [ GREEN for i in range(3) ] for i in range(3) ],
    [ [ YELLOW for i in range(3) ] for i in range(3) ]
    ];

Adjacancy = [
    [ ORANGE, BLUE, RED, GREEN ], # WHITE
    [ YELLOW, BLUE, WHITE, GREEN ], # ORANGE
    [ YELLOW, RED, WHITE, ORANGE ], # BLUE
    [ YELLOW, GREEN, WHITE, BLUE ], # RED
    [ YELLOW, ORANGE, WHITE, RED ], # GREEN
    [ ORANGE, GREEN, RED, BLUE] # YELLOW
    ]



print(CubeInitial)
