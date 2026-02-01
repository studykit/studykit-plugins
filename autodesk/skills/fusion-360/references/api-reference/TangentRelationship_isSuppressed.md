# TangentRelationship.isSuppressed Property

Parent Object: [TangentRelationship](TangentRelationship.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationship.h>

## Description

Gets and sets if this tangent relationship is suppressed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tangentRelationship\_var" is a variable referencing a TangentRelationship object. |

"tangentRelationship\_var" is a variable referencing a TangentRelationship object. ```` ``` #include <Fusion/Components/TangentRelationship.h>  // Get the value of the property. boolean propertyValue = tangentRelationship_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = tangentRelationship_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |