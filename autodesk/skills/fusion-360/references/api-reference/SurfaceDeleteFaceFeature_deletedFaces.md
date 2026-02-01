# SurfaceDeleteFaceFeature.deletedFaces Property

Parent Object: [SurfaceDeleteFaceFeature](SurfaceDeleteFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SurfaceDeleteFaceFeature.h>

## Description

Gets and sets the set of faces that are deleted by this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"surfaceDeleteFaceFeature\_var" is a variable referencing a SurfaceDeleteFaceFeature object.  ```` ``` # Get the value of the property. propertyValue = surfaceDeleteFaceFeature_var.deletedFaces  # Set the value of the property. surfaceDeleteFaceFeature_var.deletedFaces = propertyValue ``` ```` |

"surfaceDeleteFaceFeature\_var" is a variable referencing a SurfaceDeleteFaceFeature object. ```` ``` #include <Fusion/Features/SurfaceDeleteFaceFeature.h>  // Get the value of the property. std::vector<Ptr<BRepFace>> propertyValue = surfaceDeleteFaceFeature_var->deletedFaces();  // Set the value of the property, where value_var is a BRepFace. bool returnValue = surfaceDeleteFaceFeature_var->deletedFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepFace](BRepFace.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |