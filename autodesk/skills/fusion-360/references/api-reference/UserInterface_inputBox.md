# UserInterface.inputBox Method

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

Displays a modal dialog to get string input from the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterface\_var" is a variable referencing a [UserInterface](UserInterface.htm) object. |

```` ```  #include <Core/UserInterface/UserInterface.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string | Returns the string entered by the user but because the user can click Cancel, the canceled argument should be tested before using the string. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| prompt | string | The message text to display in the dialog. |
| cancelled | boolean | Indicates if the dialog was canceled. |
| title | string | Sets the title for the dialog if specified, otherwise the script or add-in name is used.   This is an optional argument whose default value is "". |
| defaultValue | string | The default string that's shown when the dialog is initially displayed, otherwise the input box is empty.   This is an optional argument whose default value is "". |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Use inputBox to get value and evaluateExpression to validate it](InputBox_Sample.htm) | Uses the UserInterface.inputBox function to get a string from the user and then validates that the strinng entered is a valid expression by using the UnitsManager.evaluateExpression function. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |