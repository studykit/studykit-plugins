# BRepEdge.tempId Property

Parent Object: [BRepEdge](BRepEdge.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepEdge.h>

## Description

Returns the temporary ID of this edge. This ID is only good while the document remains open and as long as the owning BRepBody is not modified in any way. The findByTempId method of the BRepBody will return the entity in the body with the given ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepEdge\_var" is a variable referencing a BRepEdge object. |

"bRepEdge\_var" is a variable referencing a BRepEdge object. ```` ``` #include <Fusion/BRep/BRepEdge.h>  // Get the value of the property. integer propertyValue = bRepEdge_var->tempId(); ``` ```` |

## Property Value

This is a read only property whose value is an integer.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |