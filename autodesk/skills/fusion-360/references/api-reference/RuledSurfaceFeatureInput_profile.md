# RuledSurfaceFeatureInput.profile Property

Parent Object: [RuledSurfaceFeatureInput](RuledSurfaceFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeatureInput.h>

## Description

Gets and sets the Profile object that defines the sketch geometry or edges that define the shape of the ruled surface. The Component.createBRepEdgeProfile method is useful to create a profile defined from edges.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeatureInput\_var" is a variable referencing a RuledSurfaceFeatureInput object. |

"ruledSurfaceFeatureInput\_var" is a variable referencing a RuledSurfaceFeatureInput object. ```` ``` #include <Fusion/Features/RuledSurfaceFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = ruledSurfaceFeatureInput_var->profile();  // Set the value of the property, where value_var is a Base. bool returnValue = ruledSurfaceFeatureInput_var->profile(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |