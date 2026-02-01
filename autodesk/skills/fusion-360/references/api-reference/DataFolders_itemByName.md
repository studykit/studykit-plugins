# DataFolders.itemByName Method

Parent Object: [DataFolders](DataFolders.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFolders.h>

## Description

Returns the folder specified using the name of the folder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFolders\_var" is a variable referencing a [DataFolders](DataFolders.htm) object.```` ``` returnValue = dataFolders_var.itemByName(name) ``` ```` |

"dataFolders\_var" is a variable referencing a [DataFolders](DataFolders.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DataFolder](DataFolder.htm) | Returns the folder or null if a folder of the specified name is not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the folder to return. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |