# RuledSurfaceFeatureInput.cornerType Property

Parent Object: [RuledSurfaceFeatureInput](RuledSurfaceFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeatureInput.h>

## Description

Gets and sets the corner type for the ruled surface, indicating if the corners will be rounded or mitered. The default value is rounded.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeatureInput\_var" is a variable referencing a RuledSurfaceFeatureInput object. |

"ruledSurfaceFeatureInput\_var" is a variable referencing a RuledSurfaceFeatureInput object. ```` ``` #include <Fusion/Features/RuledSurfaceFeatureInput.h>  // Get the value of the property. RuledSurfaceCornerTypes propertyValue = ruledSurfaceFeatureInput_var->cornerType();  // Set the value of the property, where value_var is a RuledSurfaceCornerTypes. bool returnValue = ruledSurfaceFeatureInput_var->cornerType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [RuledSurfaceCornerTypes](RuledSurfaceCornerTypes.htm).

## Version

Introduced in version August 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |