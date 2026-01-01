# CombineFeatureInput.operation Property

Parent Object: [CombineFeatureInput](CombineFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeatureInput.h>

## Description

Gets and sets the type of operation performed by the combine. The valid values are JoinFeatureOperation, CutFeatureOperation and IntersectFeatureOperation. The default value is JoinFeatureOperation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"combineFeatureInput\_var" is a variable referencing a CombineFeatureInput object. |

"combineFeatureInput\_var" is a variable referencing a CombineFeatureInput object. ```` ``` #include <Fusion/Features/CombineFeatureInput.h>  // Get the value of the property. FeatureOperations propertyValue = combineFeatureInput_var->operation();  // Set the value of the property, where value_var is a FeatureOperations. bool returnValue = combineFeatureInput_var->operation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [FeatureOperations](FeatureOperations.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [combineFeatures.add](combineFeatures_add_Sample.htm) | Demonstrates the combineFeatures.add method. To use this sample, have a design open that contains at least two bodies. When you run the sample, you will be prompted to select the bodies and they will joined. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |