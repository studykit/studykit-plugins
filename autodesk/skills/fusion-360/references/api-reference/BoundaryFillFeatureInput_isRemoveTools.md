# BoundaryFillFeatureInput.isRemoveTools Property

Parent Object: [BoundaryFillFeatureInput](BoundaryFillFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeatureInput.h>

## Description

Gets and sets whether any BRepBodys that were used as tools should be removed as part of the feature creation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeatureInput\_var" is a variable referencing a BoundaryFillFeatureInput object. |

"boundaryFillFeatureInput\_var" is a variable referencing a BoundaryFillFeatureInput object. ```` ``` #include <Fusion/Features/BoundaryFillFeatureInput.h>  // Get the value of the property. boolean propertyValue = boundaryFillFeatureInput_var->isRemoveTools();  // Set the value of the property, where value_var is a boolean. bool returnValue = boundaryFillFeatureInput_var->isRemoveTools(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |