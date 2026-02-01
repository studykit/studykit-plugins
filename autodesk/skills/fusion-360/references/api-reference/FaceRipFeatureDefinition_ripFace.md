# FaceRipFeatureDefinition.ripFace Property

Parent Object: [FaceRipFeatureDefinition](FaceRipFeatureDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FaceRipFeatureDefinition.h>

## Description

Gets and sets the input face for a face rip.

## Syntax

* [Python](#Python)
* [C++](#C++)

"faceRipFeatureDefinition\_var" is a variable referencing a FaceRipFeatureDefinition object. |

"faceRipFeatureDefinition\_var" is a variable referencing a FaceRipFeatureDefinition object. ```` ``` #include <Fusion/SheetMetal/FaceRipFeatureDefinition.h>  // Get the value of the property. Ptr<BRepFace> propertyValue = faceRipFeatureDefinition_var->ripFace();  // Set the value of the property, where value_var is a BRepFace. bool returnValue = faceRipFeatureDefinition_var->ripFace(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BRepFace](BRepFace.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |