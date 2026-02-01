# DataProjects.itemById Method

Parent Object: [DataProjects](DataProjects.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataProjects.h>

## Description

Returns the project specified using the ID of the project.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataProjects\_var" is a variable referencing a [DataProjects](DataProjects.htm) object.```` ``` returnValue = dataProjects_var.itemById(id) ``` ```` |

"dataProjects\_var" is a variable referencing a [DataProjects](DataProjects.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DataProject](DataProject.htm) | Returns the project or null if a project with the specified ID is not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID of the project to return. This is the same ID used by the APS Data Management API. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |