# RuledSurfaceFeature.alternateFace Property

Parent Object: [RuledSurfaceFeature](RuledSurfaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeature.h>

## Description

Gets and sets if the other face is used for creation of the Ruled Surface. When creating a ruled surface using the edges of a solid or the interior edges of a surface the angle of the ruled surface is measured with respect to the face the selected edge is bounding. For a solid, or an interior edge on a surface, the edge connects to two faces. This setting toggles which of the two faces will be used for measuring the angle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeature\_var" is a variable referencing a RuledSurfaceFeature object. |

"ruledSurfaceFeature\_var" is a variable referencing a RuledSurfaceFeature object. ```` ``` #include <Fusion/Features/RuledSurfaceFeature.h>  // Get the value of the property. boolean propertyValue = ruledSurfaceFeature_var->alternateFace();  // Set the value of the property, where value_var is a boolean. bool returnValue = ruledSurfaceFeature_var->alternateFace(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |