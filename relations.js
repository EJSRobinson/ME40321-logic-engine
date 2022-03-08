//Define Relations

export class Relations {
  funcs = {};
  constructor(funcs) {
    this.funcs = funcs;
    this.rules = {
      //Tip Chord
      ct: {
        1: {
          vars: ['cr', 'S', 'Afin'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['cr', 'S', 'TEsw', 'LEsw'],
          solve: this.funcs.testfunc,
        },
        3: {
          vars: ['cr', 'TR'],
          solve: this.funcs.testfunc,
        },
        4: {
          vars: ['cr', 'S', 'Sigma'],
          solve: this.funcs.testfunc,
        },
        5: {
          vars: ['cr', 'S', 'Vdiv'],
          solve: this.funcs.testfunc,
        },
      },
      //Root Chord
      cr: {
        1: {
          vars: ['ct', 'S', 'Afin'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['ct', 'S', 'TEsw', 'LEsw'],
          solve: this.funcs.testfunc,
        },
        3: {
          vars: ['ct', 'TR'],
          solve: this.funcs.testfunc,
        },
        4: {
          vars: ['ct', 'S', 'Sigma'],
          solve: this.funcs.testfunc,
        },
        5: {
          vars: ['ct', 'S', 'Vdiv'],
          solve: this.funcs.testfunc,
        },
      },
      // Span
      S: {
        1: {
          vars: ['ct', 'cr', 'Afin'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['ct', 'cr', 'LEsw', 'TEsw'],
          solve: this.funcs.testfunc,
        },
        3: {
          vars: ['cr', 'cr', 'stress'],
          solve: this.funcs.testfunc,
        },
        4: {
          vars: ['ct', 'cr', 'Vdiv'],
          solve: this.funcs.testfunc,
        },
        5: {
          vars: ['AR', 'Afin'],
          solve: this.funcs.testfunc,
        },
      },
      // Aspect Raio
      AR: {
        1: {
          vars: ['S', 'Afin'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['Cna', 'TR', 'LEsw'],
          solve: this.funcs.testfunc,
        },
        3: {
          vars: ['Cna', 'TR', 'TEsw'],
          solve: this.funcs.testfunc,
        },
      },
      // Taper Ratio
      TR: {
        1: {
          vars: ['Cna', 'AR', 'LEsw'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['Cna', 'AR', 'TEsw'],
          solve: this.funcs.testfunc,
        },
        3: {
          vars: ['ct', 'cr'],
          solve: this.funcs.testfunc,
        },
      },
      // Area of Fin
      Afin: {
        1: {
          vars: ['ct', 'cr', 'S'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['AR', 'S'],
          solve: this.funcs.testfunc,
        },
        3: {
          vars: ['m', 't', 'Mat'],
          solve: this.funcs.testfunc,
        },
      },
      // Normal Lift Slope
      Cna: {
        1: {
          vars: ['Kn', 'Xfin', 'N'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['TR', 'AR', 'TEsw'],
          solve: this.funcs.testfunc,
        },
        3: {
          vars: ['TR', 'AR', 'LEsw'],
          solve: this.funcs.testfunc,
        },
      },
      // Angle of Attack
      AoA: {
        1: {
          vars: ['Cn', 'Cna'],
          solve: this.funcs.testfunc,
        },
      },
      // Normal Force Coefficient
      Cn: {
        1: {
          vars: ['AoA', 'Cna'],
          solve: this.funcs.testfunc,
        },
      },
      // Tangential Force Coefficient
      Ct: {
        1: {
          vars: ['AoA', 'Cta'],
          solve: this.funcs.testfunc,
        },
      },
      // Lift Force Coefficient
      Cl: {
        1: {
          vars: ['Cn', 'Ctan', 'AoA'],
          solve: this.funcs.testfunc,
        },
      },
      // Drag Force Coefficient
      Cd: {
        1: {
          vars: ['Cn', 'Ctan', 'AoA'],
          solve: this.funcs.testfunc,
        },
      },
      // Lift Force
      Fl: {
        1: {
          vars: ['Cl', 'Afin', 'S', 'M', 'Alt', 'Ta'],
          solve: this.funcs.testfunc,
        },
      },
      // Drag Force
      Fd: {
        1: {
          vars: ['Cd', 'Afin', 'S', 'M', 'Alt', 'Ta'],
          solve: this.funcs.testfunc,
        },
      },
      // Stress
      Sigma: {
        1: {
          vars: ['cr', 'ct', 'S', 'Cn', 't'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['cr', 'ct', 'LEsw', 'Cn', 't'],
          solve: this.funcs.testfunc,
        },
        3: {
          vars: ['cr', 'ct', 'TEsw', 'Cn', 't'],
          solve: this.funcs.testfunc,
        },
        4: {
          vars: ['cr', 'TEsw', 'LEsw', 'Cn', 't'],
          solve: this.funcs.testfunc,
        },
        5: {
          vars: ['ct', 'TEsw', 'LEsw', 'Cn', 't'],
          solve: this.funcs.testfunc,
        },
      },
      // Thickness
      t: {
        1: {
          vars: ['ct', 'cr', 'LEsw', 'S', 'Cn', 'Sigma'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['ct', 'cr', 'TEsw', 'S', 'Cn', 'Sigma'],
          solve: this.funcs.testfunc,
        },
        3: {
          vars: ['LEsw', 'cr', 'TEsw', 'S', 'Cn', 'Sigma'],
          solve: this.funcs.testfunc,
        },
        4: {
          vars: ['LEsw', 'ct', 'TEsw', 'S', 'Cn', 'Sigma'],
          solve: this.funcs.testfunc,
        },
      },
      // Deflection
      v: {
        1: {
          vars: ['Sigma', 't', 'cr', 'ct', 'LEsw', 'S'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['Sigma', 't', 'cr', 'ct', 'TEsw', 'S'],
          solve: this.funcs.testfunc,
        },
        3: {
          vars: ['Sigma', 't', 'cr', 'LEsw', 'TEsw', 'S'],
          solve: this.funcs.testfunc,
        },
        4: {
          vars: ['Sigma', 't', 'ct', 'LEsw', 'TEsw', 'S'],
          solve: this.funcs.testfunc,
        },
      },
      // Mass per fin
      m: {
        1: {
          vars: ['mT', 'N'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['Afin', 't', 'Mat'],
          solve: this.funcs.testfunc,
        },
      },
      // Total mass of fins in set
      mT: {
        1: {
          vars: ['m', 'N'],
          solve: this.funcs.testfunc,
        },
      },
      // Number of fins in set
      N: {
        1: {
          vars: ['m', 'mT'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['Kn', 'Cna', 'Xfin', 'CnaComp', 'Xcomp'],
          solve: this.funcs.testfunc,
        },
      },
      // Leading Edge Sweep
      LEsw: {
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
      // Trailing Edge Sweep
      TEsw: {
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
      // Axial Distance of fin set
      Xfin: {
        1: {
          vars: ['Kn', 'Cna', 'N', 'CnaComp', 'Xcomp'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['Kn', 'Cna', 'N'],
          solve: this.funcs.testfunc,
        },
      },
      // Static Stability Margin
      Kn: {
        1: {
          vars: ['Cna', 'Xfin', 'N', 'CnaComp', 'Xcomp', 'M', 'XCog'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['C1', 'V', 'Alt', 'Aref', 'Cna', 'CnaComp'],
          solve: this.funcs.testfunc,
        },
      },
      // Mach Number
      M: {
        1: {
          vars: ['V', 'Ta', 'Alt'],
          solve: this.funcs.testfunc,
        },
      },
      // Velocity
      V: {
        1: {
          vars: ['M', 'Ta', 'Alt'],
          solve: this.funcs.testfunc,
        },
      },
      // Dynamic C1 coefficient (0th order co-ef of 2nd order ODE)
      C1: {
        1: {
          vars: ['Kn', 'V', 'Alt', 'Aref', 'Cna', 'CnaComp'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['Wn', 'I'],
          solve: this.funcs.testfunc,
        },
      },
      // Natural Frequency
      Wn: {
        1: {
          vars: ['C1', 'I'],
          solve: this.funcs.testfunc,
        },
        2: {
          vars: ['Tp'],
          solve: this.funcs.testfunc,
        },
      },
      // Damping Ratio
      Zeta: {
        1: {
          vars: ['C2a', 'C2p', 'C1', 'I'],
          solve: this.funcs.testfunc,
        },
      },
      // Pitching Time Period
      Tp: {
        1: {
          vars: ['Wn'],
          solve: this.funcs.testfunc,
        },
      },
      // Normal Force
      Fn: {
        1: {
          vars: ['Cn', 'Afin', 'S', 'M', 'Alt', 'Ta'],
          solve: this.funcs.testfunc,
        },
      },
      // Tangential Force
      Ft: {
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
