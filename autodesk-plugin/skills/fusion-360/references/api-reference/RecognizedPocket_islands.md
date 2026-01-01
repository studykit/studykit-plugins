# RecognizedPocket.islands Property

Parent Object: [RecognizedPocket](RecognizedPocket.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PocketRecognition/RecognizedPocket.h>

## Description

Returns each island inside this pocket as a separate ProfileLoop object (in cm).

## Syntax

* [Python](#Python)
* [C++](#C++)

"recognizedPocket\_var" is a variable referencing a RecognizedPocket object. |

"recognizedPocket\_var" is a variable referencing a RecognizedPocket object. ```` ``` #include <Cam/PocketRecognition/RecognizedPocket.h>  // Get the value of the property. std::vector<Ptr<Curve3DPath>> propertyValue = recognizedPocket_var->islands(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [Curve3DPath](Curve3DPath.htm).

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |