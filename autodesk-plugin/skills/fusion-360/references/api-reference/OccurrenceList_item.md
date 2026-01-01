# OccurrenceList.item Method

Parent Object: [OccurrenceList](OccurrenceList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/OccurrenceList.h>

## Description

Returns the specified occurrence using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrenceList\_var" is a variable referencing an [OccurrenceList](OccurrenceList.htm) object.```` ``` returnValue = occurrenceList_var.item(index) ``` ```` |

"occurrenceList\_var" is a variable referencing an [OccurrenceList](OccurrenceList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Occurrence](Occurrence.htm) | Returns the specified occurrence or null in the case of an invalid index. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the occurrence within the collection to return. The first item has an index of 0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Assembly traversal using recursion API Sample](AssemblyTraversalUsingRecursion_Sample.htm) | Traverses the entire structure of the currently open assemlby using a recursive function and displays the result in a message box. This will match the occurrence structure seen in the browser. |
| [Create Setups From Hole Recognition API Sample](CreateSetupsFromHoleRecognition_Sample.htm) | This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.  The Fusion Manufacturing Extension is required for Hole Recognition.  The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector. |
| [Get Volume of Active Design API Sample](GetsVolumeOfActiveDesign_Sample.htm) | Traverses through the active design and totals the volume of every body within the design. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |