# RevolveFeatureInput.setOneSideToExtent Method

Parent Object: [RevolveFeatureInput](RevolveFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RevolveFeatureInput.h>

## Description

Defines the extent of the revolve to be from the sketch or profile plane to the specified "To" face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"revolveFeatureInput\_var" is a variable referencing a [RevolveFeatureInput](RevolveFeatureInput.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"revolveFeatureInput\_var" is a variable referencing a [RevolveFeatureInput](RevolveFeatureInput.htm) object.  ```` ``` #include <Fusion/Features/RevolveFeatureInput.h>  // Uses no optional arguments. returnValue = revolveFeatureInput_var->setOneSideToExtent(toEntity);  // Uses optional arguments. returnValue = revolveFeatureInput_var->setOneSideToExtent(toEntity, directionHint); ``` ```` |

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