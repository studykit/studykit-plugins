# RecognizedHole.axis Property

Parent Object: [RecognizedHole](RecognizedHole.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/HoleRecognition/RecognizedHole.h>

## Description

Returns the unit vector that points straight up out of the hole in the global coordinate system.

## Syntax

* [Python](#Python)
* [C++](#C++)

"recognizedHole\_var" is a variable referencing a RecognizedHole object. |

"recognizedHole\_var" is a variable referencing a RecognizedHole object. ```` ``` #include <Cam/HoleRecognition/RecognizedHole.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = recognizedHole_var->axis(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Setups From Hole Recognition API Sample](CreateSetupsFromHoleRecognition_Sample.htm) | This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.  The Fusion Manufacturing Extension is required for Hole Recognition.  The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector. |

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |