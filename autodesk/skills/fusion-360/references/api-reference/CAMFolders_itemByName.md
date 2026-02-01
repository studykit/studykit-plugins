# CAMFolders.itemByName Method

Parent Object: [CAMFolders](CAMFolders.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMFolders.h>

## Description

Returns the folder with the specified name (as appears in the browser).

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMFolders\_var" is a variable referencing a [CAMFolders](CAMFolders.htm) object.```` ``` returnValue = cAMFolders_var.itemByName(name) ``` ```` |

"cAMFolders\_var" is a variable referencing a [CAMFolders](CAMFolders.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CAMFolder](CAMFolder.htm) | Returns the specified folder or null in the case where there is no folder with the specified name. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name (as it appears in the browser) of the folder. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |