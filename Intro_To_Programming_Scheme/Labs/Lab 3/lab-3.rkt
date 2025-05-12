;#1
(define (pell n)
    (cond ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (* 2 (pell (- n 1))) (pell (- n 2))))))
(define (find-pell n)
    (define (find-pell-iter max test)
    (if (and (< (pell test) max) (>= (pell (+ test 1)) max)) (pell test)
        (find-pell-iter max (+ test 1))))
  (find-pell-iter n 0))
(define (comp-pell n)
    (cond ((= n 0) 2)
        ((= n 1) 2)
        (else (+ (* 2 (comp-pell (- n 1))) (comp-pell (- n 2))))))
(define (sqrt-2-approx n)
    (/ (comp-pell n) (* 2 (pell n))))

;#2
(define (viete n)
    (define (numerator n)
    (if (= n 1) (sqrt 2)
        (sqrt (+ 2 (numerator (- n 1))))))
  (define (viete-iter n count total)
    (if (> count n) total
        (viete-iter n (+ count 1) (* total (/ (numerator count) 2)))))
  (viete-iter n 1 1))

;#3
(define (new-sqrt x n)
     (define (new-sqrt-iter x n count)
    (cond ((= count n) (+ 1 (/ (- x 1) (new-sqrt-iter x n (- count 1)))))
          ((= count 0) 2)
          (else (+ 2 (/ (- x 1) (new-sqrt-iter x n (- count 1)))))))
  (new-sqrt-iter x n n))

;#4
(define (m91 n)
  (if (> n 100) (- n 10)
      (m91 (m91 (+ n 11)))))

;#5
(define (iradius A B C)
  (let ((S (/ (+ A B C) 2)))
    (sqrt (/ (* (- S A) (- S B) (- S C)) S))
  )
)

;#6
(define (heron a b c)
  (let ((s (/ (+ a b c) 2)))
    (let ((sa (- s a))
          (sb (- s b))
          (sc (- s c)))
      (sqrt (* s sa sb sc))
    )
  )
)