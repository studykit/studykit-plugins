# RuledSurfaceFeatureInput.ruledSurfaceType Property

Parent Object: [RuledSurfaceFeatureInput](RuledSurfaceFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeatureInput.h>

## Description

Gets and sets the type of ruled surface to create. To set this to DirectionRuledSurfaceType, use the direction property to set the direction entity, which will automatically set this to DirectionRuledSurfaceType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeatureInput\_var" is a variable referencing a RuledSurfaceFeatureInput object. |

"ruledSurfaceFeatureInput\_var" is a variable referencing a RuledSurfaceFeatureInput object. ```` ``` #include <Fusion/Features/RuledSurfaceFeatureInput.h>  // Get the value of the property. RuledSurfaceTypes propertyValue = ruledSurfaceFeatureInput_var->ruledSurfaceType();  // Set the value of the property, where value_var is a RuledSurfaceTypes. bool returnValue = ruledSurfaceFeatureInput_var->ruledSurfaceType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [RuledSurfaceTypes](RuledSurfaceTypes.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |