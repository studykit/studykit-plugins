# StitchFeatureInput.operation Property

Parent Object: [StitchFeatureInput](StitchFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/StitchFeatureInput.h>

## Description

Gets and sets the feature operation to perform. This property value is only valid if the isSolid property returns true. Otherwise the value of this property is ignored.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stitchFeatureInput\_var" is a variable referencing a StitchFeatureInput object. |

"stitchFeatureInput\_var" is a variable referencing a StitchFeatureInput object. ```` ``` #include <Fusion/Features/StitchFeatureInput.h>  // Get the value of the property. FeatureOperations propertyValue = stitchFeatureInput_var->operation();  // Set the value of the property, where value_var is a FeatureOperations. bool returnValue = stitchFeatureInput_var->operation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [FeatureOperations](FeatureOperations.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |