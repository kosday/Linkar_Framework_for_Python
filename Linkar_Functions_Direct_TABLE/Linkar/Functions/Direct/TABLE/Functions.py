from Linkar_Functions_Direct.Linkar.Functions.Direct.DirectFunctions import DirectFunctions
from Linkar_Functions.Linkar.Functions import LinkarFunctions

"""
	Class: Functions
			These functions perform direct (without establishing permanent session) operations with output format type TABLE.
"""
class Functions:

	"""
		Function: LkSchemas
			Returns a list of all the Schemas defined in Linkar Schemas, or the EntryPoint account data files, with TABLE output format.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			lkSchemasOptions - (<LkSchemasOptions>) This object defines the different options in base of the asked Schema Type: LKSCHEMAS, SQLMODE o DICTIONARIES.
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

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions_Direct_TABLE.Linkar.Functions.Direct.TABLE.Functions import Functions as DirectFunctions		
			def MyLkSchemas():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.LkSchemas(credentials)
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))

				return result
		---
	"""
	@staticmethod
	def LkSchemas(credentialOptions, lkSchemasOptions=LinkarFunctions.LkSchemasOptions(), customVars="", receiveTimeout=0):
		return DirectFunctions.LkSchemas(credentialOptions, lkSchemasOptions, LinkarFunctions.DATAFORMATSCH_TYPE.TABLE, customVars, receiveTimeout)

	"""
		Function: LkProperties
			Returns the Schema properties list defined in Linkar Schemas or the file dictionaries, with TABLE output format.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			filename - (string) File name to LkProperties.
			lkPropertiesOptions - (<LkPropertiesOptions>) This object defines the different options in base of the asked Schema Type: LKSCHEMAS, SQLMODE o DICTIONARIES.
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

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions_Direct_TABLE.Linkar.Functions.Direct.TABLE.Functions import Functions as DirectFunctions
			def MyLkProperties():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.LkProperties(credentials, "LK.CUSTOMERS")
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))

				return result
		---
	"""
	@staticmethod
	def LkProperties(credentialOptions, filename, lkPropertiesOptions=LinkarFunctions.LkPropertiesOptions(), customVars="", receiveTimeout=0):
		return DirectFunctions.LkProperties(credentialOptions, filename, lkPropertiesOptions, LinkarFunctions.DATAFORMATSCH_TYPE.TABLE, customVars, receiveTimeout)

	"""
		Function: GetTable
			Returns a query result in a table format.
		
		Arguments:
			credentialOptions - (<CredentialOptions>) Object with data necessary to access the Linkar Server: Username, Password, EntryPoint, Language, FreeText.
			filename - (string) File or table name defined in Linkar Schemas. Table notation is: MainTable[.MVTable[.SVTable]]
			selectClause - (string) Statement fragment specifies the selection condition. For example WITH CUSTOMER = '1'
			dictClause - (string) Space-delimited list of dictionaries to read. If this list is not set, all fields are returned. For example CUSTOMER DATE ITEM. In NONE mode you may use the format LKFLDx where x is the attribute number.
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

		Example:
		--- Code
			from Linkar.Linkar import CredentialOptions
			from Linkar_Functions_Direct_TABLE.Linkar.Functions.Direct.TABLE.Functions import Functions as DirectFunctions
			def MyGetTable():
				try:
					credentials = CredentialOptions("127.0.0.1", "EPNAME", 11300, "admin", "admin")
					result = DirectFunctions.GetTable(credentials, "LK.CUSTOMERS")
				except Exception as ex:
					result = ""
					print("ERROR: " + str(ex))

				return result
		---
	"""
	@staticmethod
	def GetTable(credentialOptions, filename, selectClause="", dictClause="", sortClause="", tableOptions=LinkarFunctions.TableOptions(), customVars="", receiveTimeout=0):
		return DirectFunctions.GetTable(credentialOptions, filename, selectClause, dictClause, sortClause, tableOptions, customVars, receiveTimeout)
	