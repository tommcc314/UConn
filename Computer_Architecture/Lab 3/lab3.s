#       CSE 3666 Lab 3: remove spaces

        .data
        # allocating space for both strings
str:    .space  128
res:    .space  128

        .globl  main

        .text
main:   
        # load address of strings 
        la      s0, str
        la      s1, res

        # we do not need LA pseudoinstructions from now on

        # read a string into str
        addi    a0, s0, 0 
        addi    a1, x0, 120
        addi    a7, x0, 8
        ecall

        # str's addres is already in s0
        # copy res's address to a1
        addi    a1, s1, 0

        # TODO
	# remove spaces in str

        
        
	addi	t0, s0, 0 # variable for storing str offset + address
	addi	t1, a1, 0 # variable for storing res offset + address
	addi	a2, x0, 0x20 # for comparing with space
check:
	lb	t3, (t0) # c = str[i]
	addi	t0, t0, 1 # i += 1
	beq	t3, x0, exit # loop condition: c != 0
	beq	t3, a2, check # if c = ' ' continue to next iteration
	sb	t3, (t1) # res[j] = c
	addi	t1, t1, 1 # j += 1
	beq	x0, x0, check # loop
		
	# print res
  
	
        # your code assumes str's address is in a0 and res's address is in a1
               
exit:   
	li	a7, 4
	addi	a0, a1, 0
        ecall
        
	addi    a7, x0, 10
        ecall
