# CAMFolders.addFolder Method

Parent Object: [CAMFolders](CAMFolders.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMFolders.h>

## Description

Creates a folder with the specified name and returns it as CAMFolder object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMFolders\_var" is a variable referencing a [CAMFolders](CAMFolders.htm) object.```` ``` returnValue = cAMFolders_var.addFolder(name) ``` ```` |

"cAMFolders\_var" is a variable referencing a [CAMFolders](CAMFolders.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CAMFolder](CAMFolder.htm) | Returns the newly created folder or null if folder can't be created. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name (as it appears in the browser) of the folder. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |