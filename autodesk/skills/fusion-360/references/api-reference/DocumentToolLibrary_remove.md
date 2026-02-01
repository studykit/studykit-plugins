# DocumentToolLibrary.remove Method

Parent Object: [DocumentToolLibrary](DocumentToolLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/DocumentToolLibrary.h>

## Description

Remove Tool by index from ToolLibrary.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentToolLibrary\_var" is a variable referencing a [DocumentToolLibrary](DocumentToolLibrary.htm) object.```` ``` returnValue = documentToolLibrary_var.remove(index) ``` ```` |

"documentToolLibrary\_var" is a variable referencing a [DocumentToolLibrary](DocumentToolLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true for successful deletion, false otherwise |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | Index of the Tool in the ToolLibrary that should be removed. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |