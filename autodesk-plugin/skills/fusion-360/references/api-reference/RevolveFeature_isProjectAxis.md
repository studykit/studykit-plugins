# RevolveFeature.isProjectAxis Property

Parent Object: [RevolveFeature](RevolveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeature.h>

## Description

Specifies if the axis should be projected on the same plane as the profile sketch plane or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeature\_var" is a variable referencing a RevolveFeature object.  ```` ``` # Get the value of the property. propertyValue = revolveFeature_var.isProjectAxis  # Set the value of the property. revolveFeature_var.isProjectAxis = propertyValue ``` ```` |

"revolveFeature\_var" is a variable referencing a RevolveFeature object. ```` ``` #include <Fusion/Features/RevolveFeature.h>  // Get the value of the property. boolean propertyValue = revolveFeature_var->isProjectAxis();  // Set the value of the property, where value_var is a boolean. bool returnValue = revolveFeature_var->isProjectAxis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |