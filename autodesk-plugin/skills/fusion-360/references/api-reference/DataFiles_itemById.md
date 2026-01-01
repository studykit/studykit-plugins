# DataFiles.itemById Method

Parent Object: [DataFiles](DataFiles.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFiles.h>

## Description

Returns the file specified using the ID or version ID of the file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFiles\_var" is a variable referencing a [DataFiles](DataFiles.htm) object.```` ``` returnValue = dataFiles_var.itemById(id) ``` ```` |

"dataFiles\_var" is a variable referencing a [DataFiles](DataFiles.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DataFile](DataFile.htm) | Returns the file or null if a file with the specified ID is not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID or version ID of the file to return. This is the same ID used by the APS Data Management API. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |