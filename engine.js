// Use relations to call solvers

//IMPORT RELATIONS
//IMPORT VARS
import { Relations } from './relations.js';

const functionsCore = {
  testfunc: () => {
    return 1;
  },
};

let relations = new Relations(functionsCore);

// setInterval(() => {}, 1500);

//Run through relations
//For each, check if required variables are defined
//Run Solvers where possible
//Run checks
//Respond to checks
//Loop until all solved
//Run Optimisation (if needed)
