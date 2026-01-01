# UserInterface.messageBox Method

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

Display a modal message box with the provided text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterface\_var" is a variable referencing a [UserInterface](UserInterface.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"userInterface\_var" is a variable referencing a [UserInterface](UserInterface.htm) object.  ```` ``` #include <Core/UserInterface/UserInterface.h>  // Uses no optional arguments. returnValue = userInterface_var->messageBox(text);  // Uses optional arguments. returnValue = userInterface_var->messageBox(text, title, buttons, icon); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DialogResults](DialogResults.htm) | The button pressed to dismiss the dialog is returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| text | string | The message text to display in the dialog. |
| title | string | If the optional title argument is provided, it sets the title for the dialog, otherwise the script or add-in name is used.   This is an optional argument whose default value is "". |
| buttons | [MessageBoxButtonTypes](MessageBoxButtonTypes.htm) | The optional buttons array can be used to specify which buttons to display on the dialog. The first button provided is the default action. If buttons are not specified, the dialog will default to a single OK button.   This is an optional argument whose default value is MessageBoxButtonTypes.OKButtonType. |
| icon | [MessageBoxIconTypes](MessageBoxIconTypes.htm) | The optional icon argument can be used to specify which icon to display, otherwise the default of no icon is used.   This is an optional argument whose default value is MessageBoxIconTypes.NoIconIconType. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |