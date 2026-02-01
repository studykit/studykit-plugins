# Attribute.parent Property

Parent Object: [Attribute](Attribute.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Attribute.h>

## Description

Returns the parent entity this attribute is associated with. This can return null in some cases. For example a BRepEdge might have been consumed by a fillet feature but can come back if the model is rolled back or the fillet is deleted.

## Syntax

* [Python](#Python)
* [C++](#C++)

"attribute\_var" is a variable referencing an Attribute object.  ```` ``` # Get the value of the property. propertyValue = attribute_var.parent ``` ```` |

"attribute\_var" is a variable referencing an Attribute object. ```` ``` #include <Core/Application/Attribute.h>  // Get the value of the property. Ptr<Base> propertyValue = attribute_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |