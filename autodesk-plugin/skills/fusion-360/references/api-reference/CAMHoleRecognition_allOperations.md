# CAMHoleRecognition.allOperations Property

Parent Object: [CAMHoleRecognition](CAMHoleRecognition.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMHoleRecognition.h>

## Description

Returns an array containing all of the operations in this hole recognition. This includes all operations nested in folders and patterns.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMHoleRecognition\_var" is a variable referencing a CAMHoleRecognition object. |

"cAMHoleRecognition\_var" is a variable referencing a CAMHoleRecognition object. ```` ``` #include <Cam/CAM/CAMHoleRecognition.h>  // Get the value of the property. std::vector<Ptr<OperationBase>> propertyValue = cAMHoleRecognition_var->allOperations(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [OperationBase](OperationBase.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |