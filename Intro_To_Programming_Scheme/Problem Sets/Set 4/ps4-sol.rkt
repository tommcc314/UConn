;#1
(define (sum term a next b)
  (if (> a b)
      0
      (+ (term a)
         (sum term (next a) next b))))
(define (harmonic n)
  (sum (lambda (x) (/ 1 x)) 1 (lambda (x) (+ x 1)) n))
(harmonic 20)
;#2
(define (product term a next b)
  (if (> a b)
      1
      (* (term a)
         (product term (next a) next b))))
(define (wallis-pi n)
  (product (lambda (x) (* (/ (* 2 x) (- (* 2 x) 1))
                          (/ (* 2 x) (+ (* 2 x) 1))))
           1 (lambda (x) (+ x 1)) n))
;(wallis-pi 200)
;#3
(define (frac-sum f g n)
  (define (frac-term f g n)
    (if (= (g n) 0) 0
        (/ (f n) (g n))))
  (define (sum-frac f g n end)
    (if (> n end) 0
        (+ (frac-term f g n) (sum-frac f g (+ n 1) end))))
  (sum-frac f g (- n) n))
;(frac-sum (lambda (x) (* x x x x)) (lambda (x) (* x x)) 5)

;#4
(define (der f h)
  (lambda (x) (/ (- (f (+ x h)) (f x)) h)))
(define (der-n f n h)
  (define (der-n-recursive f n h)
    (if (= n 0) f
        (der-n-recursive (der f h) (- n 1) h)))
  (der-n-recursive f n h))



;((der-n (lambda (x) (* x x)) 2 .001) 2)
;((der (lambda (x) (* x x)) .001) 2)


;#5
(define (newton f x n)
  (if (= n 0) x
      (newton f (- x (/ (f x) ((der f .01) x))) (- n 1))))
;(newton (lambda (x) (- (* 2 (expt x 2)) 1)) 4 5)
;(newton (lambda (x) (- (expt x 2) x 1)) 2 10)
;#6
(define (sum-term term a b)
  (if (> a b)
      0
      (+ (term a)
         (sum-term term (+ a 1) b))))
(define (simpson-integrate f a b n)
  (let ((delta-x (/ (- b a) n)))
    (define (xi i)
      (+ a (* i delta-x)))
    (* (/ delta-x 3) (sum-term (lambda (x) (cond ((= x 0) f (xi 0))
                                                 ((= x n) f (xi n))
                                                 ((= (modulo x 2) 1) (* 4 (f (xi x))))
                                                 (else (* 2 (f (xi x)))))) 0 n))))
;(simpson-integrate (lambda (x) (expt x 4)) 0 1 10)
                                                          
                                                          