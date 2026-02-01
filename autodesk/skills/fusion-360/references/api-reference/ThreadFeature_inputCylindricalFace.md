# ThreadFeature.inputCylindricalFace Property

Parent Object: [ThreadFeature](ThreadFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeature.h>

## Description

Gets and sets the threaded face. In the case where there are multiple faces, only the first one is returned. Setting this results in a thread being applied to only a single face. It is recommended that you use the inputCylindricalfaces property in order to have full access to the collection of faces to be threaded.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeature\_var" is a variable referencing a ThreadFeature object.  ```` ``` # Get the value of the property. propertyValue = threadFeature_var.inputCylindricalFace  # Set the value of the property. threadFeature_var.inputCylindricalFace = propertyValue ``` ```` |

"threadFeature\_var" is a variable referencing a ThreadFeature object. ```` ``` #include <Fusion/Features/ThreadFeature.h>  // Get the value of the property. Ptr<BRepFace> propertyValue = threadFeature_var->inputCylindricalFace();  // Set the value of the property, where value_var is a BRepFace. bool returnValue = threadFeature_var->inputCylindricalFace(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BRepFace](BRepFace.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |