"""
	enum: DATAFORMATCRU_TYPE
	Specify the output formats of Read, Update, New and Select operations.
	Used only by LkRead, LkUpdate, LkNew and LkSelect
	There are 7 possible options: MV, XML, XML_DICT, XML_SCH, JSON, JSON_DICT and JSON_SCH.
		
	Defined constants of DATAFORMATCRU_TYPE:
	--- Code
		MV - 0x01
		XML - 0x02
		JSON - 0x03
		XML_DICT - 0x05
		XML_SCH - 0x06
		JSON_DICT - 0x07
		JSON_SCH - 0x08
	---
"""
class DATAFORMATCRU_TYPE:
	MV = 0x01
	XML = 0x02
	JSON = 0x03
	XML_DICT = 0x05
	XML_SCH = 0x06
	JSON_DICT = 0x07
	JSON_SCH = 0x08
