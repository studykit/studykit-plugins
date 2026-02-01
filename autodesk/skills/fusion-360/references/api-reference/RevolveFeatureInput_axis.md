# RevolveFeatureInput.axis Property

Parent Object: [RevolveFeatureInput](RevolveFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeatureInput.h>

## Description

Gets and sets the entity used to define the axis of revolution. The axis can be a sketch line, construction axis, linear edge or a face that defines an axis (cylinder, cone, torus, etc.). If it is not in the same plane as the profile, it is projected onto the profile plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeatureInput\_var" is a variable referencing a RevolveFeatureInput object. |

"revolveFeatureInput\_var" is a variable referencing a RevolveFeatureInput object. ```` ``` #include <Fusion/Features/RevolveFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = revolveFeatureInput_var->axis();  // Set the value of the property, where value_var is a Base. bool returnValue = revolveFeatureInput_var->axis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |