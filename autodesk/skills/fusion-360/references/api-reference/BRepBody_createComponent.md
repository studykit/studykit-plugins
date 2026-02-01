# BRepBody.createComponent Method

Parent Object: [BRepBody](BRepBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBody.h>

## Description

Creates a new component and occurrence within the component that currently owns this body. This body is moved into the new component and returned. The newly created component can be obtained by using the parentComponent property of the BRepBody object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBody\_var" is a variable referencing a [BRepBody](BRepBody.htm) object.```` ``` returnValue = bRepBody_var.createComponent() ``` ```` |

"bRepBody\_var" is a variable referencing a [BRepBody](BRepBody.htm) object.  ```` ``` #include <Fusion/BRep/BRepBody.h>  returnValue = bRepBody_var->createComponent(); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepBody](BRepBody.htm) | Returns the BRrepBody in the new component or null in the case the creation failed. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |