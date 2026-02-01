# ThreadFeatureInput.threadLocation Property

Parent Object: [ThreadFeatureInput](ThreadFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeatureInput.h>

## Description

Gets and sets which end of the cylinder the thread is measured from when it's not full length. The thread position and length can be measured from either the "low" or "high" end. You can determine the low and high end by using the Cylinder associated with the cylindrical BRepFace the thread is being added to. The BRepFace.geometry which will return a Cylinder object. The axis property of the Cylinder is a vector and the high end of the cylinder is at the far end of the cylinder with respect to the axis vector.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeatureInput\_var" is a variable referencing a ThreadFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = threadFeatureInput_var.threadLocation  # Set the value of the property. threadFeatureInput_var.threadLocation = propertyValue ``` ```` |

"threadFeatureInput\_var" is a variable referencing a ThreadFeatureInput object. ```` ``` #include <Fusion/Features/ThreadFeatureInput.h>  // Get the value of the property. ThreadLocations propertyValue = threadFeatureInput_var->threadLocation();  // Set the value of the property, where value_var is a ThreadLocations. bool returnValue = threadFeatureInput_var->threadLocation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ThreadLocations](ThreadLocations.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |