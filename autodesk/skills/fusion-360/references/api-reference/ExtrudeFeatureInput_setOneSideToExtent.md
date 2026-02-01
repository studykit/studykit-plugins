# ExtrudeFeatureInput.setOneSideToExtent Method

Parent Object: [ExtrudeFeatureInput](ExtrudeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatureInput.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This method has been retired and is replaced with the new setOneSideExtent and passing in a ToEntityExtentDefinition. This method continues to work to allow the API to remain backward compatible, but it is no longer officially supported.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatureInput\_var" is a variable referencing an [ExtrudeFeatureInput](ExtrudeFeatureInput.htm) object.```` ``` # Uses no optional arguments. returnValue = extrudeFeatureInput_var.setOneSideToExtent(toEntity, matchShape)  # Uses optional arguments. returnValue = extrudeFeatureInput_var.setOneSideToExtent(toEntity, matchShape, directionHint) ``` ```` |

"extrudeFeatureInput\_var" is a variable referencing an [ExtrudeFeatureInput](ExtrudeFeatureInput.htm) object.  ```` ``` #include <Fusion/Features/ExtrudeFeatureInput.h>  // Uses no optional arguments. returnValue = extrudeFeatureInput_var->setOneSideToExtent(toEntity, matchShape);  // Uses optional arguments. returnValue = extrudeFeatureInput_var->setOneSideToExtent(toEntity, matchShape, directionHint); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| toEntity | [Base](Base.htm) | The entity that defines the "to" extent. The valid types of entities can vary depending on the type of feature this is being used with. For an extrude it can be a BRepBody, BRepFace, BRepVertex, ConstructionPlane, or ConstructionPoint. |
| matchShape | boolean | If the matchShape argument is 'true', the toEntity is extended to fully intersect the extrusion. |
| directionHint | [Vector3D](Vector3D.htm) | Specifies the direction of the extrusion. This is only used in the case where there are two possible solutions and the extrusion can hit the toEntity in either direction. An example is if the profile of the extrusion is within a hole. The extrusion will intersect the cylinder of the hole in either direction.   Typically there is only a single solution and the direction is determined automatically.   This is an optional argument whose default value is null. |

## Version

Introduced in version August 2014
Retired in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |