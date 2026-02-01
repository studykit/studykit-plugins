# ReverseNormalFeature.surfaces Property

Parent Object: [ReverseNormalFeature](ReverseNormalFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ReverseNormalFeature.h>

## Description

Gets and sets the surface bodies (open BRepBodies) whose faces normals are to be reversed. All faces of the input surface bodies get reversed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"reverseNormalFeature\_var" is a variable referencing a ReverseNormalFeature object.  ```` ``` # Get the value of the property. propertyValue = reverseNormalFeature_var.surfaces  # Set the value of the property. reverseNormalFeature_var.surfaces = propertyValue ``` ```` |

"reverseNormalFeature\_var" is a variable referencing a ReverseNormalFeature object. ```` ``` #include <Fusion/Features/ReverseNormalFeature.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = reverseNormalFeature_var->surfaces();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = reverseNormalFeature_var->surfaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |