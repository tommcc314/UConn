#       CSE 3666 Lab 1

        .globl  main

        .text
main:   
        # read integer and store it s1
        addi    a7, x0, 5
        ecall
        addi    s1, a0, 0       

	#print s1 in binary
        li      a7, 35
        add     a0, s1, zero
        ecall

	#print newline
	li	a7, 11
	addi	a0, x0, '\n'
        ecall  
        
        #register to store reversed bits
        addi	s2, x0, 0
        #temporary variables
        addi	t0, x0, 0
        addi	t1, x0, 32
        addi	t2, x0, 1
        
reverse:
	# i < 32
	bge	t0, t1, exit
	# s2 <<= 1
	slli	s2, s2, 1
	# s2 |= (s1 & 1)
	and	t3, s1, t2
	xor	s2, s2, t3
	# s1 >>= 1
	srli	s1, s1, 1
	# i+= 1
	addi 	t0, t0, 1
	beq	x0, x0, reverse	
	
exit:  
	#print s2 in binary
	li	a7, 35
	add	a0, s2, zero
	ecall
	
	#print newline
	li	a7, 11
	addi	a0, x0, '\n'
        ecall   
        
        # sys call to exit
   	addi    a7, x0, 10      
        ecall
