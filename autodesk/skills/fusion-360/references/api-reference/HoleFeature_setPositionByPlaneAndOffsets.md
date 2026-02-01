# HoleFeature.setPositionByPlaneAndOffsets Method

Parent Object: [HoleFeature](HoleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

Redefines the orientation of the hole using a planar face or construction plane. The position of the hole is defined by the distance from one or two edges.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeature\_var" is a variable referencing a [HoleFeature](HoleFeature.htm) object.```` ``` # Uses no optional arguments. returnValue = holeFeature_var.setPositionByPlaneAndOffsets(planarEntity, point, edgeOne, offsetOne)  # Uses optional arguments. returnValue = holeFeature_var.setPositionByPlaneAndOffsets(planarEntity, point, edgeOne, offsetOne, edgeTwo, offsetTwo) ``` ```` |

"holeFeature\_var" is a variable referencing a [HoleFeature](HoleFeature.htm) object.  ```` ``` #include <Fusion/Features/HoleFeature.h>  // Uses no optional arguments. returnValue = holeFeature_var->setPositionByPlaneAndOffsets(planarEntity, point, edgeOne, offsetOne);  // Uses optional arguments. returnValue = holeFeature_var->setPositionByPlaneAndOffsets(planarEntity, point, edgeOne, offsetOne, edgeTwo, offsetTwo); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| planarEntity | [Base](Base.htm) | The planar BRepFace or ConstructionPlane object that defines the orientation of the hole. The natural direction of the hole will be opposite the normal of the face or construction plane. |
| point | [Point3D](Point3D.htm) | A Point3D object that defines the approximate initial position of the hole. The point will be projected onto the plane. This point should be close to the final position of the hole and is used to determine which solution out of several possible solutions should be chosen for the hole location. |
| edgeOne | [BRepEdge](BRepEdge.htm) | A linear BRepEdge object that the position of the hole will be measured from. The position of the hole will be measured along a perpendicular from this edge. |
| offsetOne | [ValueInput](ValueInput.htm) | A ValueInput object that defines the offset distance from edgeOne. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "3 in"). If no units are specified it is interpreted using the current default units for length. |
| edgeTwo | [BRepEdge](BRepEdge.htm) | You can optionally define a second edge and offset to specify the position of the hole. If you use a second edge it has the same requirements as the edgeOne argument. If you provide a second edge you must also provide the offsetTwo argument.   This is an optional argument whose default value is null. |
| offsetTwo | [ValueInput](ValueInput.htm) | If edgeTwo is defined, you must provide this argument which is a ValueInput object that defines the offset from the edgeTwo. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "3 in"). If no units are specified it is interpreted using the current default units for length.   This is an optional argument whose default value is null. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |