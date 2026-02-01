# Vector3D.normalize Method

Parent Object: [Vector3D](Vector3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Vector3D.h>

## Description

Makes this vector of unit length. This vector should not be zero length.

## Syntax

* [Python](#Python)
* [C++](#C++)

"vector3D\_var" is a variable referencing a [Vector3D](Vector3D.htm) object.```` ``` returnValue = vector3D_var.normalize() ``` ```` |

"vector3D\_var" is a variable referencing a [Vector3D](Vector3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Setups From Hole Recognition API Sample](CreateSetupsFromHoleRecognition_Sample.htm) | This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.  The Fusion Manufacturing Extension is required for Hole Recognition.  The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |