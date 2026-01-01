# RecognizedPocket.sharedFaces Property

Parent Object: [RecognizedPocket](RecognizedPocket.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PocketRecognition/RecognizedPocket.h>

## Description

Returns all faces making up the pocket, which are shared with other pockets.

## Syntax

* [Python](#Python)
* [C++](#C++)

"recognizedPocket\_var" is a variable referencing a RecognizedPocket object. |

"recognizedPocket\_var" is a variable referencing a RecognizedPocket object. ```` ``` #include <Cam/PocketRecognition/RecognizedPocket.h>  // Get the value of the property. std::vector<Ptr<BRepFace>> propertyValue = recognizedPocket_var->sharedFaces(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [BRepFace](BRepFace.htm).

## Version

Introduced in version March 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |