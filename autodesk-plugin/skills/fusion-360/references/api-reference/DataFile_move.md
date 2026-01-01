# DataFile.move Method

Parent Object: [DataFile](DataFile.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

Moves this DataFile to the specified folder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a [DataFile](DataFile.htm) object.```` ``` returnValue = dataFile_var.move(targetFolder) ``` ```` |

"dataFile\_var" is a variable referencing a [DataFile](DataFile.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the move was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| targetFolder | [DataFolder](DataFolder.htm) | The folder to move this DataFile to. |

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |