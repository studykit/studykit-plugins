# ExtrudeFeature.thinExtrudeWallLocationTwo Property

Parent Object: [ExtrudeFeature](ExtrudeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeature.h>

## Description

Gets and sets the wall location for side two of a two sided thin extrude

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeature\_var" is a variable referencing an ExtrudeFeature object. |

"extrudeFeature\_var" is a variable referencing an ExtrudeFeature object. ```` ``` #include <Fusion/Features/ExtrudeFeature.h>  // Get the value of the property. ThinExtrudeWallLocation propertyValue = extrudeFeature_var->thinExtrudeWallLocationTwo();  // Set the value of the property, where value_var is a ThinExtrudeWallLocation. bool returnValue = extrudeFeature_var->thinExtrudeWallLocationTwo(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ThinExtrudeWallLocation](ThinExtrudeWallLocation.htm).

## Version

Introduced in version April 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |