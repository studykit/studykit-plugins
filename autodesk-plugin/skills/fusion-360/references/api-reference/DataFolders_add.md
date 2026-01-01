# DataFolders.add Method

Parent Object: [DataFolders](DataFolders.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFolders.h>

## Description

Creates a new folder within the parent folder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFolders\_var" is a variable referencing a [DataFolders](DataFolders.htm) object.```` ``` returnValue = dataFolders_var.add(name) ``` ```` |

"dataFolders\_var" is a variable referencing a [DataFolders](DataFolders.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DataFolder](DataFolder.htm) | Returns the created DataFolder or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the folder. This must be unique with respect to the other folders within the parent folder. |

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |