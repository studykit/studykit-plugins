# ThreadFeatureInput.isRightHanded Property

Parent Object: [ThreadFeatureInput](ThreadFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeatureInput.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

The direction of the thread is now controlled through the isRightHanded property of the ThreadInfo object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeatureInput\_var" is a variable referencing a ThreadFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = threadFeatureInput_var.isRightHanded  # Set the value of the property. threadFeatureInput_var.isRightHanded = propertyValue ``` ```` |

"threadFeatureInput\_var" is a variable referencing a ThreadFeatureInput object. ```` ``` #include <Fusion/Features/ThreadFeatureInput.h>  // Get the value of the property. boolean propertyValue = threadFeatureInput_var->isRightHanded();  // Set the value of the property, where value_var is a boolean. bool returnValue = threadFeatureInput_var->isRightHanded(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2015
Retired in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |