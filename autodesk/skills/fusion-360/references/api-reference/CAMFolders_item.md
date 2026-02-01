# CAMFolders.item Method

Parent Object: [CAMFolders](CAMFolders.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMFolders.h>

## Description

Function that returns the specified folder using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMFolders\_var" is a variable referencing a [CAMFolders](CAMFolders.htm) object.```` ``` returnValue = cAMFolders_var.item(index) ``` ```` |

"cAMFolders\_var" is a variable referencing a [CAMFolders](CAMFolders.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CAMFolder](CAMFolder.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |