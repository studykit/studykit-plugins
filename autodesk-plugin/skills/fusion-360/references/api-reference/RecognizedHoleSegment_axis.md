# RecognizedHoleSegment.axis Property

Parent Object: [RecognizedHoleSegment](RecognizedHoleSegment.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/HoleRecognition/RecognizedHoleSegment.h>

## Description

Returns the unit vector that points straight up out of the segment in the global coordinate system.

## Syntax

* [Python](#Python)
* [C++](#C++)

"recognizedHoleSegment\_var" is a variable referencing a RecognizedHoleSegment object. |

"recognizedHoleSegment\_var" is a variable referencing a RecognizedHoleSegment object. ```` ``` #include <Cam/HoleRecognition/RecognizedHoleSegment.h>  // Get the value of the property. Ptr<Vector3D> propertyValue = recognizedHoleSegment_var->axis(); ``` ```` |

## Property Value

This is a read only property whose value is a [Vector3D](Vector3D.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |