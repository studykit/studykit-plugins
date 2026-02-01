# Command.setDialogMinimumSize Method

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Sets the minimum size for the dialog when resized to by the user. If this is not set, a default minimum size is used.

## Syntax

* [Python](#Python)
* [C++](#C++)

"command\_var" is a variable referencing a [Command](Command.htm) object.```` ``` returnValue = command_var.setDialogMinimumSize(width, height) ``` ```` |

"command\_var" is a variable referencing a [Command](Command.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the minimum size was successfully set. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| width | integer | The minimum width of the dialog in pixels. |
| height | integer | The minimum height of the dialog in pixels. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |