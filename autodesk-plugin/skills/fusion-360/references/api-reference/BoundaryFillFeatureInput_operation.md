# BoundaryFillFeatureInput.operation Property

Parent Object: [BoundaryFillFeatureInput](BoundaryFillFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeatureInput.h>

## Description

Gets and sets the type of operation performed by the boundary fill feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeatureInput\_var" is a variable referencing a BoundaryFillFeatureInput object. |

"boundaryFillFeatureInput\_var" is a variable referencing a BoundaryFillFeatureInput object. ```` ``` #include <Fusion/Features/BoundaryFillFeatureInput.h>  // Get the value of the property. FeatureOperations propertyValue = boundaryFillFeatureInput_var->operation();  // Set the value of the property, where value_var is a FeatureOperations. bool returnValue = boundaryFillFeatureInput_var->operation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [FeatureOperations](FeatureOperations.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |