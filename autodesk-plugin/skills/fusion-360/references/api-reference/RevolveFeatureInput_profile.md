# RevolveFeatureInput.profile Property

Parent Object: [RevolveFeatureInput](RevolveFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeatureInput.h>

## Description

Gets and sets the profiles or planar faces used to define the shape of the revolve. This property can return or be set with a single Profile, a single planar face, or an ObjectCollection consisting of multiple profiles and planar faces. When an ObjectCollection is used all of the profiles and faces must be co-planar. This property returns null in the case where the feature is non-parametric.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeatureInput\_var" is a variable referencing a RevolveFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = revolveFeatureInput_var.profile  # Set the value of the property. revolveFeatureInput_var.profile = propertyValue ``` ```` |

"revolveFeatureInput\_var" is a variable referencing a RevolveFeatureInput object. ```` ``` #include <Fusion/Features/RevolveFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = revolveFeatureInput_var->profile();  // Set the value of the property, where value_var is a Base. bool returnValue = revolveFeatureInput_var->profile(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |