# CadContours2dParameterValue Object

Derived from: [ParameterValue](ParameterValue.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CadContours2dParameterValue.h>

## Description

A parameter value that is a CadContours2dParameterValue. The user needs to set the parameter anew via the API after a model update or after the CurveSelections returned by getCurveSelections() has been edited.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [applyCurveSelections](CadContours2dParameterValue_applyCurveSelections.htm) | Set the values of the parameter as a collection of CadCurves. If the input does not define continuous contours, the contour is amended and calculated, but only if used on Operations, not OperationInputs When used with OperationInputs, the contours are calculated when creating an operation out of the input. |
| [classType](CadContours2dParameterValue_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [getCurveSelections](CadContours2dParameterValue_getCurveSelections.htm) | Get the values of the parameter as a collection of CadCurves, which might consist of chains, pockets, silhouettes and face countours. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](CadContours2dParameterValue_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CadContours2dParameterValue_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parent](CadContours2dParameterValue_parent.htm) | Get the parameter object that the value is associated with. |

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