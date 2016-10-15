// Extract infoslide text

=IF(RegExMatch($I4,":.+:.+:"),
	TRIM(
		// 
		LEFT(
			// LEFT Arg1: String with round name, colon and 
			// trailing space removed

			// TRIM: Remove trailing space behind round name. Including 
			// as a TRIM because some people may not include spaces so 
			// hardcoding a +1 may result in errors.
			TRIM(  
				// Remove round name and colon
				RIGHT(
					// Cell that round name, motion, infoslide is in
					$I4,
					// Number of chars aside from round name and colon
					LEN($I4)-(FIND(":",$I4))
					)
				),

			// LEFT Arg 2: Number of characters we want

			// Find index of third colon
			FIND(":",$I4,FIND(":",$I4,FIND(":",$I4)+2)+2)
			-(FIND(":",$I4)+IF(EQ(RIGHT(LEFT($I4,FIND(":",$I4)+1))," "), 1, 0))-7)
		),
		"")
		
// 1. Remove the round name and colon.
// 2. Remove the motion (stuff behind the third colon)
// 3. Remove the word 'Motion'. -> May have exceptions.

// Hard-coding 1 vs checking for trailing space:
// Tradeoff between being more robust and being faster. In this
// case we don't care much about speed, so we always want something
// that is more robust.

// Hard-coded the word 'motion' because I can't be fudged right now.

// Motion

=IF(REGEXMATCH($I4,":.+:.+:"),TRIM(RIGHT($I4,LEN($I4)-FIND(":",$I4,FIND(":",$I4,FIND(":",$I4)+2)+2))),IF(RegExMatch($I4,":"),RIGHT($I4,LEN($I4)-FIND(":",$I4) - 1),""))


// If there is an infoslide
=IF(REGEXMATCH($I4,":.+:.+:"),

	// Take characters after third colon and remove trailing space
	TRIM(
		RIGHT($I4,
			LEN($I4)-FIND(":",$I4,
						FIND(":",$I4,
							FIND(":",$I4)
							+2)
						+2)
		)
	),

	// Else if there is a motion, 
	IF(RegExMatch($I4,":"),

		// take characters after first colon aside from trailing space
		TRIM(RIGHT($I4,LEN($I4)-FIND(":",$I4))),

		// else return an empty string
		"")
	)

// Round

// If there is a colon:
=IF(RegExMatch($I4,":"),

	// Return the text to the left of the colon
	LEFT($I4,FIND(":",$I4)-1),

	// Else return an empty string
	"")


// Round in one line
=IF(RegExMatch($I4,":"),LEFT($I4,FIND(":",$I4)-1),"")


// Infoslide


// Previous wrong version
// =IF(RegExMatch($I4,":.+:.+:"),TRIM(LEFT(TRIM(RIGHT($I4,LEN($I4)-(FIND(":",$I4)))),FIND(":",$I4,FIND(":",$I4,FIND(":",$I4)+2)+2)-(FIND(":",$I4)+IF(EQ(RIGHT(LEFT($I4,FIND(":",$I4)+1))," "),1,0))-7)),"")

// One line version
=IF(RegExMatch($I4,":.+:.+:"),TRIM(LEFT(TRIM(RIGHT($I4,LEN($I4)-(FIND(":",$I4,FIND(":",$I4)+2)))),FIND(":",$I4,FIND(":",$I4,FIND(":",$I4)+2)+2)-(FIND(":",$I4)+IF(EQ(RIGHT(LEFT($I4,FIND(":",$I4)+1))," "),1,0))-7)),"")

// Extract infoslide text

// If has infoslide
=IF(RegExMatch($I4,":.+:.+:"),


	TRIM(LEFT(
		
		// Remove round name, 'Infoslide:' equivalent and trailing space
		TRIM(RIGHT($I4,LEN($I4)-(FIND(":",$I4,FIND(":",$I4)+2)))),
		
		// Remove everything after third colon and remove 'Motion:'
		FIND(":",$I4,FIND(":",$I4,FIND(":",$I4)+2)+2)
		  -(FIND(":",$I4)+IF(EQ(RIGHT(LEFT($I4,FIND(":",$I4)+1))," "),1,0))
		  -7)
	),

	// If there is no infoslide, return an empty string.
	"")
