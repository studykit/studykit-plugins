# CutPasteBodies.add Method

Parent Object: [CutPasteBodies](CutPasteBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CutPasteBodies.h>

## Description

Cuts and copies the specified body into the component that owns this CutPasteBodies collection. This is effectively the equivalent of moving a body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cutPasteBodies\_var" is a variable referencing a [CutPasteBodies](CutPasteBodies.htm) object.```` ``` returnValue = cutPasteBodies_var.add(sourceBody) ``` ```` |

"cutPasteBodies\_var" is a variable referencing a [CutPasteBodies](CutPasteBodies.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CutPasteBody](CutPasteBody.htm) | Returns the newly created BRepBody object or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sourceBody | [Base](Base.htm) | Either an ObjectCollection of BRepBodies or a single BRepBody object to cut. |

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |