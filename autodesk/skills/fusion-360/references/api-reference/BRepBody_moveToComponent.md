# BRepBody.moveToComponent Method

Parent Object: [BRepBody](BRepBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBody.h>

## Description

Moves this body from it's current component into the root component or the component owned by the specified occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBody\_var" is a variable referencing a [BRepBody](BRepBody.htm) object.```` ``` returnValue = bRepBody_var.moveToComponent(target) ``` ```` |

"bRepBody\_var" is a variable referencing a [BRepBody](BRepBody.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepBody](BRepBody.htm) | Returns the moved BRepBody or null in the case the move failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| target | [Base](Base.htm) | The target can be either the root component or an occurrence.   In the case where an occurrence is specified, the body will be moved into the parent component of the target occurrence and the target occurrence defines the transform of how the body will be copied so that the body maintains it's same position with respect to the assembly. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |