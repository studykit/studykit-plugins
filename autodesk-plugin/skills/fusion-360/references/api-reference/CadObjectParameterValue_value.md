# CadObjectParameterValue.value Property

Parent Object: [CadObjectParameterValue](CadObjectParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CadObjectParameterValue.h>

## Description

Get or set the value of the parameter. If the value originates from a component instead of an occurrence, or an occurrence outside of the CAM environment, then the subpath is checked against the CAM model tree. An exception is thrown if the matching fails or the given entity does not match the expected type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cadObjectParameterValue\_var" is a variable referencing a CadObjectParameterValue object. |

"cadObjectParameterValue\_var" is a variable referencing a CadObjectParameterValue object. ```` ``` #include <Cam/Operations/CadObjectParameterValue.h>  // Get the value of the property. std::vector<Ptr<Base>> propertyValue = cadObjectParameterValue_var->value();  // Set the value of the property, where value_var is a Base. bool returnValue = cadObjectParameterValue_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [Base](Base.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Setups From Hole Recognition API Sample](CreateSetupsFromHoleRecognition_Sample.htm) | This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.  The Fusion Manufacturing Extension is required for Hole Recognition.  The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector. |
| [Hole and Pocket Recognition API Sample](HoleAndPocketRecognition_Sample.htm) | This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.  The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.  RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.  The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.  This script works only if the Manufacturing Extension is active. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |