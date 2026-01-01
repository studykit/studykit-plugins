# RuledSurfaceFeature.ruledSurfaceType Property

Parent Object: [RuledSurfaceFeature](RuledSurfaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeature.h>

## Description

Gets and sets the type of ruled surface. To set this to DirectionRuledSurfaceType, use the direction property to set the direction entity, which will automatically set this to DirectionRuledSurfaceType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeature\_var" is a variable referencing a RuledSurfaceFeature object. |

"ruledSurfaceFeature\_var" is a variable referencing a RuledSurfaceFeature object. ```` ``` #include <Fusion/Features/RuledSurfaceFeature.h>  // Get the value of the property. RuledSurfaceTypes propertyValue = ruledSurfaceFeature_var->ruledSurfaceType();  // Set the value of the property, where value_var is a RuledSurfaceTypes. bool returnValue = ruledSurfaceFeature_var->ruledSurfaceType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [RuledSurfaceTypes](RuledSurfaceTypes.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |