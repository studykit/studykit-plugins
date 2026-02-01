# RecognizedHoleSegment.threadFeatures Property

Parent Object: [RecognizedHoleSegment](RecognizedHoleSegment.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/HoleRecognition/RecognizedHoleSegment.h>

## Description

Returns the thread features associated with this segment, or null if none exist for this segment.

## Syntax

* [Python](#Python)
* [C++](#C++)

"recognizedHoleSegment\_var" is a variable referencing a RecognizedHoleSegment object. |

"recognizedHoleSegment\_var" is a variable referencing a RecognizedHoleSegment object. ```` ``` #include <Cam/HoleRecognition/RecognizedHoleSegment.h>  // Get the value of the property. std::vector<Ptr<ThreadFeature>> propertyValue = recognizedHoleSegment_var->threadFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [ThreadFeature](ThreadFeature.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |