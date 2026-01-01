# RecognizedHole.bottom Property

Parent Object: [RecognizedHole](RecognizedHole.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/HoleRecognition/RecognizedHole.h>

## Description

Returns a point at the center of the hole bottom.

## Syntax

* [Python](#Python)
* [C++](#C++)

"recognizedHole\_var" is a variable referencing a RecognizedHole object. |

"recognizedHole\_var" is a variable referencing a RecognizedHole object. ```` ``` #include <Cam/HoleRecognition/RecognizedHole.h>  // Get the value of the property. Ptr<Point3D> propertyValue = recognizedHole_var->bottom(); ``` ```` |

## Property Value

This is a read only property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |