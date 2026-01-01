# CommandControl.promote Method

Parent Object: [CommandControl](CommandControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandControl.h>

## Description

Promote the command to the parent panel and optionally position it relative to an already- promoted control.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandControl\_var" is a variable referencing a [CommandControl](CommandControl.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"commandControl\_var" is a variable referencing a [CommandControl](CommandControl.htm) object.  ```` ``` #include <Core/UserInterface/CommandControl.h>  // Uses no optional arguments. returnValue = commandControl_var->promote();  // Uses optional arguments. returnValue = commandControl_var->promote(byDefault, positionID, isBefore); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | True if this control was successfully promoted or was already promoted. False if promotion failed, which may happen if the control is not in a panel. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| byDefault | boolean | If true, then the control will be promoted in the panel by default if the UI is reset. If false, then the promotion is cleared on reset.   This is an optional argument whose default value is False. |
| positionID | string | If provided, then when this control is promoted, it will be positioned in the panel relative to the already-promoted control with this ID.   This is an optional argument whose default value is "". |
| isBefore | boolean | If a positionID is provided, then this specifies whether the promoted control is placed before or after the control referenced by the positionID parameter.   This is an optional argument whose default value is True. |

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |