# RevolveFeatureInput.isProjectAxis Property

Parent Object: [RevolveFeatureInput](RevolveFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeatureInput.h>

## Description

Specifies if the axis should be projected on the same plane as the profile sketch plane or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeatureInput\_var" is a variable referencing a RevolveFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = revolveFeatureInput_var.isProjectAxis  # Set the value of the property. revolveFeatureInput_var.isProjectAxis = propertyValue ``` ```` |

"revolveFeatureInput\_var" is a variable referencing a RevolveFeatureInput object. ```` ``` #include <Fusion/Features/RevolveFeatureInput.h>  // Get the value of the property. boolean propertyValue = revolveFeatureInput_var->isProjectAxis();  // Set the value of the property, where value_var is a boolean. bool returnValue = revolveFeatureInput_var->isProjectAxis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |