# BRepCoEdge.assemblyContext Property

Parent Object: [BRepCoEdge](BRepCoEdge.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepCoEdge.h>

## Description

Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this BRepCoEdge object is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCoEdge\_var" is a variable referencing a BRepCoEdge object. |

"bRepCoEdge\_var" is a variable referencing a BRepCoEdge object. ```` ``` #include <Fusion/BRep/BRepCoEdge.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = bRepCoEdge_var->assemblyContext(); ``` ```` |

## Property Value

This is a read only property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |