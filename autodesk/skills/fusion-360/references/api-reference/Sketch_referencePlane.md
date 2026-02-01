# Sketch.referencePlane Property

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Gets and sets the construction plane or planar face the sketch is associated to. This is only valid when the IsParametric property is True otherwise this returns null and setting the property will fail.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a Sketch object.  ```` ``` # Get the value of the property. propertyValue = sketch_var.referencePlane  # Set the value of the property. sketch_var.referencePlane = propertyValue ``` ```` |

"sketch\_var" is a variable referencing a Sketch object. ```` ``` #include <Fusion/Sketch/Sketch.h>  // Get the value of the property. Ptr<Base> propertyValue = sketch_var->referencePlane();  // Set the value of the property, where value_var is a Base. bool returnValue = sketch_var->referencePlane(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |