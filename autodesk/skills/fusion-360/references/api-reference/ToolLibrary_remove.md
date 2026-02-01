# ToolLibrary.remove Method

Parent Object: [ToolLibrary](ToolLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolLibrary.h>

## Description

Remove Tool by index from ToolLibrary.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolLibrary\_var" is a variable referencing a [ToolLibrary](ToolLibrary.htm) object.```` ``` returnValue = toolLibrary_var.remove(index) ``` ```` |

"toolLibrary\_var" is a variable referencing a [ToolLibrary](ToolLibrary.htm) object. |

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