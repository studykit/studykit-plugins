# CopyPasteBodies.add Method

Parent Object: [CopyPasteBodies](CopyPasteBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CopyPasteBodies.h>

## Description

Copies the specified body into the component that owns this CopyPasteBodies collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"copyPasteBodies\_var" is a variable referencing a [CopyPasteBodies](CopyPasteBodies.htm) object.```` ``` returnValue = copyPasteBodies_var.add(sourceBody) ``` ```` |

"copyPasteBodies\_var" is a variable referencing a [CopyPasteBodies](CopyPasteBodies.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CopyPasteBody](CopyPasteBody.htm) | Returns the newly created BRepBody object or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sourceBody | [Base](Base.htm) | Either an ObjectCollection of BRepBodies or a single BRepBody object to copy. |

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |