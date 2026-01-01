# DataFolders.itemById Method

Parent Object: [DataFolders](DataFolders.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFolders.h>

## Description

Returns the folder specified using the ID of the folder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFolders\_var" is a variable referencing a [DataFolders](DataFolders.htm) object.```` ``` returnValue = dataFolders_var.itemById(id) ``` ```` |

"dataFolders\_var" is a variable referencing a [DataFolders](DataFolders.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DataFolder](DataFolder.htm) | Returns the folder or null if a folder with the specified ID is not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID of the folder to return. This is the same ID used by the APS Data Management API. |

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |