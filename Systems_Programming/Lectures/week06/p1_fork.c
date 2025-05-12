/* Processes - a running executable - code + processor state + memory + resource usage
 * Processes are organized as a tree rooted at 'init'
 * Every process (except init) has a parent and 0-* children
 * Processes are born as clones of the parent process - can then upgrade themselves

 * The address space of the child is an identical copy of the parent - copies diverge as processes execute
 * The child inherits all of the parent's file descriptors 
     * Any operation in parent or child moves the file pointer

 * Both the child and parent process execute concurrently - cannot say which dies first
 * Processes die upon exiting or aborting

 * Using fork() to clone a process - both parent and child return from the call to fork
 * In the parent process, fork returns the pid of the child, and -1 if an error occured
 * In the child process, fork returns 0.
 */

#include <stdio.h> 
#include <unistd.h>

int main() {
     pid_t value;
     value = fork(); /* creates a child process and puts the return val in value */
     printf("The value = %d\n", value);

     return 0;
}
