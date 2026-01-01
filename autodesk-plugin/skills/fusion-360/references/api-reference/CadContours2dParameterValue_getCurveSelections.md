# CadContours2dParameterValue.getCurveSelections Method

Parent Object: [CadContours2dParameterValue](CadContours2dParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CadContours2dParameterValue.h>

## Description

Get the values of the parameter as a collection of CadCurves, which might consist of chains, pockets, silhouettes and face countours.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cadContours2dParameterValue\_var" is a variable referencing a [CadContours2dParameterValue](CadContours2dParameterValue.htm) object.```` ``` returnValue = cadContours2dParameterValue_var.getCurveSelections() ``` ```` |

"cadContours2dParameterValue\_var" is a variable referencing a [CadContours2dParameterValue](CadContours2dParameterValue.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CurveSelections](CurveSelections.htm) | Returns current CurveSelections of the value. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Hole and Pocket Recognition API Sample](HoleAndPocketRecognition_Sample.htm) | This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.  The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.  RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.  The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.  This script works only if the Manufacturing Extension is active. |
| [Manufacturing Workflow API Sample](ManufacturingWorkflowAPISample_Sample.htm) | Manufacturing Workflow API Sample This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |
| [Wood Routing Workflow Sample](WoodRoutingSample_Sample.htm) | This script demonstrates routing wood panels. When running the sample, it assumes you have an open design containing one or more "panels" oriented flat in the X-Y plane. The script creates a setup and a 2D contour operation with tabs to route the panels from a standard sheet. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |