from .DBMV_Mark import DBMV_Mark
from .RecoverIdType import RecoverIdType

"""
	Class: DeleteOptions
		Object that works as an argument in Delete function and defines the function options.
		
	Property: OptimisticLockControl
		boolean
		
		In the execution of the Delete function, before updating the record, checks out if the record has not been modified by other user.
		
	Remarks:
		If the OptimisticLockControl property is set to true, a copy of the record must be provided before the deletion (originalRecords argument)
		to use the Optimistic Lock technique. This copy can be obtained from a previous Read operation. The database, before executing the modification, 
		reads the record and compares it with the copy in originalRecords, if they are equal the deleted record is executed.
		But if they are not equal, it means that the record has been modified by other user and the record will not be deleted.
		The record will have to be read, and delete again.
		
	Property: ActiveTypeLinkar
		boolean
		
		Indicates that the RecoverIdType *Linkar* is enabled.
		
	Property: ActiveTypeCustom
		boolean
		
		Indicates that the RecoverIdType *Custom* is enabled.
		
	Property: Prefix
		string
		(For RecoverIdType *Linkar*)
		A prefix to the code.
	
	Property: Separator
		string
		
		(For RecoverIdType *Linkar*)
		 The separator between the prefix and the code.
		 The allowed separators list is: ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~
"""
class DeleteOptions:
	"""
		Constructor: __init__
			Initializes a new instance of the DeleteOptions class
		
		Arguments:
			optimisticLockControl - (boolean) In the execution of the Delete function, before updating the record, checks out if the record has not been modified by other user. See <OptimisticLock> property.
			recoverIdType - (<RecoverIdType>) Specifies the recovery technique for deleted item IDs.
	"""
	def __init__(self, optimisticLockControl = False, recoverIdType = RecoverIdType()):
		self.OptimisticLockControl = optimisticLockControl
		self.RecoverIdType = recoverIdType
		if not self.RecoverIdType:
			self.RecoverIdType = RecoverIdType()

		self.ActiveTypeLinkar = self.RecoverIdType.ActiveTypeLinkar
		self.Prefix = self.RecoverIdType.Prefix
		self.Separator = self.RecoverIdType.Separator
		self.ActiveTypeCustom = self.RecoverIdType.ActiveTypeCustom

	"""
		Function: GetString
			Composes the Delete options string for processing through LinkarSERVER to the database.
		
		Returns:
			string
			
			The string ready to be used by LinkarSERVER.
	"""
	def GetString(self):
		return ("1" if self.OptimisticLockControl else "0") + DBMV_Mark.AM_str + self.RecoverIdType.GetStringAM()