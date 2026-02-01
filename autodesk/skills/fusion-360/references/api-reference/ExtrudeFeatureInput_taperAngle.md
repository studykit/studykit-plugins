# ExtrudeFeatureInput.taperAngle Property

Parent Object: [ExtrudeFeatureInput](ExtrudeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatureInput.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property has been retired and is replaced by getting the extent definition for each direction and using it to set the taper angle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatureInput\_var" is a variable referencing an ExtrudeFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = extrudeFeatureInput_var.taperAngle  # Set the value of the property. extrudeFeatureInput_var.taperAngle = propertyValue ``` ```` |

"extrudeFeatureInput\_var" is a variable referencing an ExtrudeFeatureInput object. ```` ``` #include <Fusion/Features/ExtrudeFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = extrudeFeatureInput_var->taperAngle();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = extrudeFeatureInput_var->taperAngle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version August 2014
Retired in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |