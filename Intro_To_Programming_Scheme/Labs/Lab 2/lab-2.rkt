(define (geom-series-np2 n)
  (geom-series-np2-iter n 0 0))
(define (geom-series-np2-iter max counter total)
  (if (> counter max) total
      (geom-series-np2-iter max (+ counter 1) (+ total (/ 1 (expt 2 counter))))))


;(geom-series-np2 6)

(define (num-digits n)
  (if (< (abs n) 10) 1
      (+ 1 (num-digits (/ n 10)))))
;(num-digits 10000)

(define (a n)
  (if (= n 0) 1
      (* 2 (a (- n 1)))))
;(ancestors 6)
(define (num-ancestors n)
  (if (= n 0) 0
      (+ (a n) (num-ancestors (- n 1)))))
;(num-ancestors 4)

(define (factorial n)
  (if (= n 0) 1
      (* n (factorial (- n 1)))))
;(factorial 5)
(define (n-choose-k n k)
  (cond ((and (= n 0) (= k 0)) 1)
        ((<= k 0) 1)
        ((< n k) 1)  
        (else (/ (factorial n) (* (factorial (- n k)) (factorial k))))))
;(n-choose-k 100 2)

(define (pascals-triangle n k)
  (cond ((< k 0) 0)
        ((< n k) 0)
        ((and (= n 0) (= k 0)) 1)
        (else (+ (pascals-triangle (- n 1) k) (pascals-triangle (- n 1) (- k 1))))))
;(pascals-triangle 2 1)
