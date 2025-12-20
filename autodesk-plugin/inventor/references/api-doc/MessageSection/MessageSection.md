# MessageSection Object

## Description

A MessageSection object can be used to clear, adopt or retain error/warning messages created during the section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AdoptMessages](../MessageSection/MessageSection_AdoptMessages.md) | Method that adopts all messages within this section under the specified message and terminates the section. |
| [ClearMessages](../MessageSection/MessageSection_ClearMessages.md) | Method that clears all messages within this section **and terminates the section**. |
| [End](../MessageSection/MessageSection_End.md) | Method that retains all the messages within this section as is **and terminates the section**. Calling this method is not required if either the ClearMessages or the AdoptMessages method has been called. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MessageSection/MessageSection_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [HasErrors](../MessageSection/MessageSection_HasErrors.md) | Property that returns whether this message section has any errors reported in it. |
| [HasWarnings](../MessageSection/MessageSection_HasWarnings.md) | Property that returns whether this message section has any warnings reported in it. |
| [Parent](../MessageSection/MessageSection_Parent.md) | Property that returns the parent ErrorManager object. |
| [Type](../MessageSection/MessageSection_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ErrorManager.StartMessageSection](../ErrorManager/ErrorManager_StartMessageSection.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Display custom error messages](../../sample-programs/ErrorManager_AddMessage_Sample.md) | Demonstrates displaying custom error messages. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |