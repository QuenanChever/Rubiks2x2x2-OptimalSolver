# Rubiks2x2x2-OptimalSolver

## Overview
This project implements an optimal solver for the 2x2x2 Rubik's cube. All optimal (=shortest) solving maneuvers are computed. The computation time is neglectible.
The solver only uses moves of the U, R and B faces because the DBL-corner is fixed. The color scheme of the cube is detected automatically.

## Fork
This repository is forked from the Rubiks 2x2x2 solver created by Herbert Kociemba [hkociemba/RubiksCube-TwophaseSolver](https://github.com/hkociemba/RubiksCube-TwophaseSolver).
Unlike the original repository, this version is meant to be used from the command line.

## Setup
First, you need to make the main script executable:
```
sudo chmod +x kociemba-2x2x2
```
To make the solver available on the command line, you must create a symlink (feel free to change the path if necessary):
```
sudo ln -s "$(pwd)/kociemba-2x2x2" /usr/local/bin/kociemba-2x2x2
```

There are pruning tables which are created on the first run. This needs about 4 MB disk space and it takes from less than a minute to a couple of minutes to create it, depending on the hardware. You can do it behorehand by executing this command:
```
kociemba-2x2x2 --init
```

## Usage
The following command returns the solving maneuver:
```
kociemba-2x2x2 <cubestring>
```

For example:
```
$ kociemba-2x2x2 DDUUBFRURRUFLDDLRFLBLBFB
R2 U3 F1 U2 F1 R2 U1 R1 U2 F2
```

Make sure that you use Python 3.