# RuledSurfaceFeatureInput.direction Property

Parent Object: [RuledSurfaceFeatureInput](RuledSurfaceFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeatureInput.h>

## Description

Gets and sets the entity that defines the direction when the ruled surface type is DirectionRuledSurfaceType. The direction is specified by providing a linear or planar entity. For example, a linear edge, construction axis, planar face, or construction plane can be used as input.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeatureInput\_var" is a variable referencing a RuledSurfaceFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = ruledSurfaceFeatureInput_var.direction  # Set the value of the property. ruledSurfaceFeatureInput_var.direction = propertyValue ``` ```` |

"ruledSurfaceFeatureInput\_var" is a variable referencing a RuledSurfaceFeatureInput object. ```` ``` #include <Fusion/Features/RuledSurfaceFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = ruledSurfaceFeatureInput_var->direction();  // Set the value of the property, where value_var is a Base. bool returnValue = ruledSurfaceFeatureInput_var->direction(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |