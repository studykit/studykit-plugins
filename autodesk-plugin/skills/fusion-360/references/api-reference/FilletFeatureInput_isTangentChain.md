# FilletFeatureInput.isTangentChain Property

Parent Object: [FilletFeatureInput](FilletFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeatureInput.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property is obsolete. You should now use the FilletEdgeSet object to define if the tangency chaining should be used for entities in that edge set.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeatureInput\_var" is a variable referencing a FilletFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = filletFeatureInput_var.isTangentChain  # Set the value of the property. filletFeatureInput_var.isTangentChain = propertyValue ``` ```` |

"filletFeatureInput\_var" is a variable referencing a FilletFeatureInput object. ```` ``` #include <Fusion/Features/FilletFeatureInput.h>  // Get the value of the property. boolean propertyValue = filletFeatureInput_var->isTangentChain();  // Set the value of the property, where value_var is a boolean. bool returnValue = filletFeatureInput_var->isTangentChain(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2014
Retired in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |