# CombineFeature.operation Property

Parent Object: [CombineFeature](CombineFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeature.h>

## Description

Gets and sets the type of operation performed by the combine. The valid values are JoinFeatureOperation, CutFeatureOperation and IntersectFeatureOperation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"combineFeature\_var" is a variable referencing a CombineFeature object.  ```` ``` # Get the value of the property. propertyValue = combineFeature_var.operation  # Set the value of the property. combineFeature_var.operation = propertyValue ``` ```` |

"combineFeature\_var" is a variable referencing a CombineFeature object. ```` ``` #include <Fusion/Features/CombineFeature.h>  // Get the value of the property. FeatureOperations propertyValue = combineFeature_var->operation();  // Set the value of the property, where value_var is a FeatureOperations. bool returnValue = combineFeature_var->operation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [FeatureOperations](FeatureOperations.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |