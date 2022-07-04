#lang racket

(provide past)
 
(define (past h m s)
  (* (+ (* h 60 60) (* m 60) s) 1000))