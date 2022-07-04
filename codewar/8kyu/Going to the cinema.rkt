#lang racket
(provide movie)

(define (movie card ticket fraction)

  (define A 0)
  (define B card)

  (define (loop n new-ticket)
    (set! A (+ A ticket))
    (set! B (+ B new-ticket))
    (if (< (exact-ceiling B) A)
        n
        (loop (add1 n) (* new-ticket fraction))))

  (loop 1 (* ticket fraction))) 