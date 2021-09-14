from .DBMV_Mark import DBMV_Mark
from .ASCII_Chars import ASCII_Chars
from .CONVERSION_TYPE import CONVERSION_TYPE
from .ReadOptions import ReadOptions
from .UpdateOptions import UpdateOptions
from .NewOptions import NewOptions
from .DeleteOptions import DeleteOptions
from .SelectOptions import SelectOptions

"""
Class: OperationArguments
	Auxiliary static class with functions to obtain the 3 items of every LinkarSERVER operation.
		
	These items are: CUSTOMVARS, OPTIONS and INPUTDATA.
		
	Unit Separator character (31) is used as separator between these items.
		
	- CUSTOMVARS: String for database custom subroutines.
	- OPTIONS: The options of every operation.
	- INPUTDATA: The necessary data for perform every operation.
		
	CUSTOMVARS US_char OPTIONS US_char INPUTDATA
"""
class OperationArguments:

	"""
		Function: GetReadArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the Read operation.

		Arguments:
			filename - (string) File name to read.
			recordIds - (string) A list of item IDs to read, separated by the Record Separator character (30). Use StringFunctions.ComposeRecordIds to compose this string.
			dictionaries - (string) List of dictionaries to read, separated by space. If this list is not set, all fields are returned.
			readOptions - (<ReadOptions>) Object that defines the different reading options of the Function: Calculated, dictClause, conversion, formatSpec, originalRecords.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.

		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetReadArgs(filename, recordIds, dictionaries, readOptions, customVars):
		if not readOptions:
			readOptions = ReadOptions()

		options = readOptions.GetString()
		inputData = filename + DBMV_Mark.AM + recordIds + DBMV_Mark.AM + dictionaries
		return customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + inputData;

	"""
		Function: GetUpdateArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the GetUpdateArgs operation.

		Arguments:
			filename - (string) Name of the file being updated.
			records - (string) Buffer of record data to update. Inside this string are the recordIds, the modified records, and the originalRecords. Use StringFunctions.ComposeUpdateBuffer (Linkar.Strings library) function to compose this string.
			updateOptions - (<UpdateOptions>) Object with write options, including optimisticLockControl, readAfter, calculated, dictionaries, conversion, formatSpec, originalRecords.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.

		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetUpdateArgs(filename, records, updateOptions, customVars):
		if not updateOptions:
			updateOptions = UpdateOptions()

		options = updateOptions.GetString()
		inputData = filename + DBMV_Mark.AM + records
		
		return customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + inputData

	"""
		Function: GetUpdatePartialArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the GetUpdateArgs operation.
		
		Arguments:
			filename - (string) Name of the file being updated.
			records - (string) Buffer of record data to update. Inside this string are the recordIds, the modified records, and the originalRecords. Use StringFunctions.ComposeUpdateBuffer (Linkar.Strings library) function to compose this string.
			dictionaries - (string) List of dictionaries to write, separated by space. In MV output format is mandatory.
			updateOptions - (<UpdateOptions>) Object with write options, including optimisticLockControl, readAfter, calculated, dictionaries, conversion, formatSpec, originalRecords.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
		
		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetUpdatePartialArgs(filename, records, dictionaries, updateOptions, customVars):
		if not updateOptions:
			updateOptions = UpdateOptions()

		options = updateOptions.GetString()
		inputData = filename + DBMV_Mark.AM + records + ASCII_Chars.FS_str + dictionaries;
		return customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + inputData

	"""
		Function: GetNewArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the ResetCommonBlocks operation.
		
		Arguments:
			filename - (string) The file name where the records are going to be created.
			records - (string) Buffer of records to write. Inside this string are the recordIds, and the records. Use StringFunctions.ComposeNewBuffer (Linkar.Strings library) function to compose this string.
			newOptions - (<NewOptions>) Object with write options for the new record(s), including recordIdType, readAfter, calculated, dictionaries, conversion, formatSpec, originalRecords.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
		
		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetNewArgs(filename, records, newOptions, customVars):
		if not newOptions:
			newOptions = NewOptions()

		options = newOptions.GetString()
		inputData = filename + DBMV_Mark.AM + records
		return customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + inputData

	"""
		Function: GetDeleteArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the GetDeleteArgs operation.
		
		Arguments:
			filename - (string) The file name where the records are going to be deleted. DICT in case of deleting a record that belongs to a dictionary.
			records - (string) Buffer of records to be deleted. Use StringFunctions.ComposeDeleteBuffer (Linkar.Strings library) function to compose this string.
			deleteOptions - (<DeleteOptions>) Object with options to manage how records are deleted, including optimisticLockControl, recoverRecordIdType.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
		
		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetDeleteArgs(filename, records, deleteOptions, customVars):
		options = deleteOptions.GetString()
		inputData = filename + DBMV_Mark.AM + records
		return customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + inputData

	"""
		Function: GetSelectArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the GetSelectArgs operation.
		
		Arguments:
			filename - (string) Name of file on which the operation is performed. For example LK.ORDERS
			selectClause - (string) Statement fragment specifies the selection condition. For example WITH CUSTOMER = '1'
			sortClause - (string) Statement fragment specifies the selection order. If there is a selection rule, Linkar will execute a SSELECT, otherwise Linkar will execute a SELECT. For example BY CUSTOMER
			dictClause - (string) Space-delimited list of dictionaries to read. If this list is not set, all fields are returned. For example CUSTOMER DATE ITEM
			preSelectClause - (string) An optional command that executes before the main Select
			selectOptions - (<SelectOptions>) Object with options to manage how records are selected, including calculated, dictionaries, conversion, formatSpec, originalRecords, onlyItemId, pagination, regPage, numPage.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
		
		
		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetSelectArgs(filename, selectClause, sortClause, dictClause, preSelectClause, selectOptions, customVars):
		if not selectOptions:
			selectOptions = SelectOptions()

		options = selectOptions.GetString()
		inputData = filename + DBMV_Mark.AM + selectClause + DBMV_Mark.AM + sortClause + DBMV_Mark.AM + dictClause + DBMV_Mark.AM + preSelectClause
		return customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + inputData

	"""
		Function: GetSubroutineArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the GetSubroutineArgs operation.
		
		Arguments:
			subroutineName - (string) Name of BASIC subroutine to execute.
			argsNumber - (number) Number of arguments
			arguments - (string) The subroutine arguments list. Use StringFunctions.ComposeSubroutineArgs function to compose this string.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
		
		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetSubroutineArgs(subroutineName, argsNumber, args, customVars):
		options = ""
		inputData1 = subroutineName + DBMV_Mark.AM + str(argsNumber)
		inputData2 = args
		inputData = inputData1 + ASCII_Chars.FS_str + inputData2
		return customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + inputData

	"""
		Function: GetConversionArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the GetConversionArgs operation.
		
		Arguments:
			expression - (string) The data or expression to convert. May include MV marks (value delimiters), in which case the conversion will execute in each value obeying the original MV mark.
			code - (string) The conversion code. Must obey the Database conversions specifications.
			conversionOptions - (string) Indicates the conversion type, input or output: INPUT=ICONV(); OUTPUT=OCONV()
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
		
		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetConversionArgs(expression, code, conversionType, customVars):
		options = "I" if conversionType == CONVERSION_TYPE.INPUT else "O"
		inputData = code + ASCII_Chars.FS_str + expression
		return customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + inputData

	"""
		Function: GetFormatArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the GetFormatArgs operation.
		
		Arguments:
			expression - (string) The data or expression to format. If multiple values are present, the operation will be performed individually on all values in the expression.
			formatSpec - (string) Specified format
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
		
		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetFormatArgs(expression, formatSpec, customVars):
		options = ""
		inputData = formatSpec + ASCII_Chars.FS_str + expression
		return customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + inputData

	"""
		Function: GetDictionariesArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the GetDictionariesArgs operation.
		
		Arguments:
			filename - (string) File name
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
		
		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetDictionariesArgs(filename, customVars):
		options = ""
		return customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + filename

	"""
		Function: GetExecuteArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the GetExecuteArgs operation.
		
		Arguments:
			statement - (string) The command you want to execute in the Database.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
		
		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetExecuteArgs(statement,customVars):
		options = ""
		return customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + statement

	"""
		Function: GetSendCommandArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the GetSendCommandArgs operation.
		
		Arguments:
			command - (string) Content of the operation you want to send.
		
		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetSendCommandArgs(command):
		options = ""
		customVars = ""
		return customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + command

	"""
		Function: GetVersionArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the Version operation.
		
		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetVersionArgs():
		options = ""
		return "" + ASCII_Chars.US_str + options + ASCII_Chars.US_str + ""

	"""
		Function: GetLkSchemasArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the GetLkSchemasArgs operation.
		
		Arguments:
			lkSchemasOptions - (<LkSchemasOptions>) This object defines the different options in base of the asked Schema Type: LKSCHEMAS, SQLMODE o DICTIONARIES.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
		
		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetLkSchemasArgs(lkSchemasOptions, customVars):
		options = lkSchemasOptions.GetString()
		return  customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + ""

	"""
		Function: GetLkPropertiesArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the GetLkPropertiesArgs operation.
		
		Arguments:
			filename - (string) File name to LkProperties
			lkPropertiesOptions - (<LkPropertiesOptions>) This object defines the different options in base of the asked Schema Type: LKSCHEMAS, SQLMODE o DICTIONARIES.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
		
		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetLkPropertiesArgs(filename, lkPropertiesOptions, customVars):
		options = lkPropertiesOptions.GetString()
		return customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + filename

	"""
		Function: GetGetTableArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the GetGetTableArgs operation.
		
		Arguments:
			filename - (string) File or table name defined in Linkar Schemas. Table notation is: MainTable[.MVTable[.SVTable]]
			selectClause - (string) Statement fragment specifies the selection condition. For example WITH CUSTOMER = '1'
			dictClause - (string) Space-delimited list of dictionaries to read. If this list is not set, all fields are returned. For example CUSTOMER DATE ITEM
			sortClause - (string) Statement fragment specifies the selection order. If there is a selection rule Linkar will execute a SSELECT, otherwise Linkar will execute a SELECT. For example BY CUSTOMER
			tableOptions - (<TableOptions>) Detailed options to be used, including: rowHeaders, rowProperties, onlyVisibe, usePropertyNames, repeatValues, applyConversion, applyFormat, calculated, pagination, regPage, numPage.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
		
		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetGetTableArgs(filename, selectClause, dictClause, sortClause, tableOptions, customVars):
		options = tableOptions.GetString()
		inputData = filename + DBMV_Mark.AM + selectClause + DBMV_Mark.AM + dictClause + DBMV_Mark.AM + sortClause
		return customVars + ASCII_Chars.US_str + options + ASCII_Chars.US_str + inputData

	"""
		Function: GetResetCommonBlocksArgs
			Compose the 3 items (CUSTOMVARS, OPTIONS and INPUTDATA) of the ResetCommonBlocks operation.
		
		Returns:
			string
			
			A string ready to be used in <Linkar.LkExecuteDirectOperation> and <Linkar.LkExecutePersistentOperation>.
	"""
	@staticmethod
	def GetResetCommonBlocksArgs():
		options = ""
		return  "" + ASCII_Chars.US_str + options + ASCII_Chars.US_str + ""
