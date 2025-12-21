# ChangeProcessor Object

## Description

The ChangeProcessor object is at the heart of Inventor's transaction and transcripting mechanism, exposed via its public API.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Execute](../ChangeProcessor/ChangeProcessor_Execute.md) | Executes the ChangeProcessor on the specified document. |
| [SetAffectedDocuments](../ChangeProcessor/ChangeProcessor_SetAffectedDocuments.md) | Sets the FullDocumentNames, and optionally the change types, of the documents that will be affected by this change. |
| [SetMessageDialogOptions](../ChangeProcessor/ChangeProcessor_SetMessageDialogOptions.md) | Method that specifies the buttons that should be available on the message dialog. |
| [SuppressChangeNotifications](../ChangeProcessor/ChangeProcessor_SuppressChangeNotifications.md) | Method that sets whether the changes notifications within this change processor should be suppressed or not. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ChangeProcessor/ChangeProcessor_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ChangeType](../ChangeProcessor/ChangeProcessor_ChangeType.md) | Gets and sets the type of change (shape edit, query only, etc.) that this ChangeProcessor will make. Defaults to the type set on the ChangeDefinition, but can be overridden. |
| [DisplayMessages](../ChangeProcessor/ChangeProcessor_DisplayMessages.md) | Read-write property that gets and sets whether or not to display error/warning messages during the change process. A value of False indicates that all the messages will be suppressed. Initially set to False. This property should be set before the Execute metho. |
| [GlobalChangeProcess](../ChangeProcessor/ChangeProcessor_GlobalChangeProcess.md) | Gets and sets whether or not to execute the change process as a global transaction (can be viewed as a top-level transaction). If True, a global transaction will be created. Initially False; this property should be set before the Execute method is called. |
| [GlobalChangeProcessAborted](../ChangeProcessor/ChangeProcessor_GlobalChangeProcessAborted.md) | Gets whether the global transaction for this change had to be aborted. This only applies if GlobalChangeProcess is True and an Execute is in progress. |
| [MergeWithPrevious](../ChangeProcessor/ChangeProcessor_MergeWithPrevious.md) | Gets and sets whether to merge this change process with the previously committed transaction. |
| [MessageDialogUserChoice](../ChangeProcessor/ChangeProcessor_MessageDialogUserChoice.md) | Read-only property that returns a ButtonTypeEnum value indicating the user’s choice in the message dialog. |
| [Parent](../ChangeProcessor/ChangeProcessor_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Transact](../ChangeProcessor/ChangeProcessor_Transact.md) | Gets and sets whether to execute the change process as a transacting one. A non-transacting change process cannot be undone or redone. |
| [Type](../ChangeProcessor/ChangeProcessor_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnExecute](../ChangeProcessor/ChangeProcessor_OnExecute.md) | Event that is fired when Inventor is in a state to accept changes to data. This is the event where the client application executes its logic on the specified document. |
| [OnReadFromScript](../ChangeProcessor/ChangeProcessor_OnReadFromScript.md) | Event that is fired in a replay scenario supplying the cached Inputs string. The client application interprets the inputs and converts them into meaningful data for use in the execution of logic in the OnExecute event. This event is always followed by the OnExecute event. |
| [OnTerminate](../ChangeProcessor/ChangeProcessor_OnTerminate.md) | Event that is fired when this ChangeProcessor is done being used for the current execution. |
| [OnWriteToScript](../ChangeProcessor/ChangeProcessor_OnWriteToScript.md) | Event that is fired before the execution of and commit of the change. The return string should be set with a formatted string of the arguments. The string may be persisted for eventual replay, such as a transcript replay. A semicolon (';') character should be considered a reserved character used as a separator between individual arguments. The recommended format would be a variable name value pair separated by an equal character, with arguments separated by semicolons. For example "Argument1Name=Value1;Argument2Name=Value2" |

## Accessed From

[ChangeDefinition.CreateChangeProcessor](../ChangeDefinition/ChangeDefinition_CreateChangeProcessor.md), [ChangeDefinition.OnReplay](../ChangeDefinition/ChangeDefinition_OnReplay.md)

## Version

Introduced in version 9
