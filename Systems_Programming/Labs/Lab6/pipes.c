#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>
#include <errno.h>

#define READ_END 0
#define WRITE_END 1

#define BUFFER_SIZE 20

void write_message(char * message, int fd) {
  /* TODO Q1.1:
   * Iterate through the string (message) and write one character at a time to the fd till '\0'
   * Use the built-in write function to do this.
   */
    int sz = 0;
    while (message[sz] != 0) {
        write(fd, message + sz, 1);
        ++sz;
    }
}
char* read_message(int fd) {
  /* TODO Q1.2:
   * Create a char* buffer with initial size of BUFFER_SIZE
   * Read a character from fd into the buffer, until a new line character is reached.
    * Expand the buffer as needed.
   * The string must end with a new line character and a null character. 
   */
    char* message = malloc(BUFFER_SIZE);
    int sz = 0, cap = BUFFER_SIZE;
    while (read(fd, message + sz, 1) != 0) {
        ++sz;
        if (sz >= cap - 1) {
            message = realloc(message, cap * 2);
        }
        if (message[sz - 1] == '\n') break;
    }
    message[sz] = 0;
    return message;
}

/* This function takes as input a string and encrypts it */
void encrypt(char * message) {
  for(int i=0;i<strlen(message);i++) {
    if(message[i] == '\n') break;
    message[i] += 1;
  }
}

/* This function takes as input a string and decrypts it */
void decrypt(char * message) {
  for(int i=0;i<strlen(message);i++) {
    if(message[i] == '\n') break;
    message[i] -= 1;
  }
}

int main() {
  /* TODO Q2. Establish pipes for communication as directed in the pdf 
   * The parent process creates 2 child processes.
   * The parent process prints a string and sends it to child 1 via pipe.
   * Child 1 takes this message, encrypts it and send it to child 2 via pipe.
   * Child 2 takes the encrypted message, prints it, and sends it back to parent via pipe.
   * Parent takes the encrypted message, decrypts it and prints it on the stdout.
   
   * To do the above, you need to create pipes, fork child processes, redirect the input
   * and output of the processes to read and write end of pipes in a suitable manner.
   * Remember to always close ends of pipes that are not needed in a process.
   
   * Part of the functionality is implemented for you. Fill in the gaps listed with TODO.
   */
  
  /* TODO: 
   * Create pipes. Think carefully how many pipes you need. 
   */
    int pc1[2], c1c2[2], c2p[2];
    pipe(pc1);
    pipe(c1c2);
    pipe(c2p);
    pid_t pid1 = fork();  
    if (pid1 == 0) {    /* Child 1 */
        char* msg;        /* Buffer to receive the message from parent */
        /* TODO: 
        * Close unneeded pipes
        * Read message from the pipe connecting parent to child 1.
        */
        msg = read_message(pc1[READ_END]);
        close(pc1[READ_END]);
        close(pc1[WRITE_END]);
        printf("Child 1 is Encrypting!\n");
        encrypt(msg);
        /* TODO
        * Write message to the pipe connecting child 1 with child 2
        * Free the buffer
        * Close unneeded pipes
        */
        write_message(msg, c1c2[WRITE_END]);
        close(c1c2[WRITE_END]);
        close(c1c2[READ_END]);
        close(c2p[READ_END]);
        close(c2p[WRITE_END]);
        free(msg);
        exit(0);
    } else {          /* Parent process */
        pid_t pid2 = fork(); 
        if (pid2 ==0) { /* Child 2 */
        char* msg;    /* buffer to store the read message */
        /* TODO: 
        * Close Unneeded Pipes
        * Read the message from the pipe connecting child 1 to child 2.
        */
        msg = read_message(c1c2[READ_END]);
        close(c1c2[READ_END]);
        close(c1c2[WRITE_END]);
        printf("Child 2: %s", msg);
        /* TODO:
        * Write the message to the pipe connecting child 2 to Parent
        * Free the buffer.
        * Close unneeded pipes
        */
        write_message(msg, c2p[WRITE_END]);
        close(c2p[WRITE_END]);
        close(c2p[READ_END]);
        close(pc1[READ_END]);
        close(pc1[WRITE_END]);
        free(msg);
        exit(0);
        } else {        /* Parent */
        char * msg = "This is a test.\n"; /* this is the plaintext message */
        printf("Parent: %s", msg);
        /* TODO:
        * Close unneeded Pipes
        * Write message to pipe connecting parent to child 1
        * Read the message from pipe connecting child 2 to parent and store in msg
        */
        write_message(msg, pc1[WRITE_END]);
        close(pc1[WRITE_END]);
        close(pc1[READ_END]);
        close(c1c2[READ_END]);
        close(c1c2[WRITE_END]);
        msg = read_message(c2p[READ_END]);
        close(c2p[READ_END]);
        close(c2p[WRITE_END]);
        int exit1;
        pid_t dc1 = wait(&exit1);
        int exit2;
        pid_t dc2 = wait(&exit2);
        decrypt(msg);
        printf("Parent: %s", msg);
        /* TODO: 
        * Free the buffer
        * Close remaining Pipes
        */
        free(msg);
        return 0;
        } 
    }
}
