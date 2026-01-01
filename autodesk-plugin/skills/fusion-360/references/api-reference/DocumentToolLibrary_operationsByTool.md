# DocumentToolLibrary.operationsByTool Method

Parent Object: [DocumentToolLibrary](DocumentToolLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/DocumentToolLibrary.h>

## Description

Returns all operations that use the given tool. The tool must exist in the document tool library. Raises an error if the tool is not in the document.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentToolLibrary\_var" is a variable referencing a [DocumentToolLibrary](DocumentToolLibrary.htm) object.```` ``` returnValue = documentToolLibrary_var.operationsByTool(tool) ``` ```` |

"documentToolLibrary\_var" is a variable referencing a [DocumentToolLibrary](DocumentToolLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Operation](Operation.htm)[] | Returns operations using a specific tool. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| tool | [Tool](Tool.htm) | The tool to search for in operations. The tool must exist in the document. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |