;#1
(define (fizzbuzz x)
  (cond ((and (= (modulo x 3) 0) (= (modulo x 5) 0)) "fizzbuzz")
        ((= (modulo x 3) 0) "fizz")
        ((= (modulo x 5) 0) "buzz")
        (else x)))
;(fizzbuzz 56)
(define (fizz x)
  (if (= (modulo x 3) 0) "fizz" ""))
(define (buzz x)
  (if (= (modulo x 5) 0) "buzz" ""))
(define (fizzbuzz2 x)
  (if (and (equal? (fizz x) "") (equal? (buzz x) ""))
      x
      (string-append (fizz x) (buzz x))))
;(fizzbuzz2 15)

;#2
(define pi 3.142)
(define (piecewise x)
  (cond ((> x (* 2 pi)) (- x (* 2 pi)))
        ((>= x (- pi)) (sin x))
        (else (- (- x) pi))))
;(piecewise -4)

;#3
(define (inc x) (+ x 1))
(define (dec x) (- x 1))
(define (add n m)
  (if (= m 0)
      n
      (add (inc n) (dec m))))
;(add 17 19)

;#4
(define (mult n m)
  (mult-iter n m 0))
(define (mult-iter n counter product) 
  (if (= counter 0)
      product
      (mult-iter n (dec counter) (add n product))))
  ;(cond ((= n 0) 0)
        ;(else (add m (mult (dec n) m)))))
;(mult 7 3)

;#5
(define (power b n)
  (expt-iter b n 1))
(define (expt-iter b counter product)
  (if (= counter 0)
      product
      (expt-iter b (dec counter) (mult b product))))
;(power 3 8)
;#6
(define (raise x n)
  (cond ((= n 0) 1)
        ((even? n) (mult (raise x (/ n 2)) (raise x (/ n 2))))
        (else (mult x (mult (raise x (floor (/ n 2)))
                      (raise x (floor (/ n 2))))))))
;(raise 4 4)

;#7
(define (pmult x y)
  (pmult-iter x y 0))
(define (pmult-iter x y total)
  (cond ((= x 0) 0)
        ((= y 0) 0)
        ((= x 1) (+ total y))
        (else (pmult-iter (floor (/ x 2)) (* y 2)
                          (if (even? x) total (+ total y))))))
;(pmult 15 8)

;#8
(define (sumEven n)
  (if (= (modulo n 2) 0) (sumEven-iter n)
      (sumEven-iter (- n 1))))
(define (sumEven-iter n)
  (if (= n 0)
      0
      (+ n (sumEven-iter (- n 2)))))
;(sumEven 11)
(define (sumOdd n)
  (cond ((= n 0) 0)
        ((= (modulo n 2) 0) (sumOdd-iter (- n 1)))
        (else (sumOdd-iter n))))
(define (sumOdd-iter n)
  (if (= n 1) 1
      (+ n (sumOdd-iter (- n 2)))))
;(sumOdd 10)

;#9
(define (h-product k)
  (cond ((= k 0) 0)
        ((= k 1) 1)
        ((= k 2) 0.5)
        (else (* (- 1 (/ 1 k))(h-product (- k 1))))))
;(h-product 0)

;#10
(define (divides a b) (= 0 (modulo b a)))
(define (divisors n) (divisors-upto n n))
(define (divisors-upto n k)
  (cond ((= 0 k) 0)
        ((= 0 n) 0)
        ((= 1 k) 1)
        ((divides k n) (+ 1 (divisors-upto n (- k 1))))
        (else (divisors-upto n (- k 1)))))
;(divisors 120)

;#11
(define (subfact n)
  (cond ((= 0 n) 1)
        ((= 1 n) 0)
        (else (* (- n 1) (+ (subfact (- n 1)) (subfact (- n 2)))))))
;(subfact 7)

;#12
(define (factorial x)
  (define (fact-iter a product)
	(if (= a 0)
		product
		(fact-iter (- a 1) (* product a))))
  (fact-iter x 1))
;(factorial 9)
(define (new-cos x n)
  (new-cos-iter x n 0))
(define (new-cos-iter x n total)
  (if (= n 0) (+ total 1)
      (new-cos-iter x (- n 1)
                       (+ total (* (expt -1 n)
                                   (/ (expt x (* 2 n)) (factorial (* 2 n))))))))
;(new-cos 3 5)