# ExtrudeFeatureInput.thinExtrudeWallLocationTwo Property

Parent Object: [ExtrudeFeatureInput](ExtrudeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatureInput.h>

## Description

Gets and sets the wall location for side two of a two sided thin extrude

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatureInput\_var" is a variable referencing an ExtrudeFeatureInput object. |

"extrudeFeatureInput\_var" is a variable referencing an ExtrudeFeatureInput object. ```` ``` #include <Fusion/Features/ExtrudeFeatureInput.h>  // Get the value of the property. ThinExtrudeWallLocation propertyValue = extrudeFeatureInput_var->thinExtrudeWallLocationTwo();  // Set the value of the property, where value_var is a ThinExtrudeWallLocation. bool returnValue = extrudeFeatureInput_var->thinExtrudeWallLocationTwo(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ThinExtrudeWallLocation](ThinExtrudeWallLocation.htm).

## Version

Introduced in version April 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |