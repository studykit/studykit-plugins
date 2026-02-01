# CurveSelections.createNewChainSelection Method

Parent Object: [CurveSelections](CurveSelections.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/CurveSelections.h>

## Description

Creates a new chain selection and adds it to the end of the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveSelections\_var" is a variable referencing a [CurveSelections](CurveSelections.htm) object.```` ``` returnValue = curveSelections_var.createNewChainSelection() ``` ```` |

"curveSelections\_var" is a variable referencing a [CurveSelections](CurveSelections.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ChainSelection](ChainSelection.htm) | Returns newly created ChainSelection. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Hole and Pocket Recognition API Sample](HoleAndPocketRecognition_Sample.htm) | This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.  The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.  RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.  The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.  This script works only if the Manufacturing Extension is active. |
| [Manufacturing Workflow API Sample](ManufacturingWorkflowAPISample_Sample.htm) | Manufacturing Workflow API Sample This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |