# ExtrudeFeatureInput.profile Property

Parent Object: [ExtrudeFeatureInput](ExtrudeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatureInput.h>

## Description

Gets and sets the profiles or planar faces used to define the shape of the extrude. This property can return or be set with a single profile, a single planar face, or an ObjectCollection consisting of multiple profiles and planar faces. When an ObjectCollection is used all of the profiles and faces must be co-planar.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatureInput\_var" is a variable referencing an ExtrudeFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = extrudeFeatureInput_var.profile  # Set the value of the property. extrudeFeatureInput_var.profile = propertyValue ``` ```` |

"extrudeFeatureInput\_var" is a variable referencing an ExtrudeFeatureInput object. ```` ``` #include <Fusion/Features/ExtrudeFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = extrudeFeatureInput_var->profile();  // Set the value of the property, where value_var is a Base. bool returnValue = extrudeFeatureInput_var->profile(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |