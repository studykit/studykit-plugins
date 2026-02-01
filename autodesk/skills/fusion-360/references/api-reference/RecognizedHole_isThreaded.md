# RecognizedHole.isThreaded Property

Parent Object: [RecognizedHole](RecognizedHole.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/HoleRecognition/RecognizedHole.h>

## Description

Returns true if at least one segment of this hole is threaded, i.e. associated with a thread feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"recognizedHole\_var" is a variable referencing a RecognizedHole object. |

"recognizedHole\_var" is a variable referencing a RecognizedHole object. ```` ``` #include <Cam/HoleRecognition/RecognizedHole.h>  // Get the value of the property. boolean propertyValue = recognizedHole_var->isThreaded(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |