# Command.setDialogInitialSize Method

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Sets the initial size of the dialog when it is first displayed. If this is not set, Fusion will use a default size for the dialog.

## Syntax

* [Python](#Python)
* [C++](#C++)

"command\_var" is a variable referencing a [Command](Command.htm) object.```` ``` returnValue = command_var.setDialogInitialSize(width, height) ``` ```` |

"command\_var" is a variable referencing a [Command](Command.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the default size was successfully set. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| width | integer | The width of the dialog in pixels. |
| height | integer | The height of the dialog in pixels. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |