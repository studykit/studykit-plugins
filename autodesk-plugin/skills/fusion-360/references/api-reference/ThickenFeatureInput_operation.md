# ThickenFeatureInput.operation Property

Parent Object: [ThickenFeatureInput](ThickenFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeatureInput.h>

## Description

Gets and sets the feature operation to perform.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeatureInput\_var" is a variable referencing a ThickenFeatureInput object. |

"thickenFeatureInput\_var" is a variable referencing a ThickenFeatureInput object. ```` ``` #include <Fusion/Features/ThickenFeatureInput.h>  // Get the value of the property. FeatureOperations propertyValue = thickenFeatureInput_var->operation();  // Set the value of the property, where value_var is a FeatureOperations. bool returnValue = thickenFeatureInput_var->operation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [FeatureOperations](FeatureOperations.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |