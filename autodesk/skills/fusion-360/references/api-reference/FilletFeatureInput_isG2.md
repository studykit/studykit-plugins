# FilletFeatureInput.isG2 Property

Parent Object: [FilletFeatureInput](FilletFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeatureInput.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property is obsolete. You should now use the continuity property on the EdgeSetInput object to control the continuity. define new fillets.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeatureInput\_var" is a variable referencing a FilletFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = filletFeatureInput_var.isG2  # Set the value of the property. filletFeatureInput_var.isG2 = propertyValue ``` ```` |

"filletFeatureInput\_var" is a variable referencing a FilletFeatureInput object. ```` ``` #include <Fusion/Features/FilletFeatureInput.h>  // Get the value of the property. boolean propertyValue = filletFeatureInput_var->isG2();  // Set the value of the property, where value_var is a boolean. bool returnValue = filletFeatureInput_var->isG2(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2014
Retired in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |