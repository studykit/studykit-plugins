# TangentRelationship.nativeObject Property

Parent Object: [TangentRelationship](TangentRelationship.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationship.h>

## Description

The native object is the tangent relationship in the context of the component it was created within.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tangentRelationship\_var" is a variable referencing a TangentRelationship object.  ```` ``` # Get the value of the property. propertyValue = tangentRelationship_var.nativeObject ``` ```` |

"tangentRelationship\_var" is a variable referencing a TangentRelationship object. ```` ``` #include <Fusion/Components/TangentRelationship.h>  // Get the value of the property. Ptr<TangentRelationship> propertyValue = tangentRelationship_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [TangentRelationship](TangentRelationship.htm).

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |