# RecognizedHoleSegment.halfAngle Property

Parent Object: [RecognizedHoleSegment](RecognizedHoleSegment.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/HoleRecognition/RecognizedHoleSegment.h>

## Description

For hole segments of type Cone, returns the cone's half angle, i.e. the angle between the axis of the cone and its surface. Returns 0 for other segment types.

## Syntax

* [Python](#Python)
* [C++](#C++)

"recognizedHoleSegment\_var" is a variable referencing a RecognizedHoleSegment object. |

"recognizedHoleSegment\_var" is a variable referencing a RecognizedHoleSegment object. ```` ``` #include <Cam/HoleRecognition/RecognizedHoleSegment.h>  // Get the value of the property. double propertyValue = recognizedHoleSegment_var->halfAngle(); ``` ```` |

## Property Value

This is a read only property whose value is a double.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |