# DataFiles.item Method

Parent Object: [DataFiles](DataFiles.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFiles.h>

## Description

Returns the specified data file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFiles\_var" is a variable referencing a [DataFiles](DataFiles.htm) object.```` ``` returnValue = dataFiles_var.item(index) ``` ```` |

"dataFiles\_var" is a variable referencing a [DataFiles](DataFiles.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DataFile](DataFile.htm) | Returns the specified file or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the file to return. The first file in the list has an index of 0. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |