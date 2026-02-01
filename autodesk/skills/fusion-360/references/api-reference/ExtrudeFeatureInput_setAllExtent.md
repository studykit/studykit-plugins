# ExtrudeFeatureInput.setAllExtent Method

Parent Object: [ExtrudeFeatureInput](ExtrudeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatureInput.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This method has been retired and is replaced with the setOneSideExtent and SetTwoSidesExtent, passing in a ThroughAllExtentDefinition. This method continues to work to allow the API to remain backward compatible, but it is no longer officially supported.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatureInput\_var" is a variable referencing an [ExtrudeFeatureInput](ExtrudeFeatureInput.htm) object.```` ``` returnValue = extrudeFeatureInput_var.setAllExtent(direction) ``` ```` |

"extrudeFeatureInput\_var" is a variable referencing an [ExtrudeFeatureInput](ExtrudeFeatureInput.htm) object.  ```` ``` #include <Fusion/Features/ExtrudeFeatureInput.h>  returnValue = extrudeFeatureInput_var->setAllExtent(direction); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| direction | [ExtentDirections](ExtentDirections.htm) | The direction can be either positive, negative, or symmetric. |

## Version

Introduced in version August 2014
Retired in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |