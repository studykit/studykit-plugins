# RuledSurfaceFeatures.createInput Method

Parent Object: [RuledSurfaceFeatures](RuledSurfaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeatures.h>

## Description

Creates a RuledSurfaceFeatureInput object that defines the input needed to create a ruled surface feature. Use the input object to define the input to create the desired feature and then use the Add method, passing in the RuledSurfaceFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeatures\_var" is a variable referencing a [RuledSurfaceFeatures](RuledSurfaceFeatures.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"ruledSurfaceFeatures\_var" is a variable referencing a [RuledSurfaceFeatures](RuledSurfaceFeatures.htm) object.  ```` ``` #include <Fusion/Features/RuledSurfaceFeatures.h>  // Uses no optional arguments. returnValue = ruledSurfaceFeatures_var->createInput(profile, distance, angle, ruledSurfaceType);  // Uses optional arguments. returnValue = ruledSurfaceFeatures_var->createInput(profile, distance, angle, ruledSurfaceType, direction); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RuledSurfaceFeatureInput](RuledSurfaceFeatureInput.htm) | Returns the newly created RuledSurfaceFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| profile | [Base](Base.htm) | A Profile object that defines the sketch geometry or edges that define the shape of the ruled surface. The Component.createBRepEdgeProfile method is useful to create a profile defined from edges. |
| distance | [ValueInput](ValueInput.htm) | ValueInput object that defines the extension distance of the Ruled Surface.. |
| angle | [ValueInput](ValueInput.htm) | ValueInput object that defines angle to use when creating the Ruled Surface. When the input is a real value, the units are radians. |
| ruledSurfaceType | [RuledSurfaceTypes](RuledSurfaceTypes.htm) | The Ruled Surface type (TangentRuledSurfaceType, NormalRuledSurfaceType, or DirectionRuledSurfaceType). |
| direction | [Base](Base.htm) | If the ruled surface type is DirectionRuledSurfaceType, you must specify the direction. The direction is specified by providing a linear or planar entity. For example, a linear edge, construction axis, planar face, or construction plane can be used as input.   This is an optional argument whose default value is null. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |