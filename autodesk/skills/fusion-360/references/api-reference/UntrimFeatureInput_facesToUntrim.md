# UntrimFeatureInput.facesToUntrim Property

Parent Object: [UntrimFeatureInput](UntrimFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeatureInput.h>

## Description

Gets the face objects to untrim. Returns null/None in the case where loops are specified instead of faces.

## Syntax

* [Python](#Python)
* [C++](#C++)

"untrimFeatureInput\_var" is a variable referencing a UntrimFeatureInput object. |

"untrimFeatureInput\_var" is a variable referencing a UntrimFeatureInput object. ```` ``` #include <Fusion/Features/UntrimFeatureInput.h>  // Get the value of the property. std::vector<Ptr<BRepFace>> propertyValue = untrimFeatureInput_var->facesToUntrim(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [BRepFace](BRepFace.htm).

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |