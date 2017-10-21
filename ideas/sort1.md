Program:	 	Input-outputexample	Description:
x?[int] 		Input:			XavierandYasminearelayingstickstoform non-overlapping
y?[int] 		[7 3 8 2 5],		rectangles on the ground. They both have ?xed sets
c?SORT x		[2 8 9 1 3]		of pairs of sticks of certain lengths (represented
d?SORT y 		Output:			as arrays x and y of numbers). Xavier only lays sticks
e?REVERSE d 		79			paralleltothexaxis,andYasminelayssticks only
f?ZIPWITH (*) d e 				parallel to y axis. Compute the area their
g?SUM f						rectangles will cover at least.