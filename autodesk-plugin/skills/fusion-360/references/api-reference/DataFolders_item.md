# DataFolders.item Method

Parent Object: [DataFolders](DataFolders.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFolders.h>

## Description

Returns the specified folder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFolders\_var" is a variable referencing a [DataFolders](DataFolders.htm) object.```` ``` returnValue = dataFolders_var.item(index) ``` ```` |

"dataFolders\_var" is a variable referencing a [DataFolders](DataFolders.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DataFolder](DataFolder.htm) | Returns the item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the folder to return. The first folder in the list has an index of 0. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |