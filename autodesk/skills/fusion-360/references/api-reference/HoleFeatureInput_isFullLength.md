# HoleFeatureInput.isFullLength Property

Parent Object: [HoleFeatureInput](HoleFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeatureInput.h>

## Description

Gets and sets if this thread is the full length of the hole. It defaults to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeatureInput\_var" is a variable referencing a HoleFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = holeFeatureInput_var.isFullLength  # Set the value of the property. holeFeatureInput_var.isFullLength = propertyValue ``` ```` |

"holeFeatureInput\_var" is a variable referencing a HoleFeatureInput object. ```` ``` #include <Fusion/Features/HoleFeatureInput.h>  // Get the value of the property. boolean propertyValue = holeFeatureInput_var->isFullLength();  // Set the value of the property, where value_var is a boolean. bool returnValue = holeFeatureInput_var->isFullLength(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |