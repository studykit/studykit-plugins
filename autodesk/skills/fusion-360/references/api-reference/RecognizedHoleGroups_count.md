# RecognizedHoleGroups.count Property

Parent Object: [RecognizedHoleGroups](RecognizedHoleGroups.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/HoleRecognition/RecognizedHoleGroups.h>

## Description

Returns the number of hole groups contained in this hole group collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"recognizedHoleGroups\_var" is a variable referencing a RecognizedHoleGroups object. |

"recognizedHoleGroups\_var" is a variable referencing a RecognizedHoleGroups object. ```` ``` #include <Cam/HoleRecognition/RecognizedHoleGroups.h>  // Get the value of the property. uinteger propertyValue = recognizedHoleGroups_var->count(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

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