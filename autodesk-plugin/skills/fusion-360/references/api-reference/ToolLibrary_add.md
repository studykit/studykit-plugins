# ToolLibrary.add Method

Parent Object: [ToolLibrary](ToolLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolLibrary.h>

## Description

Inserts a Tool at the end of the ToolLibrary.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolLibrary\_var" is a variable referencing a [ToolLibrary](ToolLibrary.htm) object.```` ``` returnValue = toolLibrary_var.add(tool) ``` ```` |

"toolLibrary\_var" is a variable referencing a [ToolLibrary](ToolLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true for successful insertion, false otherwise |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| tool | [Tool](Tool.htm) | The Tool that should be added. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |