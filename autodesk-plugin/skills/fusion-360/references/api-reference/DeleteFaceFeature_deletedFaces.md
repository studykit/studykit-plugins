# DeleteFaceFeature.deletedFaces Property

Parent Object: [DeleteFaceFeature](DeleteFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DeleteFaceFeature.h>

## Description

Gets and sets the set of faces that are deleted by this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"deleteFaceFeature\_var" is a variable referencing a DeleteFaceFeature object.  ```` ``` # Get the value of the property. propertyValue = deleteFaceFeature_var.deletedFaces  # Set the value of the property. deleteFaceFeature_var.deletedFaces = propertyValue ``` ```` |

"deleteFaceFeature\_var" is a variable referencing a DeleteFaceFeature object. ```` ``` #include <Fusion/Features/DeleteFaceFeature.h>  // Get the value of the property. std::vector<Ptr<BRepFace>> propertyValue = deleteFaceFeature_var->deletedFaces();  // Set the value of the property, where value_var is a BRepFace. bool returnValue = deleteFaceFeature_var->deletedFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepFace](BRepFace.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |