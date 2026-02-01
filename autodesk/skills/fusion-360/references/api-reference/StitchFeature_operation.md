# StitchFeature.operation Property

Parent Object: [StitchFeature](StitchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/StitchFeature.h>

## Description

Gets and sets the feature operation to perform. This property value is ignored if the stitched result does not form a solid body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stitchFeature\_var" is a variable referencing a StitchFeature object.  ```` ``` # Get the value of the property. propertyValue = stitchFeature_var.operation  # Set the value of the property. stitchFeature_var.operation = propertyValue ``` ```` |

"stitchFeature\_var" is a variable referencing a StitchFeature object. ```` ``` #include <Fusion/Features/StitchFeature.h>  // Get the value of the property. FeatureOperations propertyValue = stitchFeature_var->operation();  // Set the value of the property, where value_var is a FeatureOperations. bool returnValue = stitchFeature_var->operation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [FeatureOperations](FeatureOperations.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |