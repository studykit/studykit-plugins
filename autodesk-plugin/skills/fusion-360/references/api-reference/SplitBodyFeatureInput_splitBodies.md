# SplitBodyFeatureInput.splitBodies Property

Parent Object: [SplitBodyFeatureInput](SplitBodyFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitBodyFeatureInput.h>

## Description

Gets and sets the input solid or open bodies to be split. This can be a single BRepBody or an ObjectCollection if multiple bodies are to be split.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitBodyFeatureInput\_var" is a variable referencing a SplitBodyFeatureInput object. |

"splitBodyFeatureInput\_var" is a variable referencing a SplitBodyFeatureInput object. ```` ``` #include <Fusion/Features/SplitBodyFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = splitBodyFeatureInput_var->splitBodies();  // Set the value of the property, where value_var is a Base. bool returnValue = splitBodyFeatureInput_var->splitBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |