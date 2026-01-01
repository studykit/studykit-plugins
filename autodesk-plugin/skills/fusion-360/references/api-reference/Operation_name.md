# Operation.name Property

Parent Object: [Operation](Operation.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/Operation.h>

## Description

Gets and sets the name of the operation as seen in the browser. This name is unique as compared to the names of all other operations in the document.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operation\_var" is a variable referencing an Operation object. |

"operation\_var" is a variable referencing an Operation object. ```` ``` #include <Cam/Operations/Operation.h>  // Get the value of the property. string propertyValue = operation_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = operation_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Setups From Hole Recognition API Sample](CreateSetupsFromHoleRecognition_Sample.htm) | This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.  The Fusion Manufacturing Extension is required for Hole Recognition.  The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector. |
| [Create CAM Operation From Template API Sample](New_Operation_Sample_Sample.htm) | Demonstrates adding a new toolpath into the document using an existing CAM template. You can view the template [here](../ExtraFiles/face.f3dhsm-template), although it will be loaded automatically. Run the sample script within any Fusion project containing at least one setup. A new facing operation will be created at the end of each setup discovered. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |