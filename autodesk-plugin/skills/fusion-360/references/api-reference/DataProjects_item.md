# DataProjects.item Method

Parent Object: [DataProjects](DataProjects.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataProjects.h>

## Description

Returns the specified project.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataProjects\_var" is a variable referencing a [DataProjects](DataProjects.htm) object.```` ``` returnValue = dataProjects_var.item(index) ``` ```` |

"dataProjects\_var" is a variable referencing a [DataProjects](DataProjects.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DataProject](DataProject.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the project to return. The first project in the list has an index of 0. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |