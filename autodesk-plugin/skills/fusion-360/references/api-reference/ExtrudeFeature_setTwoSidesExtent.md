# ExtrudeFeature.setTwoSidesExtent Method

Parent Object: [ExtrudeFeature](ExtrudeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeature.h>

## Description

Redefines the extrusion to go in both directions from the profile. The extent is defined independently for each direction using the input arguments.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeature\_var" is a variable referencing an [ExtrudeFeature](ExtrudeFeature.htm) object.```` ``` # Uses no optional arguments. returnValue = extrudeFeature_var.setTwoSidesExtent(sideOneExtent, sideTwoExtent)  # Uses optional arguments. returnValue = extrudeFeature_var.setTwoSidesExtent(sideOneExtent, sideTwoExtent, sideOneTaperAngle, sideTwoTaperAngle) ``` ```` |

"extrudeFeature\_var" is a variable referencing an [ExtrudeFeature](ExtrudeFeature.htm) object.  ```` ``` #include <Fusion/Features/ExtrudeFeature.h>  // Uses no optional arguments. returnValue = extrudeFeature_var->setTwoSidesExtent(sideOneExtent, sideTwoExtent);  // Uses optional arguments. returnValue = extrudeFeature_var->setTwoSidesExtent(sideOneExtent, sideTwoExtent, sideOneTaperAngle, sideTwoTaperAngle); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true, if the call was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sideOneExtent | [ExtentDefinition](ExtentDefinition.htm) | An ExtentDefinition object that defines how the extent of the extrusion towards side one is defined. This can be a specified distance (DistanceExtentDefinition), to an entity (ToEntityExtent), or through-all (AllExtentDefinition). These objects can be obtained by using the static create method on the appropriate class. |
| sideTwoExtent | [ExtentDefinition](ExtentDefinition.htm) | An ExtentDefinition object that defines how the extent of the extrusion towards side two is defined. This can be a specified distance (DistanceExtentDefinition), to an entity (ToEntityExtent), or through-all (AllExtentDefinition). These objects can be obtained by using the static create method on the appropriate class. |
| sideOneTaperAngle | [ValueInput](ValueInput.htm) | Optional argument that specifies the taper angle for side one. If omitted a taper angle of 0 is used.   This is an optional argument whose default value is null. |
| sideTwoTaperAngle | [ValueInput](ValueInput.htm) | Optional argument that specifies the taper angle for side two. If omitted a taper angle of 0 is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |