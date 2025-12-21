# ErrorManager.Show Method

Parent Object: [ErrorManager](../ErrorManager/ErrorManager.md)

## Description

Method that displays the current error/warning or the stack of errors/warnings to the user.

## Remarks

The method returns an error if there are no errors or warnings. If there were errors or warnings, the method \returns a ButtonTypeEnum value indicating the user's choice. The return value can be one of the three values listed below and should be handled as described: \* **kCancelButtonType** - Implies that the user does not want to continue. Any partial success during the execution is to be aborted. The command would have thus behaved like a no-op. \* **kAcceptButtonType** - Implies that the user would like to continue despite the errors/warnings. The entire operation should return success, with the partially successful results committed to the document(s). \* **kEditButtonType** - Implies that the user would like to go back into the command to correct the situation. The entire operation should be aborted, including any partial success and control should be returned back to the command.

## Syntax

ErrorManager.**Show**( ***Title*** As String, ***AllowAccept*** As Boolean, ***AllowEdit*** As Boolean ) As [ButtonTypeEnum](../ButtonTypeEnum.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Title | String | Input string that specifies the title of the message dialog. The display name of the product (e.g. 'Autodesk Inventor 2010 ' ') is prefixed to the string automatically. |
| AllowAccept | Boolean | Input Boolean that indicates whether the 'Accept' button should be available. This user choice implies that the user would like to continue despite any errors/warnings. |
| AllowEdit | Boolean | Input Boolean that indicates whether the 'Edit' button should be available. This user choice implies that implies that the user would like to go back into the command to correct the situation. |

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