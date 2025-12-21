# ErrorManager Object

## Description

The ErrorManager object contains methods and properties to get errors and warnings that occurred during an API call, add to Inventor's errors or to display them.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddMessage](../ErrorManager/ErrorManager_AddMessage.md) | Method that adds a new message at the current level in the message tree. |
| [Clear](../ErrorManager/ErrorManager_Clear.md) | Method that clears all errors and warnings. This method returns a failure if there are any active message sections (indicated by the IsMessageSectionActive property). |
| [Show](../ErrorManager/ErrorManager_Show.md) | Method that displays the current error/warning or the stack of errors/warnings to the user. |
| [StartMessageSection](../ErrorManager/ErrorManager_StartMessageSection.md) | Method that starts a message section and returns a MessageSection object which can be used to clear, adopt or retain error/warning messages created during the section. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllMessages](../ErrorManager/ErrorManager_AllMessages.md) | Property that returns an XML string containing all messages (errors and warnings). |
| [Application](../ErrorManager/ErrorManager_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [HasErrors](../ErrorManager/ErrorManager_HasErrors.md) | Property that returns whether there are any recorded errors. |
| [HasWarnings](../ErrorManager/ErrorManager_HasWarnings.md) | Property that returns whether there are any recorded warnings. |
| [IsMessageSectionActive](../ErrorManager/ErrorManager_IsMessageSectionActive.md) | Property that returns whether there is any message section active. |
| [LastMessage](../ErrorManager/ErrorManager_LastMessage.md) | Property that returns the last recorded error/warning message. If there is a tree of errors/warnings, this property returns the most recent leaf error/warning. |
| [Parent](../ErrorManager/ErrorManager_Parent.md) | Property that returns the parent Application object. |
| [Type](../ErrorManager/ErrorManager_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Application.ErrorManager](../Application/Application_ErrorManager.md), [InventorServer.ErrorManager](InventorServer_ErrorManager.md), [InventorServerObject.ErrorManager](InventorServerObject_ErrorManager.md), [MessageSection.Parent](../MessageSection/MessageSection_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Display custom error messages](../../sample-programs/ErrorManager_AddMessage_Sample.md) | Demonstrates displaying custom error messages. |

## Version

Introduced in version 2010
