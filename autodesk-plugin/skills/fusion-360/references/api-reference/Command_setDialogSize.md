# Command.setDialogSize Method

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Sets the size of the dialog and overrides any size. This can be used when the command is created or anytime while the command is running. If the height is zero, the dialog will be sized to fit the command inputs currently displayed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"command\_var" is a variable referencing a [Command](Command.htm) object.```` ``` returnValue = command_var.setDialogSize(width, height) ``` ```` |

"command\_var" is a variable referencing a [Command](Command.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if size was successfully set. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| width | integer | The width of the dialog in pixels. |
| height | integer | The height of the dialog in pixels. If zero, the dialog will be sized to fit the command inputs currently displayed. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |