# CAMFolders.itemByOperationId Method

Parent Object: [CAMFolders](CAMFolders.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMFolders.h>

## Description

Returns the folder with the specified operation id.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMFolders\_var" is a variable referencing a [CAMFolders](CAMFolders.htm) object.```` ``` returnValue = cAMFolders_var.itemByOperationId(id) ``` ```` |

"cAMFolders\_var" is a variable referencing a [CAMFolders](CAMFolders.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CAMFolder](CAMFolder.htm) | Returns the specified folder or null in the case where there is no folder with the specified operation id. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | integer | The id of the folder. |

## Version

Introduced in version May 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |