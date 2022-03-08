//Define Relations

export class Relations {
  funcs = {};
  constructor(funcs) {
    this.funcs = funcs;
    this.rules = {
      //*Tip Chord - 0
      tipChord: {
        1: {
          // Cr, S, A
          vars: ['cr', 'S', 'Afin'],
          solve: this.funcs.testfunc,
        },
        2: {
          // Cr, S, SweepLE, SweepTE
          vars: ['cr', 'S', 'TEsw', 'LEsw'],
          solve: this.funcs.testfunc,
        },
        3: {
          // Cr, TR
          vars: ['cr', 'TR'],
          solve: this.funcs.testfunc,
        },
        4: {
          // Cr, S, Stress
          vars: ['cr', 'S', 'Sigma'],
          solve: this.funcs.testfunc,
        },
        5: {
          // Cr, S, Vd
          vars: ['cr', 'S', 'Vdiv'],
          solve: this.funcs.testfunc,
        },
      },
      rootChord: {
        1: {
          // ct, S, A
          vars: ['ct', 'S', 'Afin'],
          solve: this.funcs.testfunc,
        },
        2: {
          // ct, S, SweepLE, SweepTE
          vars: ['ct', 'S', 'TEsw', 'LEsw'],
          solve: this.funcs.testfunc,
        },
        3: {
          // ct, TR
          vars: ['ct', 'TR'],
          solve: this.funcs.testfunc,
        },
        4: {
          // ct, S, Stress
          vars: ['ct', 'S', 'Sigma'],
          solve: this.funcs.testfunc,
        },
        5: {
          // ct, S, Vd
          vars: ['ct', 'S', 'Vdiv'],
          solve: this.funcs.testfunc,
        },
      },
      span: {
        1: {
          // ct, cr, A
          vars: ['ct', 'cr', 'Afin'],
          solve: this.funcs.testfunc,
        },
        2: {
          // Ct, Cr, SweepLE, SweepTE
          vars: ['ct', 'cr', 'LEsw', 'TEsw'],
          solve: this.funcs.testfunc,
        },
        3: {
          // Ct, Cr, Stress
          vars: ['cr', 'cr', 'stress'],
          solve: this.funcs.testfunc,
        },
        4: {
          // Ct, Cr, Vd
          vars: ['ct', 'cr', 'Vdiv'],
          solve: this.funcs.testfunc,
        },
        5: {
          // AR, A
          vars: ['AR', 'Afin'],
          solve: this.funcs.testfunc,
        },
      },
      aspectRatio: {
        // S, A
        1: {
          vars: ['S', 'Afin'],
          solve: this.funcs.testfunc,
        },
        // Cna, TR, SweepLE
        2: {
          vars: [''],
          solve: this.funcs.testfunc,
        },
        // Cna, TR, SweepTE
        3: {
          vars: ['Cna', 'TR', 'TEsw'],
          solve: this.funcs.testfunc,
        },
      },
      taperRatio: {
        // Cna, AR, SweepLE
        1: {
          vars: ['Cna', 'AR', 'LEsw'],
          solve: this.funcs.testfunc,
        },
        // Cna, AR, SweepTE
        2: {
          vars: ['Cna', 'AR', 'TEsw'],
          solve: this.funcs.testfunc,
        },
        // Ct, Cr
        3: {
          vars: ['ct', 'cr'],
          solve: this.funcs.testfunc,
        },
      },
      finArea: {
        1: {
          // Ct, Cr, S
          vars: ['ct', 'cr', 'S'],
          solve: this.funcs.testfunc,
        },
        2: {
          // AR, S
          vars: ['AR', 'S'],
          solve: this.funcs.testfunc,
        },
        3: {
          // Mass, t, Material
          vars: ['m', 't', 'Mat'],
          solve: this.funcs.testfunc,
        },
      },
      normalSlope: {
        // Kn, Xfin, N
        1: {
          vars: ['Kn', 'Xfin', 'N'],
          solve: this.funcs.testfunc,
        },
        // TR, AR, SweepTE
        2: {
          vars: ['TR', 'AR', 'TEsw'],
          solve: this.funcs.testfunc,
        },
        // TR, AR, SweepLE
        3: {
          vars: ['TR', 'AR', 'LEsw'],
          solve: this.funcs.testfunc,
        },
      },
      angleOfAttack: {
        // Cn, Cna
        1: {
          vars: ['Cn', 'Cna'],
          solve: this.funcs.testfunc,
        },
      },
      normalForceCoefficient: {
        // AoA, Cna
        1: {
          vars: ['AoA', 'Cna'],
          solve: this.funcs.testfunc,
        },
      },
      tangentialForceCoefficient: {
        // AoA, Cda
        1: {
          vars: ['AoA', 'Cta'],
          solve: this.funcs.testfunc,
        },
      },
      lifeForceCoefficient: {
        1: {
          vars: ['Cn', 'Ctan', 'AoA'],
          solve: this.funcs.testfunc,
        },
      },
      dragForceCoefficient: {
        1: {
          vars: ['Cn', 'Ctan', 'AoA'],
          solve: this.funcs.testfunc,
        },
      },
      liftForce: {
        1: {
          vars: ['Cl', 'Afin', 'S', 'M', 'Alt', 'Ta'],
          solve: this.funcs.testfunc,
        },
      },
      dragForce: {
        1: {
          vars: ['Cd', 'Afin', 'S', 'M', 'Alt', 'Ta'],
          solve: this.funcs.testfunc,
        },
      },
      stress: {
        // Cr, Ct, S, Cn, t
        1: {
          vars: ['cr', 'ct', 'S', 'Cn', 't'],
          solve: this.funcs.testfunc,
        },
        // Cr, Ct, SweepLE, Cn, t
        2: {
          vars: ['cr', 'ct', 'LEsw', 'Cn', 't'],
          solve: this.funcs.testfunc,
        },
        // Cr, Ct, SweepTE, Cn, t
        3: {
          vars: ['cr', 'ct', 'TEsw', 'Cn', 't'],
          solve: this.funcs.testfunc,
        },
        // Cr, SweepTE, SweepLE, Cn, t
        4: {
          vars: ['cr', 'TEsw', 'LEsw', 'Cn', 't'],
          solve: this.funcs.testfunc,
        },
        // Ct, SweepTE, SweepLE, Cn, t
        5: {
          vars: ['ct', 'TEsw', 'LEsw', 'Cn', 't'],
          solve: this.funcs.testfunc,
        },
      },
      thickness: {
        // Cr, Ct, S, SweepLE, Cn, Stress
        1: {
          vars: ['ct', 'cr', 'LEsw', 'S', 'Cn', 'Sigma'],
          solve: this.funcs.testfunc,
        },
        // Cr, Ct, S, SweepTE, Cn, Stress
        2: {
          vars: ['ct', 'cr', 'TEsw', 'S', 'Cn', 'Sigma'],
          solve: this.funcs.testfunc,
        },
        // Cr, S, SweepTE, SweepLE, Cn, Stress
        3: {
          vars: ['LEsw', 'cr', 'TEsw', 'S', 'Cn', 'Sigma'],
          solve: this.funcs.testfunc,
        },
        // Ct, S, SweepTE, SweepLE, Cn, Stress
        4: {
          vars: ['LEsw', 'ct', 'TEsw', 'S', 'Cn', 'Sigma'],
          solve: this.funcs.testfunc,
        },
      },
      deflection: {
        // Stress, t, Cr, Ct, SweepLE, S
        1: {
          vars: ['Sigma', 't', 'cr', 'ct', 'LEsw', 'S'],
          solve: this.funcs.testfunc,
        },
        // Stress, t, Cr, Ct, SweepTE, S
        2: {
          vars: ['Sigma', 't', 'cr', 'ct', 'TEsw', 'S'],
          solve: this.funcs.testfunc,
        },
        // Stress, t, Cr, SweepTE, SweepLE, S
        3: {
          vars: ['Sigma', 't', 'cr', 'LEsw', 'TEsw', 'S'],
          solve: this.funcs.testfunc,
        },
        // Stress, t, Ct, SweepTE, SweepLE, S
        4: {
          vars: ['Sigma', 't', 'ct', 'LEsw', 'TEsw', 'S'],
          solve: this.funcs.testfunc,
        },
      },
      mass: {
        1: {
          vars: ['mT', 'N'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['Afin', 't', 'Mat'],
          solve: this.funcs.testfunc,
        },
      },
      setMass: {
        1: {
          vars: ['m', 'N'],
          solve: this.funcs.testfunc,
        },
      },
      finsInSet: {
        1: {
          vars: ['m', 'mT'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['Kn', 'Cna', 'Xfin', 'CnaComp', 'Xcomp'],
          solve: this.funcs.testfunc,
        },
      },
      sweepLeadingEdge: {
        1: {
          vars: ['cr', 'ct', 'TEsw', 'S'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['cr', 'TR', 'TEsw', 'S'],
          solve: this.funcs.testfunc,
        },
        3: {
          vars: ['ct', 'TR', 'TEsw', 'S'],
          solve: this.funcs.testfunc,
        },
      },
      sweepTrailingEdge: {
        1: {
          vars: ['cr', 'ct', 'LEsw', 'S'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['cr', 'TR', 'LEsw', 'S'],
          solve: this.funcs.testfunc,
        },
        3: {
          vars: ['ct', 'TR', 'LEsw', 'S'],
          solve: this.funcs.testfunc,
        },
      },
      axialPosition: {
        1: {
          vars: ['Kn', 'Cna', 'N', 'CnaComp', 'Xcomp'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['Kn', 'Cna', 'N'],
          solve: this.funcs.testfunc,
        },
      },
      staticStabilityMargin: {
        1: {
          vars: ['Cna', 'Xfin', 'N', 'CnaComp', 'Xcomp', 'M', 'XCog'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['C1', 'V', 'Alt', 'Aref', 'Cna', 'CnaComp'],
          solve: this.funcs.testfunc,
        },
      },
      machNumber: {
        1: {
          vars: ['V', 'Ta', 'Alt'],
          solve: this.funcs.testfunc,
        },
      },
      velocity: {
        1: {
          vars: ['M', 'Ta', 'Alt'],
          solve: this.funcs.testfunc,
        },
      },
      dynamicC1: {
        1: {
          vars: ['Kn', 'V', 'Alt', 'Aref', 'Cna', 'CnaComp'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['Wn', 'I'],
          solve: this.funcs.testfunc,
        },
      },
      naturalFrequency: {
        1: {
          vars: ['C1', 'I'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['Tp'],
          solve: this.funcs.testfunc,
        },
      },
      dampingRatio: {
        1: {
          vars: ['C2a', 'C2p', 'C1', 'I'],
          solve: this.funcs.testfunc,
        },
      },
      pitchingTimePeriod: {
        1: {
          vars: ['Wn'],
          solve: this.funcs.testfunc,
        },
      },
      normalForce: {
        1: {
          vars: ['Cn', 'Afin', 'S', 'M', 'Alt', 'Ta'],
          solve: this.funcs.testfunc,
        },
      },
      tangentialForce: {
        1: {
          vars: ['Ct', 'Afin', 'S', 'M', 'Alt', 'Ta'],
          solve: this.funcs.testfunc,
        },
      },
    };
  }
}

// *** TO ADD
//*TangentialSlope - 7
//*Critical Flutter - 27
//*Divergence Velocity - 28
