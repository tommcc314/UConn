#       CSE 3666 Lab 4
#	TAG: 61ed0598ed0f3e3e43c5abc168c4387d

	.data
	.align	2	
word_array:     .word
        0,   10,   20,  30,  40,  50,  60,  70,  80,  90, 
        100, 110, 120, 130, 140, 150, 160, 170, 180, 190,
        200, 210, 220, 230, 240, 250, 260, 270, 280, 290,
        300, 310, 320, 330, 340, 350, 360, 370, 380, 390,
        400, 410, 420, 430, 440, 450, 460, 470, 480, 490,
        500, 510, 520, 530, 540, 550, 560, 570, 580, 590,
        600, 610, 620, 630, 640, 650, 660, 670, 680, 690,
        700, 710, 720, 730, 740, 750, 760, 770, 780, 790,
        800, 810, 820, 830, 840, 850, 860, 870, 880, 890,
        900, 910, 920, 930, 940, 950, 960, 970, 980, 990

        # code
        .text
        .globl  main
main:   
	addi	s0, x0, -1
	addi	s1, x0, -1
	addi	s2, x0, -1
	addi	s3, x0, -1
	addi	s4, x0, -1
	addi	s5, x0, -1
	# help to check if any saved registers are changed during the function call
	# could add more...

        # la      s1, word_array
        lui     s1, 0x10010      # starting addr of word_array in standard memory config
        addi    s2, x0, 100      # 100 elements in the array

        # read an integer from the console
        addi    a7, x0, 5
        ecall

        addi    s3, a0, 0       # keep a copy of v in s3
        
        # call binary search
        addi	a0, s1, 0
        addi	a1, s2, 0
        addi	a2, s3, 0
        jal	ra, binary_search

	# print the return value
        jal	ra, print_int

	# set a breakpoint here and check if any saved register was changed
        # exit
exit:   addi    a7, x0, 10      
        ecall

# a function that prints an integer, followed by a newline
print_int: 
        addi    a7, x0, 1
        ecall
 
        # print newline
        addi    a7, x0, 11
        addi    a0, x0, '\n'
        ecall        
         
        jalr    x0, ra, 0
	
#### Do not change lines above
binary_search:

        addi	sp, sp, -8		# move stack pointer
        sw	s1, 4(sp)		# preserve saved register
        sw	ra, 0(sp)		# store return address
        addi	t0, x0, 0		# initialize rv
        beq	a1, x0, notfound	# if n == 0, element is not found
        srai	t1, a1, 1		# half = n / 2
        slli	t2, t1, 2		# offset = half * 4
        add	t2, t2, a0		# address of a[half]
        lw	t3, 0(t2)		# half_v = a[half]
	beq	t3, a2, found		# if half_v == v, element is found
	blt	a2, t3, lessthan	# if v < half_v, go to less than. Else:
	addi	s1, t1, 1		# left = half + 1
	slli	t4, s1, 2		# offset = left * 4
	add	a0, t4, a0		# address of a[left]
	sub	a1, a1, s1		# n = n - left for next recursive call
	jal	ra, binary_search	# recursive call
	addi	t0, a0, 0		# rv = binary_search return value
	blt	t0, x0, binary_exit	# if rv >= 0:
	add	t0, t0, s1		# rv += left
	beq	x0, x0, binary_exit	# exit
	
found:
	addi	t0, t1, 0		# rv = half
	beq	x0, x0, binary_exit	# exit
lessthan:
	addi	a1, t1, 0		# n = half for the next recursive call
        jal	ra, binary_search	# recursive call
        addi	t0, a0, 0		# rv = binary_search return value
        beq	x0, x0, binary_exit
notfound:
	addi	t0, x0, -1		# rv = -1
	beq	x0, x0, binary_exit    	# exit   
        
binary_exit:
	addi	a0, t0, 0		# store rv in a0 to return
	lw	ra, 0(sp)		# load ra
	lw	s1, 4(sp)		# restore s1
	addi	sp, sp, 8		# restore stack pointer
	jalr	x0, ra, 0		# exit function
	
        
        
