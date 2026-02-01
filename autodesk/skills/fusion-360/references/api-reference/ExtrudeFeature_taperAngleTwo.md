# ExtrudeFeature.taperAngleTwo Property

Parent Object: [ExtrudeFeature](ExtrudeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeature.h>

## Description

Gets the parameter controlling the taper angle for side two of a two-sided extrusion. if the extrusion is single-sided, this property will return null. The hasTwoExtents property can be used to determine if there are two sides or not. To edit the angle, use properties on the parameter to change the value of the parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeature\_var" is a variable referencing an ExtrudeFeature object. |

"extrudeFeature\_var" is a variable referencing an ExtrudeFeature object. ```` ``` #include <Fusion/Features/ExtrudeFeature.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = extrudeFeature_var->taperAngleTwo(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |