# ExtrudeFeatureInput.setDistanceExtent Method

Parent Object: [ExtrudeFeatureInput](ExtrudeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatureInput.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This method has been retired and is replaced with the new SetOneSideExtent and passing in either a DistanceExtentDefinition or SymmetricExtentDefinition. This method continues to work for the API to remain backward compatible but it is not longer officially supported.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatureInput\_var" is a variable referencing an [ExtrudeFeatureInput](ExtrudeFeatureInput.htm) object.```` ``` returnValue = extrudeFeatureInput_var.setDistanceExtent(isSymmetric, distance) ``` ```` |

"extrudeFeatureInput\_var" is a variable referencing an [ExtrudeFeatureInput](ExtrudeFeatureInput.htm) object.  ```` ``` #include <Fusion/Features/ExtrudeFeatureInput.h>  returnValue = extrudeFeatureInput_var->setDistanceExtent(isSymmetric, distance); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| isSymmetric | boolean | Set to 'true' for an extrusion symmetrical about the profile plane |
| distance | [ValueInput](ValueInput.htm) | ValueInput object that defines the extrude distance. If the isSymmetric argument is 'false', a positive or negative distance can be used to control the direction. |

## Version

Introduced in version November 2016
Retired in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |