# FilletFeature.isG2 Property

Parent Object: [FilletFeature](FilletFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeature.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property is obsolete. You should now use the continuity property on the FilletEdgeSet object to control the continuity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeature\_var" is a variable referencing a FilletFeature object.  ```` ``` # Get the value of the property. propertyValue = filletFeature_var.isG2  # Set the value of the property. filletFeature_var.isG2 = propertyValue ``` ```` |

"filletFeature\_var" is a variable referencing a FilletFeature object. ```` ``` #include <Fusion/Features/FilletFeature.h>  // Get the value of the property. boolean propertyValue = filletFeature_var->isG2();  // Set the value of the property, where value_var is a boolean. bool returnValue = filletFeature_var->isG2(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2014
Retired in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |