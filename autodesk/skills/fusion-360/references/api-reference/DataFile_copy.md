# DataFile.copy Method

Parent Object: [DataFile](DataFile.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

Copies this DataFile to the specified folder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a [DataFile](DataFile.htm) object.```` ``` returnValue = dataFile_var.copy(targetFolder) ``` ```` |

"dataFile\_var" is a variable referencing a [DataFile](DataFile.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DataFile](DataFile.htm) | Returns the copied DataFile if the copy was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| targetFolder | [DataFolder](DataFolder.htm) | The folder to copy this DataFile to. |

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |