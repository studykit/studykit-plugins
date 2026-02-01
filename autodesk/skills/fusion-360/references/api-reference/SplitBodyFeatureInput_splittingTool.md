# SplitBodyFeatureInput.splittingTool Property

Parent Object: [SplitBodyFeatureInput](SplitBodyFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitBodyFeatureInput.h>

## Description

Gets and sets the entity that defines the splitting tool. The splitting tool is a single entity that can be either a solid or open BRepBody, construction plane, profile, or a face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitBodyFeatureInput\_var" is a variable referencing a SplitBodyFeatureInput object. |

"splitBodyFeatureInput\_var" is a variable referencing a SplitBodyFeatureInput object. ```` ``` #include <Fusion/Features/SplitBodyFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = splitBodyFeatureInput_var->splittingTool();  // Set the value of the property, where value_var is a Base. bool returnValue = splitBodyFeatureInput_var->splittingTool(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |