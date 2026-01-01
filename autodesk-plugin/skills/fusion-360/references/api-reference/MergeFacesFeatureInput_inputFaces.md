# MergeFacesFeatureInput.inputFaces Property

Parent Object: [MergeFacesFeatureInput](MergeFacesFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MergeFacesFeatureInput.h>

## Description

Gets and sets an array of BRepFace objects that define the faces the merge will be performed on. The faces need to be connected and from the same body (solid or surface).

## Syntax

* [Python](#Python)
* [C++](#C++)

"mergeFacesFeatureInput\_var" is a variable referencing a MergeFacesFeatureInput object. |

"mergeFacesFeatureInput\_var" is a variable referencing a MergeFacesFeatureInput object. ```` ``` #include <Fusion/Features/MergeFacesFeatureInput.h>  // Get the value of the property. std::vector<Ptr<BRepFace>> propertyValue = mergeFacesFeatureInput_var->inputFaces();  // Set the value of the property, where value_var is a BRepFace. bool returnValue = mergeFacesFeatureInput_var->inputFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepFace](BRepFace.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |