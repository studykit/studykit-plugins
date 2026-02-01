# Sketch.transform Property

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Gets and sets the transform of the sketch with respect to model space. This defines the transform from the parent component space to the sketch space. For example, if you have point coordinates in the space of the parent component and apply this transform it will result in the coordinates of the equivalent position in sketch space. The transform is sensitive to the assembly context.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a Sketch object.  ```` ``` # Get the value of the property. propertyValue = sketch_var.transform  # Set the value of the property. sketch_var.transform = propertyValue ``` ```` |

"sketch\_var" is a variable referencing a Sketch object. ```` ``` #include <Fusion/Sketch/Sketch.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = sketch_var->transform();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = sketch_var->transform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |