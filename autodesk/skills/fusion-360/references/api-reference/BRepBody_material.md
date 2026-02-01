# BRepBody.material Property

Parent Object: [BRepBody](BRepBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBody.h>

## Description

Gets and sets the material assigned to this body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBody\_var" is a variable referencing a BRepBody object.  ```` ``` # Get the value of the property. propertyValue = bRepBody_var.material  # Set the value of the property. bRepBody_var.material = propertyValue ``` ```` |

"bRepBody\_var" is a variable referencing a BRepBody object. ```` ``` #include <Fusion/BRep/BRepBody.h>  // Get the value of the property. Ptr<Material> propertyValue = bRepBody_var->material();  // Set the value of the property, where value_var is a Material. bool returnValue = bRepBody_var->material(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Material](Material.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |