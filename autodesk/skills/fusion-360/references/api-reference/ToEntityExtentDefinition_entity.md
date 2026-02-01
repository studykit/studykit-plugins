# ToEntityExtentDefinition.entity Property

Parent Object: [ToEntityExtentDefinition](ToEntityExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ToEntityExtentDefinition.h>

## Description

Gets and sets the entity that the feature extent is defined up to. This can be a ConstructionPlane, Profile, BrepFace, BrepBody, or BRepVertex.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toEntityExtentDefinition\_var" is a variable referencing a ToEntityExtentDefinition object. |

"toEntityExtentDefinition\_var" is a variable referencing a ToEntityExtentDefinition object. ```` ``` #include <Fusion/Features/ToEntityExtentDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = toEntityExtentDefinition_var->entity();  // Set the value of the property, where value_var is a Base. bool returnValue = toEntityExtentDefinition_var->entity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |