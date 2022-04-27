"""
	(20 points)
	
	Add necessary code so that, when we run the program, the following output is generated. Do not change the given code. 
	All your code should be written in classes. Use polymorphism as much as possible.

		=> Istanbul
		=>	=> BU, University
		=>	=> ITU, University
		=>	=> DSI, HighSchool, German
		=>	=> GS, HighSchool, French
		=> Konya
		=>	=> Selcuk, University
		=>	=> KAL, HighSchool, English
		Distances:
		BU -> DSI = 10
		Selcuk -> ITU = 50
"""

m = MAP()
L1 = m.add_location(CITY("Istanbul"))
L5 = m.add_location(CITY("Konya"))

L2 = m.add_location(University(L1, "BU"))
L6 = m.add_location(University(L5, "Selcuk"))
L3 = m.add_location(University(L1, "ITU"))
L4 = m.add_location(HighSchool(L1, "DSI", "German"))
L7 = m.add_location(HighSchool(L1, "GS", "French"))
L8 = m.add_location(HighSchool(L5, "KAL", "English"))

m.set_distance(L2, L4, 10)
m.set_distance(L6, L3, 50)

m.print()
