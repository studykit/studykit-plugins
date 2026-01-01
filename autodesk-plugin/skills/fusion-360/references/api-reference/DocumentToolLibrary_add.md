# DocumentToolLibrary.add Method

Parent Object: [DocumentToolLibrary](DocumentToolLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/DocumentToolLibrary.h>

## Description

Inserts a Tool at the end of the ToolLibrary.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentToolLibrary\_var" is a variable referencing a [DocumentToolLibrary](DocumentToolLibrary.htm) object.```` ``` returnValue = documentToolLibrary_var.add(tool) ``` ```` |

"documentToolLibrary\_var" is a variable referencing a [DocumentToolLibrary](DocumentToolLibrary.htm) object. |

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