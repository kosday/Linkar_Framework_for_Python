from Linkar_Functions.Linkar.Functions import LinkarFunctions
from Linkar import Linkar

linkar = Linkar.Linkar()

"""
	Class: LinkarClient
		These functions perform synchronous persistent (establishing permanent session) operations with any kind of output format type.
		Property: SessionId
		string
		
		SessionID of the connection.
		Property: ReceiveTimeout
		number
		
		Maximum time in seconds that the client will wait for a response from the server.
		Default = 0 to wait indefinitely.
		When the receiveTimeout argument is omitted in any operation, the value set here will be applied.
"""
class LinkarClient:

	"""
		Constructor: __init__
			Initializes a new instance of the LinkarClient class.
			
		Arguments:
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely. When the receiveTimeout argument is omitted in any operation, the value set here will be applied.
	"""
	def __init__(self, receiveTimeout=0):
		self.SessionId = ""
		if receiveTimeout >= 0:
			self.ReceiveTimeout = receiveTimeout
		else:
			self.ReceiveTimeout = 0
		self.ConnectionInfo = None

	"""
		Function: Login
			Starts the communication with a server allowing making use of the rest of functions until the Logout method is executed or the connection with the server gets lost.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Remarks:
			Login is actually a "virtual" operation which creates a new Client Session ID. No DBMS login is performed unless Linkar SERVER determines new Database Sessions are required - these operations are not related.
	"""
	def Login(self, credentialOptions, customVars="", receiveTimeout=0):
		if self.ConnectionInfo is None:
			options = ""
			loginArgs = customVars if customVars else "" + LinkarFunctions.ASCII_Chars.US_chr + options
			byteOpCode = LinkarFunctions.OPERATION_CODE.LOGIN
			byteInputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
			byteOutputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
			receiveTimeout = receiveTimeout if receiveTimeout else 0
			
			if receiveTimeout <= 0 and self.ReceiveTimeout > 0:
				receiveTimeout = self.ReceiveTimeout

			connectionInfo = Linkar.ConnectionInfo("", "", "", credentialOptions)
			loginResult = linkar.LkExecutePersistentOperation(connectionInfo, byteOpCode, loginArgs, byteInputFormat, byteOutputFormat, receiveTimeout)
			if loginResult is not None or len(loginResult) > 0:
				self.ConnectionInfo = connectionInfo
				self.SessionId = connectionInfo.SessionId
			else:
				self.ConnectionInfo = None
				self.SessionId = None

	"""
		Function: Logout
			Closes the communication with the server, that previously has been opened with a Login function.
		
		Arguments:
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.</param>
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.</param>
		Remarks:
			Logout is actually a "virtual" operation which disposes the current Client Session ID. No DBMS logout is performed.
	"""
	def Logout(self, customVars="", receiveTimeout=0):
		logoutArgs = customVars if customVars else ""
		byteOpCode = LinkarFunctions.OPERATION_CODE.LOGOUT
		byteInputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		byteOutputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		receiveTimeout = receiveTimeout if receiveTimeout else 0
		if receiveTimeout <= 0 and self.ReceiveTimeout > 0:
			receiveTimeout = self.ReceiveTimeout

		logoutResult = linkar.LkExecutePersistentOperation(self.ConnectionInfo, byteOpCode, logoutArgs, byteInputFormat, byteOutputFormat, receiveTimeout)
		if logoutResult is not None or len(logoutResult) > 0:
			self.ConnectionInfo = None

	"""
		Function: Read
			Reads one or several records of a file.
			
		Arguments:
			filename - (string) File name to read.
			recordIds - (string) A list of item IDs to read.
			dictionaries - (string) List of dictionaries to read, separated by space. If this list is not set, all fields are returned.
			readOptions - (<ReadOptions>) Object that defines the different reading options of the Function: Calculated, dictClause, conversion, formatSpec, originalRecords.
			inputFormat - (<DATAFORMAT_TYPE>) Indicates in what format you wish to send the record ids: MV, XML or JSON.
			outputFormat - (<DATAFORMATCRU_TYPE>) Indicates in what format you want to receive the data resulting from the Read, New, Update and Select operations: MV, XML, XML_DICT, XML_SCH, JSON, JSON_DICT or JSON_SCH.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		Returns:
			string
		
			The results of the operation
	"""
	def Read(self, filename, recordIds, dictionaries="", readOptions=LinkarFunctions.ReadOptions(), inputFormat=LinkarFunctions.DATAFORMAT_TYPE.MV, outputFormat=LinkarFunctions.DATAFORMATCRU_TYPE.MV, customVars="", receiveTimeout=0):
		opArgs = LinkarFunctions.OperationArguments.GetReadArgs(filename, recordIds, dictionaries, readOptions, customVars)
		opCode = LinkarFunctions.OPERATION_CODE.READ
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)

	"""
		Function: Update
			Update one or several records of a file.
			
		Arguments:
			filename - (string) Name of the file being updated.
			records - (string) Buffer of record data to update. Inside this string are the recordIds, the modified records, and the originalRecords.
			updateOptions - (<UpdateOptions>) Object with write options, including optimisticLockControl, readAfter, calculated, dictionaries, conversion, formatSpec, originalRecords.
			inputFormat - (<DATAFORMAT_TYPE>) Indicates in what format you wish to send the resultant writing data: MV, XML or JSON.
			outputFormat - (<DATAFORMATCRU_TYPE>) Indicates in what format you want to receive the data resulting from the Read, New, Update and Select operations: MV, XML, XML_DICT, XML_SCH, JSON, JSON_DICT or JSON_SCH.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.	
		Returns:
			string
		
			The results of the operation.
			
		Remarks:
		Inside the records argument, the recordIds and the modified records always must be specified. But the originalRecords not always.
		When <UpdateOptions> argument is specified and the <UpdateOptions.OptimisticLockControl> property is set to true, a copy of the record must be provided before the modification (originalRecords argument)
		to use the Optimistic Lock technique. This copy can be obtained from a previous <Read> operation. The database, before executing the modification, 
		reads the record and compares it with the copy in originalRecords, if they are equal the modified record is executed.
		But if they are not equal, it means that the record has been modified by other user and its modification will not be saved.
		The record will have to be read, modified and saved again.
	"""
	def Update(self, filename, records, updateOptions=LinkarFunctions.UpdateOptions(), inputFormat=LinkarFunctions.DATAFORMAT_TYPE.MV, outputFormat=LinkarFunctions.DATAFORMATCRU_TYPE.MV, customVars="", receiveTimeout=0):
		opArgs = LinkarFunctions.OperationArguments.GetUpdateArgs(filename, records, updateOptions, customVars)
		opCode = LinkarFunctions.OPERATION_CODE.UPDATE
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)

	"""
		Function: UpdatePartial
			Update one or more attributes of one or more file records.
			
		Arguments:
			filename - (string) Name of the file being updated.
			records - (string) Buffer of record data to update. Inside this string are the recordIds, the modified records, and the originalRecords.
			dictionaries - (string) List of dictionaries to write, separated by space. In MV output format is mandatory. You may use the format LKFLDx where x is the attribute number.
			updateOptions - (<UpdateOptions>) Object with write options, including optimisticLockControl, readAfter, calculated, dictionaries, conversion, formatSpec, originalRecords.
			inputFormat - (<DATAFORMAT_TYPE>) Indicates in what format you wish to send the resultant writing data: MV, XML or JSON.
			outputFormat - (<DATAFORMATCRU_TYPE>) Indicates in what format you want to receive the data resulting from the Read, New, Update and Select operations: MV, XML, XML_DICT, XML_SCH, JSON, JSON_DICT or JSON_SCH.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		Returns:
			string
		
			The results of the operation.
		Remarks:
			Inside the records argument, the recordIds and the modified records always must be specified. But the originalRecords not always.
			When <UpdateOptions> argument is specified and the <UpdateOptions.OptimisticLockControl> property is set to true, a copy of the record must be provided before the modification (originalRecords argument)
			to use the Optimistic Lock technique. This copy can be obtained from a previous <Read> operation. The database, before executing the modification, 
			reads the record and compares it with the copy in originalRecords, if they are equal the modified record is executed.
			But if they are not equal, it means that the record has been modified by other user and its modification will not be saved.
			The record will have to be read, modified and saved again.
	"""
	def UpdatePartial(self, filename, records, dictionaries, updateOptions=LinkarFunctions.UpdateOptions(), inputFormat=LinkarFunctions.DATAFORMAT_TYPE.MV, outputFormat=LinkarFunctions.DATAFORMATCRU_TYPE.MV, customVars="", receiveTimeout=0):
		opArgs = LinkarFunctions.OperationArguments.GetUpdatePartialArgs(filename, records, dictionaries, updateOptions, customVars)
		opCode = LinkarFunctions.OPERATION_CODE.UPDATEPARTIAL
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)

	"""
		Function: New
			Creates one or several records of a file.
		
		Arguments:
			filename - (string) The file name where the records are going to be created.
			records - (string) Buffer of records to write. Inside this string are the recordIds, and the records.
			newOptions - (<NewOptions>) Object with write options for the new record(s), including recordIdType, readAfter, calculated, dictionaries, conversion, formatSpec, originalRecords.
			inputFormat - (<DATAFORMAT_TYPE>) Indicates in what format you wish to send the resultant writing data: MV, XML or JSON.
			outputFormat - (<DATAFORMATCRU_TYPE>) Indicates in what format you want to receive the data resulting from the Read, New, Update and Select operations: MV, XML, XML_DICT, XML_SCH, JSON, JSON_DICT or JSON_SCH.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
		Remarks:
			Inside the records argument, the records always must be specified.
			But the recordIds only must be specified when <NewOptions> argument is NULL, or when the <RecordIdType> argument of the <NewOptions> constructor is NULL.
	"""
	def New(self, filename, records, newOptions=LinkarFunctions.NewOptions(), inputFormat=LinkarFunctions.DATAFORMAT_TYPE.MV, outputFormat=LinkarFunctions.DATAFORMATCRU_TYPE.MV, customVars="", receiveTimeout=0):
		opArgs = LinkarFunctions.OperationArguments.GetNewArgs(filename, records, newOptions, customVars)
		opCode = LinkarFunctions.OPERATION_CODE.NEW
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)

	"""
		Function: Delete
			Deletes one or several records in file.
		
		Arguments:
			filename - (string) The file name where the records are going to be created.
			records - (string) Buffer of records to be deleted.
			deleteOptions - (<DeleteOptions>) Object with options to manage how records are deleted, including optimisticLockControl, recoverRecordIdType.
			inputFormat - (<DATAFORMAT_TYPE>) Indicates in what format you wish to send the resultant writing data: MV, XML or JSON.
			outputFormat - (<DATAFORMAT_TYPE>) Indicates in what format you want to receive the data resulting from the operation: MV, XML or JSON.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		Returns:
			string
			
			The results of the operation.
			
		Remarks:
			Inside the records argument, the recordIds always must be specified. But the originalRecords not always.
			When <deleteOptions> argument is specified and the <DeleteOptions.OptimisticLockControl> property is set to true,
			a copy of the record must be provided before the deletion to use the Optimistic Lock technique.
			This copy can be obtained from a previous <Read> operation. The database, before executing the deletion, 
			reads the record and compares it with the copy in originalRecords, if they are equal the record is deleted.
			But if they are not equal, it means that the record has been modified by other user and the record will not be deleted.
			The record will have to be read, and deleted again.
	"""
	def Delete(self, filename, records, deleteOptions=LinkarFunctions.DeleteOptions(), inputFormat=LinkarFunctions.DATAFORMAT_TYPE.MV, outputFormat=LinkarFunctions.DATAFORMAT_TYPE.MV, customVars="", receiveTimeout=0):
		opArgs = LinkarFunctions.OperationArguments.GetDeleteArgs(filename, records, deleteOptions, customVars)
		opCode = LinkarFunctions.OPERATION_CODE.DELETE
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)

	"""
		Function: Select
			Executes a Query in the Database.
		
		Arguments:
			filename - (string) Name of file on which the operation is performed. For example LK.ORDERS
			selectClause - (string) Statement fragment specifies the selection condition. For example WITH CUSTOMER = '1'
			sortClause - (string) Statement fragment specifies the selection order. If there is a selection rule, Linkar will execute a SSELECT, otherwise Linkar will execute a SELECT. For example BY CUSTOMER
			dictClause - (string) Space-delimited list of dictionaries to read. If this list is not set, all fields are returned. For example CUSTOMER DATE ITEM
			preSelectClause - (string) An optional command that executes before the main Select
			selectOptions - (<SelectOptions>) Object with options to manage how records are selected, including calculated, dictionaries, conversion, formatSpec, originalRecords, onlyItemId, pagination, regPage, numPage.
			outputFormat - (<DATAFORMATCRU_TYPE>) Indicates in what format you want to receive the data resulting from the Read, New, Update and Select operations: MV, XML, XML_DICT, XML_SCH, JSON, JSON_DICT or JSON_SCH.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
			
		Remarks:
			In the preSelectClause argument these operations can be carried out before executing the Select statement:
			
				- Previously call to a saved list with the GET.LIST command to use it in the Main Select input
				- Make a previous Select to use the result as the Main Select input, with the SELECT or SSELECT commands.In this case the entire sentence must be indicated in the PreselectClause. For example:SSELECT LK.ORDERS WITH CUSTOMER = '1'
				- Exploit a Main File index to use the result as a Main Select input, with the SELECTINDEX command. The syntax for all the databases is SELECTINDEX index.name.value. For example SELECTINDEX ITEM,"101691"
	"""
	def Select(self, filename, selectClause, sortClause, dictClause, preSelectClause, selectOptions=LinkarFunctions.SelectOptions(), outputFormat=LinkarFunctions.DATAFORMATCRU_TYPE.MV, customVars="", receiveTimeout=0):
		opArgs = LinkarFunctions.OperationArguments.GetSelectArgs(filename, selectClause, sortClause, dictClause, preSelectClause, selectOptions, customVars)
		opCode = LinkarFunctions.OPERATION_CODE.SELECT
		inputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)

	"""
		Function: Subroutine
			Executes a subroutine.
		
		Arguments:
			subroutineName - (string) Name of BASIC subroutine to execute.
			argsNumber - (number) Number of arguments.
			arguments - (string) The subroutine arguments list. Each argument is a substring separated with the ASCII char DC4 (20).
			inputFormat - (<DATAFORMAT_TYPE>) Indicates in what format you wish to send the subroutine arguments: MV, XML or JSON.
			outputFormat - (<DATAFORMAT_TYPE>) Indicates in what format you want to receive the data resulting from the operation: MV, XML or JSON.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
	"""
	def Subroutine(self, subroutineName, argsNumber, args, inputFormat=LinkarFunctions.DATAFORMAT_TYPE.MV, outputFormat=LinkarFunctions.DATAFORMAT_TYPE.MV, customVars="", receiveTimeout=0):
		opArgs = LinkarFunctions.OperationArguments.GetSubroutineArgs(subroutineName, argsNumber, args, customVars)
		opCode = LinkarFunctions.OPERATION_CODE.SUBROUTINE
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)

	"""
		Function: Conversion
			Returns the result of executing ICONV() or OCONV() functions from a expression list in the Database.
		
		Arguments:
			conversionType - (<CONVERSION_TYPE>) Indicates the conversion type, input or output: INPUT=ICONV() OUTPUT=OCONV()
			expression - (string) The data or expression to convert. May include MV marks (value delimiters), in which case the conversion will execute in each value obeying the original MV mark.
			code - (string) The conversion code. Must obey the Database conversions specifications.
			outputFormat - (<DATAFORMAT_TYPE>) Indicates in what format you want to receive the data resulting from the operation: MV, XML or JSON.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
	"""
	def Conversion(self, conversionType, expression, code, outputFormat=LinkarFunctions.DATAFORMAT_TYPE.MV, customVars="", receiveTimeout=0):
		opArgs = LinkarFunctions.OperationArguments.GetConversionArgs(expression, code, conversionType, customVars)      
		opCode = LinkarFunctions.OPERATION_CODE.CONVERSION
		inputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)

	"""
		Function: Format
			Returns the result of executing the FMT function in a expressions list in the Database.
		
		Arguments:
			expression - (string) The data or expression to format. If multiple values are present, the operation will be performed individually on all values in the expression.
			formatSpec - (string) Specified format.
			outputFormat - (<DATAFORMAT_TYPE>) Indicates in what format you want to receive the data resulting from the operation: MV, XML or JSON.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
	"""
	def Format(self, expression, formatSpec, outputFormat=LinkarFunctions.DATAFORMAT_TYPE.MV, customVars="", receiveTimeout=0):
		opArgs = LinkarFunctions.OperationArguments.GetFormatArgs(expression, formatSpec, customVars)      
		opCode = LinkarFunctions.OPERATION_CODE.FORMAT
		inputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)

	"""
		Function: Dictionaries
			Returns all the dictionaries of a file.
		
		Arguments:
			filename - (string) File name.
			outputFormat - (<DATAFORMAT_TYPE>) Indicates in what format you want to receive the data resulting from the operation: MV, XML or JSON.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
	"""
	def Dictionaries(self, filename, outputFormat=LinkarFunctions.DATAFORMAT_TYPE.MV, customVars="", receiveTimeout=0):
		opArgs = LinkarFunctions.OperationArguments.GetDictionariesArgs(filename, customVars)      
		opCode = LinkarFunctions.OPERATION_CODE.DICTIONARIES
		inputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)

	"""
		Function: Execute
			Allows the execution of any command from the Database.
		
		Arguments:
			statement - (string) The command you want to execute in the Database.
			outputFormat - (<DATAFORMAT_TYPE>) Indicates in what format you want to receive the data resulting from the operation: MV, XML or JSON.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
	"""
	def Execute(self, statement, outputFormat=LinkarFunctions.DATAFORMAT_TYPE.MV, customVars="", receiveTimeout=0):
		opArgs = LinkarFunctions.OperationArguments.GetExecuteArgs(statement, customVars)
		opCode = LinkarFunctions.OPERATION_CODE.EXECUTE
		inputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)

	"""
		Function: GetVersion
			Allows getting the server version.
		
		Arguments:
			outputFormat - (<DATAFORMAT_TYPE>) Indicates in what format you want to receive the data resulting from the operation: MV, XML or JSON.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
		
		Remarks:
			This function returns the following information:
			
				LKMVCOMPONENTSVERSION - MV Components version.
				LKSERVERVERSION - Linkar SERVER version.
				LKCLIENTVERSION - Used client library version.
				DATABASE - Database.
				OS - Operating system.
				DATEZERO - Date zero base in YYYYMMDD format.
				DATEOUTPUTCONVERSION - Output conversion for date used by Linkar Schemas.
				TIMEOUTPUTCONVERSION - Output conversion for time used by Linkar Schemas.
				MVDATETIMESEPARATOR - DateTime used separator used by Linkar Schemas, for instance 18325,23000.
				MVBOOLTRUE - Database used char for the Boolean true value used by Linkar Schemas.
				MVBOOLFALSE - Database used char for the Boolean false value used by Linkar Schemas.
				OUTPUTBOOLTRUE - Used char for the Boolean true value out of the database used by Linkar Schemas.
				OUTPUTBOOLFALSE - Used char for the Boolean false value out of the database used by Linkar Schemas.
				MVDECIMALSEPARATOR - Decimal separator in the database. May be point, comma or none when the database does not store decimal numbers. Used by Linkar Schemas.
				OTHERLANGUAGES - Languages list separated by commas.
				TABLEROWSEPARATOR - It is the decimal char that you use to separate the rows in the output table format. By default 11.
				TABLECOLSEPARATOR - It is the decimal char that you use to separate the columns in the output table format. By default 9.
				CONVERTNUMBOOLJSON - Switch to create numeric and boolean data in JSON strings. Default is false.
	"""
	def GetVersion(self, outputFormat=LinkarFunctions.DATAFORMAT_TYPE.MV, receiveTimeout=0):
		opArgs = LinkarFunctions.OperationArguments.GetVersionArgs()        
		opCode = LinkarFunctions.OPERATION_CODE.GETVERSION
		inputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)

	"""
		Function: LkSchemas
			Returns a list of all the Schemas defined in Linkar Schemas, or the EntryPoint account data files.
		
		Arguments:
			lkSchemasOptions - (<LkSchemasOptions>) This object defines the different options in base of the asked Schema Type: LKSCHEMAS, SQLMODE o DICTIONARIES.
			outputFormat - (<DATAFORMATSCH_TYPE>) Indicates in what format you want to receive the data resulting from the operation: MV, XML, JSON or TABLE.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
		
		Remarks:
			TABLE output format uses the defined control characters in <EntryPoints Parameters: http://kosday.com/Manuals/en_web_linkar/lk_schemas_ep_parameters.html> Table Row Separator and Column Row Separator.
			
			By default:
			
				TAB - char (9) for columns.
				VT - char (11) for rows.
	"""
	def LkSchemas(self, lkSchemasOptions=LinkarFunctions.LkSchemasOptions(), outputFormat=LinkarFunctions.DATAFORMATSCH_TYPE.MV, customVars="", receiveTimeout=0):
		opArgs = LinkarFunctions.OperationArguments.GetLkSchemasArgs(lkSchemasOptions, customVars)
		opCode = LinkarFunctions.OPERATION_CODE.LKSCHEMAS
		inputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)

	"""
		Function: LkProperties
			Returns the Schema properties list defined in Linkar Schemas or the file dictionaries.
		
		Arguments:
			filename - (string) File name to LkProperties.
			lkPropertiesOptions - (<LkPropertiesOptions>) This object defines the different options in base of the asked Schema Type: LKSCHEMAS, SQLMODE o DICTIONARIES.
			outputFormat - (<DATAFORMATSCHPROP_TYPE>) Indicates in what format you want to receive the data resulting from the operation: MV, XML, XML_DICT, XML_SCH, JSON, JSON_DICT, JSON_SCH or TABLE.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
		
		Remarks:
			TABLE output format uses the defined control characters in <EntryPoints Parameters: http://kosday.com/Manuals/en_web_linkar/lk_schemas_ep_parameters.html> Table Row Separator and Column Row Separator.
			
			By default:
			
				TAB - char (9) for columns.
				VT - char (11) for rows.
	"""
	def LkProperties(self, filename, lkPropertiesOptions=LinkarFunctions.LkPropertiesOptions(),	outputFormat=LinkarFunctions.DATAFORMATSCHPROP_TYPE.MV, customVars="", receiveTimeout=0):
		opArgs = LinkarFunctions.OperationArguments.GetLkPropertiesArgs(filename, lkPropertiesOptions, customVars)
		opCode = LinkarFunctions.OPERATION_CODE.LKPROPERTIES
		inputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV	
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)

	"""
		Function: GetTable
			Returns a query result in a table format.
		
		Arguments:
			filename - (string) File or table name defined in Linkar Schemas. Table notation is: MainTable[.MVTable[.SVTable]]
			selectClause - (string) Statement fragment specifies the selection condition. For example WITH CUSTOMER = '1'
			dictClause - (string) Space-delimited list of dictionaries to read. If this list is not set, all fields are returned. For example CUSTOMER DATE ITEM
			sortClause - (string) Statement fragment specifies the selection order. If there is a selection rule Linkar will execute a SSELECT, otherwise Linkar will execute a SELECT. For example BY CUSTOMER
			tableOptions - (<TableOptions>) Detailed options to be used, including: rowHeaders, rowProperties, onlyVisibe, usePropertyNames, repeatValues, applyConversion, applyFormat, calculated, pagination, regPage, numPage.
			customVars - (string) Free text sent to the database allows management of additional behaviours in SUB.LK.MAIN.CONTROL.CUSTOM, which is called when this parameter is set.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
		
		Remarks:
			TABLE output format uses the defined control characters in <EntryPoints Parameters: http://kosday.com/Manuals/en_web_linkar/lk_schemas_ep_parameters.html> Table Row Separator and Column Row Separator.
			
			By default:
			
				TAB - char (9) for columns.
				VT - char (11) for rows.
	"""
	def GetTable(self, filename, selectClause="", dictClause="", sortClause="", tableOptions=LinkarFunctions.TableOptions(), customVars="", receiveTimeout=0):
		opArgs = LinkarFunctions.OperationArguments.GetGetTableArgs(filename, selectClause, dictClause, sortClause, tableOptions, customVars)
		opCode = LinkarFunctions.OPERATION_CODE.GETTABLE
		inputFormat = LinkarFunctions.DATAFORMATSCH_TYPE.MV
		outputFormat = LinkarFunctions.DATAFORMATSCH_TYPE.TABLE
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)

	"""
		Function: ResetCommonBlocks
			Resets the COMMON variables with the 100 most used files.
		
		Arguments:
			outputFormat - (<DATAFORMAT_TYPE>) Indicates in what format you want to receive the data resulting from the operation: MV, XML or JSON.
			receiveTimeout - (number) Maximum time in seconds that the client will wait for a response from the server. Default = 0 to wait indefinitely.
		
		Returns:
			string
			
			The results of the operation.
	"""
	def ResetCommonBlocks(self, outputFormat=LinkarFunctions.DATAFORMAT_TYPE.MV, receiveTimeout=0):
		opArgs = LinkarFunctions.OperationArguments.GetResetCommonBlocksArgs()
		opCode = LinkarFunctions.OPERATION_CODE.RESETCOMMONBLOCKS
		inputFormat = LinkarFunctions.DATAFORMAT_TYPE.MV
		return linkar.LkExecutePersistentOperation(self.ConnectionInfo, opCode, opArgs, inputFormat, outputFormat, receiveTimeout)