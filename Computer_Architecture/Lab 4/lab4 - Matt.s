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
      addi        sp, sp, -8
      sw     ra, 4(sp)
      sw     s1, 0(sp)
      
      beq    x0, a1, nothin    
    ### I replaced s2 with a1 and s3 with a2
    # calculate mid index
      srai     t0, a1, 1   #  (left + right) // 2 ### half = n / 2
    slli    t3, t0, 2   #  offset
    add    t6, t3, a0  #  BaseAddr of A + offset == A[mid]
    
      # If mid element == v
      lw     t4, 0(t6)  # this doesn't work tho!
      beq     t4, a2, mid_return
    
      # If     v < mid element
      blt     a2, t4, left_half


      # Else, search in right half
      
      #else {  // v > half_v
        #    // search the second half, excluding a[half]
        #    int left = half + 1;

        #    // &a[left] means the address of a[left]
        #    rv = binary_search(&a[left], n - left, v);

        #    if (rv >= 0) {
        #        rv += left;
        #    }
        #}
      addi     s1, t0, 1  # set left = midIdx + 1
      slli    t5, s1, 2  # * 4 (word)
      
      add    a0, t5, a0  # &a[left]
      sub    a1, a1, s1 # n - left
      
      jal     ra, binary_search
      
      bge    a0, x0, left_inc
      beq    x0, x0, f_exit

nothin:
    addi    a0, x0, -1
      beq    x0, x0, f_exit

mid_return:
      # set result to mid index
      addi     a0, t0, 0
      beq      x0, x0, f_exit ###idk why you had a jal here
     
left_half:
      # search in left half
      addi     a1, t0, 0  # set right = midIdx - 1  ### n = half. You could have that half = 0, in which case you would be setting
                                                     ###           n = -1 which would result in an infinite loop
      jal      ra, binary_search ### when using jal, you need to pass the return address
      beq      x0, x0, f_exit ### you need to add an instruction for going to exit for when the recursive call jumps back here
left_inc:
    add    a0, a0, s1
    # jal    ra, binary_search ### no recursive call here. just exit

f_exit:
      # restore return address 
      lw     s1, 0(sp)
      lw     ra, 4(sp)
      addi     sp, sp, 8  # restore sp
      jalr      x0, ra, 0  # and return a0
        
        
        
