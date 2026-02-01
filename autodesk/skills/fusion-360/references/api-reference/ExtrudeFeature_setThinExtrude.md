# ExtrudeFeature.setThinExtrude Method

Parent Object: [ExtrudeFeature](ExtrudeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeature.h>

## Description

Changes the extrude feature to be a thin extrude. This is only valid if the isThinExtrude property is False. If the extrusion is already a thin extrude, you can use the properties on the ExtrudeFeature to modify the thin extrude specific values.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeature\_var" is a variable referencing an [ExtrudeFeature](ExtrudeFeature.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"extrudeFeature\_var" is a variable referencing an [ExtrudeFeature](ExtrudeFeature.htm) object.  ```` ``` #include <Fusion/Features/ExtrudeFeature.h>  // Uses no optional arguments. returnValue = extrudeFeature_var->setThinExtrude(thinExtrudeWallLocationOne, thinExtrudeWallThicknessOne);  // Uses optional arguments. returnValue = extrudeFeature_var->setThinExtrude(thinExtrudeWallLocationOne, thinExtrudeWallThicknessOne, thinExtrudeWallLocationTwo, thinExtrudeWallThicknessTwo); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| thinExtrudeWallLocationOne | [ThinExtrudeWallLocation](ThinExtrudeWallLocation.htm) | Specifies the position of the thin wall extrude with respect to the profile being extruded. This defines the direction for a single sided thin extrude or side one of a two-sided extrusion. |
| thinExtrudeWallThicknessOne | [ValueInput](ValueInput.htm) | A ValueInput object that defines the thickness for a single sided thin extrude or side one of a two-sided extrusion . |
| thinExtrudeWallLocationTwo | [ThinExtrudeWallLocation](ThinExtrudeWallLocation.htm) | Optional argument that specifies the position of side two of a two-sided extrusion. This argument is ignored for a single sided thin extrude.   This is an optional argument whose default value is ThinExtrudeWallLocation.Side1. |
| thinExtrudeWallThicknessTwo | [ValueInput](ValueInput.htm) | Optional argument that is a ValueInput object that defines the thickness for side two of a two-sided extrusion. This argument is ignored for a single sided thin extrude.   This is an optional argument whose default value is null. |

## Version

Introduced in version April 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |