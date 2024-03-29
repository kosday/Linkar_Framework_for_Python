"""
	enum: DATAFORMAT_TYPE
	Indicates in what format you want to receive the data resulting from the operation.
	For some operations, also the format in you want to send the data.
	There are 3 possible options: MV, XML and JSON.
	
	Defined constants of DATAFORMAT_TYPE:
	--- Code
		MV - 0x01
		XML - 0x02
		JSON - 0x03
	---
"""
class DATAFORMAT_TYPE:
	MV = 0x01
	XML = 0x02
	JSON = 0x03
