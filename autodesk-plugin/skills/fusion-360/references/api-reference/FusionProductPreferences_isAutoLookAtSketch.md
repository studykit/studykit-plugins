# FusionProductPreferences.isAutoLookAtSketch Property

Parent Object: [FusionProductPreferences](FusionProductPreferences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionProductPreferences.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

Gets and sets if the view is re-oriented to view the newly created sketch.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionProductPreferences\_var" is a variable referencing a FusionProductPreferences object.  ```` ``` # Get the value of the property. propertyValue = fusionProductPreferences_var.isAutoLookAtSketch  # Set the value of the property. fusionProductPreferences_var.isAutoLookAtSketch = propertyValue ``` ```` |

"fusionProductPreferences\_var" is a variable referencing a FusionProductPreferences object. ```` ``` #include <Fusion/Fusion/FusionProductPreferences.h>  // Get the value of the property. boolean propertyValue = fusionProductPreferences_var->isAutoLookAtSketch();  // Set the value of the property, where value_var is a boolean. bool returnValue = fusionProductPreferences_var->isAutoLookAtSketch(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015
Retired in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |