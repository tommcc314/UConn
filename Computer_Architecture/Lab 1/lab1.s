#       CSE 3666 Lab 1

        .globl  main

        .text
main:   

        # GCD examples:
        #     gcd(11, 121) = 11
        #     gcd(24, 60) = 12
        #     gcd(192, 270) = 6
        #     gcd(14, 97) = 1
        
        # more test cases:
        # gcd(24, 6) = 6
        # gcd(100, 27) = 1
        # gcd(7, 7) = 7

        # read two positive integers from the console and 
        # save them in s1 and s2 

        # use system call 5 to read integers
        addi    a7, x0, 5
        ecall
        addi    s1, a0, 0       # a in s1

        addi    a7, x0, 5
        ecall
        addi    s2, a0, 0       # b in s2

        # TODO
        # Add you code here
        # compute GCD(a, b) and print it
        
gcd:
	# if a = b, exit
	beq	s1, s2, exit
	# if a < b, go to else
	blt	s1, s2, else
	# a = a - b
	sub	s1, s1, s2
	# loop
	beq	x0, x0, gcd
	
else:
	# b = b - a
	sub 	s2, s2, s1
	#loop
	beq	x0, x0, gcd
	
exit:   # print gcd
	li	a7, 1
	add	a0, s1, zero
        ecall    
        # sys call to exit
   	addi    a7, x0, 10      
        ecall
