# SplitFaceFeatureInput.splittingTool Property

Parent Object: [SplitFaceFeatureInput](SplitFaceFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeatureInput.h>

## Description

Gets and sets the entity(s) that define the splitting tool(s). The splitting tool can be a single entity or an ObjectCollection containing solid and/or open bodies, construction planes, faces, or sketch curves that partially or fully intersect the faces that are being split.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitFaceFeatureInput\_var" is a variable referencing a SplitFaceFeatureInput object. |

"splitFaceFeatureInput\_var" is a variable referencing a SplitFaceFeatureInput object. ```` ``` #include <Fusion/Features/SplitFaceFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = splitFaceFeatureInput_var->splittingTool();  // Set the value of the property, where value_var is a Base. bool returnValue = splitFaceFeatureInput_var->splittingTool(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |