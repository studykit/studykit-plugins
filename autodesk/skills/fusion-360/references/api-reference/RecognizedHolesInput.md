# RecognizedHolesInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/HoleRecognition/RecognizedHolesInput.h>

## Description

Object that contains the settings used by recognizedHoles and recognizedHoleGroups.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](RecognizedHolesInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](RecognizedHolesInput_create.htm) | Creates an empty input object to be passed into recognizedHoles or recognizedHoleGroups |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [filterPartialHoles](RecognizedHolesInput_filterPartialHoles.htm) | Partial holes will not be included in recognized holes when set to true. Holes that intersect edges are considered partial holes. If a hole has multiple segments, such as a counterbore hole, all the segments inside the hole must intersect an edge for the hole to be considered a partial hole. |
| [isValid](RecognizedHolesInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](RecognizedHolesInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[RecognizedHolesInput.create](RecognizedHolesInput_create.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Setups From Hole Recognition API Sample](CreateSetupsFromHoleRecognition_Sample.htm) | This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.  The Fusion Manufacturing Extension is required for Hole Recognition.  The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |