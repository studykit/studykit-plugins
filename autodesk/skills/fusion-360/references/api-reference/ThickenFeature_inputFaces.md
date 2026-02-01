# ThickenFeature.inputFaces Property

Parent Object: [ThickenFeature](ThickenFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeature.h>

## Description

Gets and sets the ObjectCollection containing the face and/or patch bodies to thicken.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeature\_var" is a variable referencing a ThickenFeature object.  ```` ``` # Get the value of the property. propertyValue = thickenFeature_var.inputFaces  # Set the value of the property. thickenFeature_var.inputFaces = propertyValue ``` ```` |

"thickenFeature\_var" is a variable referencing a ThickenFeature object. ```` ``` #include <Fusion/Features/ThickenFeature.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = thickenFeature_var->inputFaces();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = thickenFeature_var->inputFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |