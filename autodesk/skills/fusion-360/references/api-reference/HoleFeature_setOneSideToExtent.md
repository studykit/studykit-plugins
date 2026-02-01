# HoleFeature.setOneSideToExtent Method

Parent Object: [HoleFeature](HoleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

Sets the extent of the hole to be from the sketch plane to the specified "to" face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeature\_var" is a variable referencing a [HoleFeature](HoleFeature.htm) object.```` ``` # Uses no optional arguments. returnValue = holeFeature_var.setOneSideToExtent(toEntity, matchShape)  # Uses optional arguments. returnValue = holeFeature_var.setOneSideToExtent(toEntity, matchShape, directionHint) ``` ```` |

"holeFeature\_var" is a variable referencing a [HoleFeature](HoleFeature.htm) object.  ```` ``` #include <Fusion/Features/HoleFeature.h>  // Uses no optional arguments. returnValue = holeFeature_var->setOneSideToExtent(toEntity, matchShape);  // Uses optional arguments. returnValue = holeFeature_var->setOneSideToExtent(toEntity, matchShape, directionHint); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| toEntity | [Base](Base.htm) | The entity that defines the "to" extent. The valid types of entities can vary depending on the type of feature this is being used with. For a hole it can be a BRepBody, BRepFace, BRepVertex, ConstructionPlane, or ConstructionPoint. |
| matchShape | boolean | Indicates if the hole is not contained on the face that the hole should match the shape of the entity as if it extended beyond its current boundaries. |
| directionHint | [Vector3D](Vector3D.htm) | Specifies the direction of the hole. This is only used in the case where there are two possible solutions and the hole can hit the toEntity in either direction.   Typically there is only a single solution and the direction is determined automatically.   This is an optional argument whose default value is null. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |