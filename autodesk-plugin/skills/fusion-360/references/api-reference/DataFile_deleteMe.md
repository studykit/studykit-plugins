# DataFile.deleteMe Method

Parent Object: [DataFile](DataFile.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

Deletes this DataFile. This can fail if this file is referenced by another file or is currently open.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a [DataFile](DataFile.htm) object.```` ``` returnValue = dataFile_var.deleteMe() ``` ```` |

"dataFile\_var" is a variable referencing a [DataFile](DataFile.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the deletion was successful. |

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |