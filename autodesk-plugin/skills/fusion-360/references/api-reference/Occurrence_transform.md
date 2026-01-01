# Occurrence.transform Property

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property has been retired and replaced by the transform2 property. This method remains and has the same behavior as before. It returns incorrect results in some cases but some existing programs may be relying on these bad results so this property remains unchanged. It will be best to use the transform2 property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an Occurrence object.  ```` ``` # Get the value of the property. propertyValue = occurrence_var.transform  # Set the value of the property. occurrence_var.transform = propertyValue ``` ```` |

"occurrence\_var" is a variable referencing an Occurrence object. ```` ``` #include <Fusion/Components/Occurrence.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = occurrence_var->transform();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = occurrence_var->transform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version August 2014
Retired in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |