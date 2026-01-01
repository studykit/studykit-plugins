# BRepBody.opacity Property

Parent Object: [BRepBody](BRepBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBody.h>

## Description

Gets and sets the opacity override assigned to this body. A value of 1.0 specifies that is it completely opaque and a value of 0.0 specifies that is it completely transparent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBody\_var" is a variable referencing a BRepBody object.  ```` ``` # Get the value of the property. propertyValue = bRepBody_var.opacity  # Set the value of the property. bRepBody_var.opacity = propertyValue ``` ```` |

"bRepBody\_var" is a variable referencing a BRepBody object. ```` ``` #include <Fusion/BRep/BRepBody.h>  // Get the value of the property. double propertyValue = bRepBody_var->opacity();  // Set the value of the property, where value_var is a double. bool returnValue = bRepBody_var->opacity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |