# DraftFeatureInput.inputFaces Property

Parent Object: [DraftFeatureInput](DraftFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeatureInput.h>

## Description

Gets and sets the input faces. If IsTangentChain is true, all the faces that are tangentially connected to the input faces (if any) will also be included.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeatureInput\_var" is a variable referencing a DraftFeatureInput object. |

"draftFeatureInput\_var" is a variable referencing a DraftFeatureInput object. ```` ``` #include <Fusion/Features/DraftFeatureInput.h>  // Get the value of the property. std::vector<Ptr<BRepFace>> propertyValue = draftFeatureInput_var->inputFaces();  // Set the value of the property, where value_var is a BRepFace. bool returnValue = draftFeatureInput_var->inputFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepFace](BRepFace.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |