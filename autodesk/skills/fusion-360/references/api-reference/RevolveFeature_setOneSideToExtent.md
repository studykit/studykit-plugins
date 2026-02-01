# RevolveFeature.setOneSideToExtent Method

Parent Object: [RevolveFeature](RevolveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeature.h>

## Description

Changes the extent of the revolve to be from the sketch plane to the specified "to" face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeature\_var" is a variable referencing a [RevolveFeature](RevolveFeature.htm) object.```` ``` # Uses no optional arguments. returnValue = revolveFeature_var.setOneSideToExtent(toEntity)  # Uses optional arguments. returnValue = revolveFeature_var.setOneSideToExtent(toEntity, directionHint) ``` ```` |

"revolveFeature\_var" is a variable referencing a [RevolveFeature](RevolveFeature.htm) object.  ```` ``` #include <Fusion/Features/RevolveFeature.h>  // Uses no optional arguments. returnValue = revolveFeature_var->setOneSideToExtent(toEntity);  // Uses optional arguments. returnValue = revolveFeature_var->setOneSideToExtent(toEntity, directionHint); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| toEntity | [Base](Base.htm) | The entity that defines the "to" extent. The valid types of entities can vary depending on the type of feature this is being used with. For a revolve it can be a BRepBody, BRepFace, BRepVertex, ConstructionPlane, or ConstructionPoint. |
| directionHint | [Vector3D](Vector3D.htm) | Specifies the direction of the revolve.   This is an optional argument whose default value is null. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |