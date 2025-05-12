#ifndef SHELLP_H
#define SHELLP_H

enum Kind {
  noCMD,exitCMD,cdCMD,pwdCMD,linkCMD,rmCMD,basicCMD,pipelineCMD
};

typedef struct Stage {
   int       _nba;
   char**   _args;
   int      _fdin;	
   int     _fdout;	
   pid_t   _child;  
} Stage;

/* A pipeline "object" contains 
 * 1. An array of nbStages stages
 * 2. A mode flag to determine whether 
 *            - the pipeline input is redirected
 *            - the pipeline output is redirected
 * Each stage is a structure that encapsulates
 * - The number of arguments
 * - Each argument (in string form)
 * - input fd
 * - output fd
 * - pid
 * BY DEFAULT THE MAIN PROGRAM CALLS THE PRINT METHOD OF THE COMMAND
 * OBJECT. So you can see how the pipeline description is represented/stored
 */

typedef struct Command {
  char*      _com;
  enum Kind _kind;
  int       _mode;
  char*    _input;
  char*   _output;
  char**    _args;
  int        _nba;
  Stage** _stages;	//array of stages in the pipeline. 
  int        _nbs;
} Command;

#define TRUE 1
#define FALSE 0

#endif
