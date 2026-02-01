# MachineParts.add Method

Parent Object: [MachineParts](MachineParts.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineParts.h>

## Description

Add a new part to this collection. The part's parent will be set to the owner of this collection, or null if this is the root parts collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineParts\_var" is a variable referencing a [MachineParts](MachineParts.htm) object.```` ``` returnValue = machineParts_var.add(partInput) ``` ```` |

"machineParts\_var" is a variable referencing a [MachineParts](MachineParts.htm) object.  ```` ``` #include <Cam/Machine/MachineParts.h>  returnValue = machineParts_var->add(partInput); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MachinePart](MachinePart.htm) | Returns the newly created MachinePart or null if creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| partInput | [MachinePartInput](MachinePartInput.htm) | Part input object used to create the new MachinePart. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |