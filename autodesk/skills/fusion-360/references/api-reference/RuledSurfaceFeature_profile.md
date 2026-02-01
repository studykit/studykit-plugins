# RuledSurfaceFeature.profile Property

Parent Object: [RuledSurfaceFeature](RuledSurfaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeature.h>

## Description

Gets and sets the Profile object that defines the sketch geometry or edges that define the shape of the ruled surface. The Component.createBRepEdgeProfile method is useful to create a profile defined from edges.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeature\_var" is a variable referencing a RuledSurfaceFeature object.  ```` ``` # Get the value of the property. propertyValue = ruledSurfaceFeature_var.profile  # Set the value of the property. ruledSurfaceFeature_var.profile = propertyValue ``` ```` |

"ruledSurfaceFeature\_var" is a variable referencing a RuledSurfaceFeature object. ```` ``` #include <Fusion/Features/RuledSurfaceFeature.h>  // Get the value of the property. Ptr<Base> propertyValue = ruledSurfaceFeature_var->profile();  // Set the value of the property, where value_var is a Base. bool returnValue = ruledSurfaceFeature_var->profile(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |