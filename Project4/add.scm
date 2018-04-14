;;define tax function;;
(define tax .06)

;;define add function which takes in a number and total;;
(define (add num total)
	(cond
		(
                        ;;checks if num is less than 0;;
			(< num 0)

                        ;;displays final total after tax;;
			(display "Total: $")
			(display (+ total (* total tax)))#t
		)
		(else
                        ;;prompts the user to enter a value;;
			(display "Enter Value: ")

                        ;;setting input value to x;;
			(let ((x (read)))

                        ;;recursivly calling add function with input value x;;
                        (add x (+ num total)))
		)
	)
)

;;main method funciton;;
(define (main)
        (add 0 0)
        (newline)
)

