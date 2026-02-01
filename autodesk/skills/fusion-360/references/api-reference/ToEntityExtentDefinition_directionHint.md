# ToEntityExtentDefinition.directionHint Property

Parent Object: [ToEntityExtentDefinition](ToEntityExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ToEntityExtentDefinition.h>

## Description

Gets and sets a direction that is used when the result is ambiguous. For example, if you have a profile in the center of a torus and are extruding to the torus, the extrusion can go in either direction. When needed, this provides the information to tell Fusion which direction to go. In most cases this is not needed and the property will be null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toEntityExtentDefinition\_var" is a variable referencing a ToEntityExtentDefinition object. |

"toEntityExtentDefinition\_var" is a variable referencing a ToEntityExtentDefinition object. ```` ``` #include <Fusion/Features/ToEntityExtentDefinition.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = toEntityExtentDefinition_var->directionHint();  // Set the value of the property, where value_var is a Vector3D. bool returnValue = toEntityExtentDefinition_var->directionHint(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |