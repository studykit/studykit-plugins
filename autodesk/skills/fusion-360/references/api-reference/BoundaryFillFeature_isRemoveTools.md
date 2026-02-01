# BoundaryFillFeature.isRemoveTools Property

Parent Object: [BoundaryFillFeature](BoundaryFillFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeature.h>

## Description

Gets and sets whether any BRepBodys that were used as tools should be removed as part of the feature creation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeature\_var" is a variable referencing a BoundaryFillFeature object.  ```` ``` # Get the value of the property. propertyValue = boundaryFillFeature_var.isRemoveTools  # Set the value of the property. boundaryFillFeature_var.isRemoveTools = propertyValue ``` ```` |

"boundaryFillFeature\_var" is a variable referencing a BoundaryFillFeature object. ```` ``` #include <Fusion/Features/BoundaryFillFeature.h>  // Get the value of the property. boolean propertyValue = boundaryFillFeature_var->isRemoveTools();  // Set the value of the property, where value_var is a boolean. bool returnValue = boundaryFillFeature_var->isRemoveTools(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |