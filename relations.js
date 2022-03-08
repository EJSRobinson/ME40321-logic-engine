//*Tip Chord - 0
// Cr, S, A
// Cr, S, SweepLE, SweepTE
// Cr, TR
// Cr, S, Stress
// Cr, S, Vd

//*Root Chord - 1
// Ct, S, A
// Ct, S, SweepLE, SweepTE
// Ct, TR
// Ct, S, Stress
// Ct, S, Vd

//*Span - 2
// Ct, Cr, A
// Ct, Cr, SweepLE, SweepTE
// Ct, Cr, Stress
// Ct, Cr, Vd
// AR, A

//*Aspect Ratio - 3
// S, A
// Cna, TR, SweepLE
// Cna, TR, SweepTE

//*Taper Ratio - 4
// Cna, AR, SweepLE
// Cna, AR, SweepTE
// Ct, Cr

//*Fin Area - 5
// Ct, Cr, S
// AR, S
// Mass, t, Material

//*Lift Slope - 6
// Kn, Xfin, N
// TR, AR, SweepTE
// TR, AR, SweepLE

//***********************7

//*AoA - 8
// Cn, Cna

//*Cn - 9
// AoA, Cna

//*Ctan - 10
// AoA, Cda

//*Cl - 11
// Cn, Ctan, AoA

//*Cd - 12
// Cn, Ctan, AoA

//*Lift Force  - 13
// Cl, A, S, M, Alt, Temperature

//*Drag Force  - 14
// Cd, A, S, M, Alt, Temperature

//*Stress - 15
// Cr, Ct, S, Cn, t
// Cr, Ct, SweepLE, Cn, t
// Cr, Ct, SweepTE, Cn, t
// Cr, SweepTE, SweepLE, Cn, t
// Ct, SweepTE, SweepLE, Cn, t

//*Thickness - 16
// Cr, Ct, S, SweepLE, Cn, Stress
// Cr, Ct, S, SweepTE, Cn, Stress
// Cr, S, SweepTE, SweepLE, Cn, Stress
// Ct, S, SweepTE, SweepLE, Cn, Stress

//*Delection - 17
// Stress, t, Cr, Ct, SweepLE, S
// Stress, t, Cr, Ct, SweepTE, S
// Stress, t, Cr, SweepTE, SweepLE, S
// Stress, t, Ct, SweepTE, SweepLE, S

//*Mass - 18
// Total Mass, N
// A, t, Material

//*Total Mass - 19
// Mass, N

//*N - 20
// Mass, Total Mass
// Kn, Cna, Xfin, Cna (Components), Xcomps

//*SweepLE - 21
// Cr, Ct, SweepTE, S
// Cr, TR, SweepTE, S
// Ct, TR, SweepTE, S

//*SweepTE - 22
// Cr, Ct, SweepLE, S
// Cr, TR, SweepLE, S
// Ct, TR, SweepLE, S

//***********************23

//*Kn - 24
// Cna, Xfin, N, Cna (Components), Xcomps, M, COG Pos,
// C1, Velocity, Altitude, Aref, Cna, Cna (Components)

//*M - 25
// Velocity, Surface Temperature, Max Altitude

//*V - 26
// M, Surface Temperature, Max Altitude

//*Critical Flutter - 27
//********************

//*Divergence Velocity
//********************

//*C1 - 29
// Kn, Velocity, Altitude, Aref, Cna, Cna (Components)
// Wn, Il

//*Wn - 30
// C1, Il
// Pitching Time Period

//*Damping Ratio - 31
// C2a, C2p, C1, Il

//*Pitching Time Period - 32
// Wn
