# ExtrudeFeature.setOneSideExtent Method

Parent Object: [ExtrudeFeature](ExtrudeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeature.h>

## Description

Redefines the extrusion to go in one direction from the profile. The extent of the extrusion is defined by the extent argument.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeature\_var" is a variable referencing an [ExtrudeFeature](ExtrudeFeature.htm) object.```` ``` # Uses no optional arguments. returnValue = extrudeFeature_var.setOneSideExtent(extent, direction)  # Uses optional arguments. returnValue = extrudeFeature_var.setOneSideExtent(extent, direction, taperAngle) ``` ```` |

"extrudeFeature\_var" is a variable referencing an [ExtrudeFeature](ExtrudeFeature.htm) object.  ```` ``` #include <Fusion/Features/ExtrudeFeature.h>  // Uses no optional arguments. returnValue = extrudeFeature_var->setOneSideExtent(extent, direction);  // Uses optional arguments. returnValue = extrudeFeature_var->setOneSideExtent(extent, direction, taperAngle); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true is setting the input to a one sided extent was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| extent | [ExtentDefinition](ExtentDefinition.htm) | An ExtentDefinition object that defines how the extent of the extrusion is defined. This can be a specified distance (DistanceExtentDefinition), to an entity (ToEntityExtent), or through-all (AllExtentDefinition). These objects can be obtained by using the static create method on the appropriate class. |
| direction | [ExtentDirections](ExtentDirections.htm) | Specifies the direction of the extrusion. PositiveExtentDirection and NegativeExtentDirection are valid values. PositiveExtentDirection is in the same direction as the normal of the profile's parent sketch plane. |
| taperAngle | [ValueInput](ValueInput.htm) | Optional argument that specifies the taper angle. If omitted a taper angle of 0 is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |