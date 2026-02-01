# DocumentToolLibrary.toolsBySetupOrFolder Method

Parent Object: [DocumentToolLibrary](DocumentToolLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/DocumentToolLibrary.h>

## Description

Returns all tools used in a given setup or folder. Given setup or folder must belong to the document of the DocumentToolLibrary. Raises an error if given operation is not in the document.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentToolLibrary\_var" is a variable referencing a [DocumentToolLibrary](DocumentToolLibrary.htm) object.```` ``` returnValue = documentToolLibrary_var.toolsBySetupOrFolder(setupOrFolder) ``` ```` |

"documentToolLibrary\_var" is a variable referencing a [DocumentToolLibrary](DocumentToolLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Tool](Tool.htm)[] | Returns tools used by a specific setup or folder. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| setupOrFolder | [OperationBase](OperationBase.htm) | The setup or folder to get tools from. Must belong to the document. |

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |