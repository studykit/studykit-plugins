# FilletFeatureInput.isRollingBallCorner Property

Parent Object: [FilletFeatureInput](FilletFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeatureInput.h>

## Description

Gets and sets if a rolling ball or setback solution is to be used in any corners.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeatureInput\_var" is a variable referencing a FilletFeatureInput object. |

"filletFeatureInput\_var" is a variable referencing a FilletFeatureInput object. ```` ``` #include <Fusion/Features/FilletFeatureInput.h>  // Get the value of the property. boolean propertyValue = filletFeatureInput_var->isRollingBallCorner();  // Set the value of the property, where value_var is a boolean. bool returnValue = filletFeatureInput_var->isRollingBallCorner(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Fillet Feature API Sample](FilletFeatureSample_Sample.htm) | Demonstrates creating fillets using the various types of fillets. Create a new design and add a box that is at least 2 cm on each side. The script creates a constant radius, variable radius and chord length fillets. After creating each one, it deletes it and then creates the next. To see any of the fillets that were deleted, undo to get the fillet back. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |