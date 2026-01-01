# PocketSelection.inputGeometry Property

Parent Object: [PocketSelection](PocketSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/PocketSelection.h>

## Description

Get or set the value of the input geometry. If the value originates from a component instead of an occurrence, or an occurrence outside of the CAM environment, then the subpath is checked against the CAM model tree. For some child classes, this may be the same as the value property, but might also consist of fewer elements. Valid elements depend on the capabilities of the derived class. An exception is thrown if the matching fails or the given entity does not match the expected type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pocketSelection\_var" is a variable referencing a PocketSelection object. |

"pocketSelection\_var" is a variable referencing a PocketSelection object. ```` ``` #include <Cam/GeometrySelections/PocketSelection.h>  // Get the value of the property. std::vector<Ptr<Base>> propertyValue = pocketSelection_var->inputGeometry();  // Set the value of the property, where value_var is a Base. bool returnValue = pocketSelection_var->inputGeometry(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [Base](Base.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Hole and Pocket Recognition API Sample](HoleAndPocketRecognition_Sample.htm) | This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.  The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.  RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.  The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.  This script works only if the Manufacturing Extension is active. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |