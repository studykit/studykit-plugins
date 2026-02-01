# MachineQuery.execute Method

Parent Object: [MachineQuery](MachineQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineQuery.h>

## Description

Executes the query for specific machines based on the query's properties.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineQuery\_var" is a variable referencing a [MachineQuery](MachineQuery.htm) object.```` ``` returnValue = machineQuery_var.execute() ``` ```` |

"machineQuery\_var" is a variable referencing a [MachineQuery](MachineQuery.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Machine](Machine.htm)[] | Returns a list of `Machine`. Each returned machine matches this query. |

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |