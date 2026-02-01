# DraftFeature.inputFaces Property

Parent Object: [DraftFeature](DraftFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeature.h>

## Description

Gets and sets the input faces. If isTangentChain is true, all the faces that are tangentially connected to the input faces (if any) will also be included.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeature\_var" is a variable referencing a DraftFeature object.  ```` ``` # Get the value of the property. propertyValue = draftFeature_var.inputFaces  # Set the value of the property. draftFeature_var.inputFaces = propertyValue ``` ```` |

"draftFeature\_var" is a variable referencing a DraftFeature object. ```` ``` #include <Fusion/Features/DraftFeature.h>  // Get the value of the property. std::vector<Ptr<BRepFace>> propertyValue = draftFeature_var->inputFaces();  // Set the value of the property, where value_var is a BRepFace. bool returnValue = draftFeature_var->inputFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepFace](BRepFace.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |