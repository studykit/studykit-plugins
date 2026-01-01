# Arrange2DProfileOrFaceEnvelopeInput.profilesOrFaces Property

Parent Object: [Arrange2DProfileOrFaceEnvelopeInput](Arrange2DProfileOrFaceEnvelopeInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange2DProfileOrFaceEnvelopeInput.h>

## Description

Gets and sets an array that contains a combination of Profile and planar BRepFace objects that will be used to define the shape of the envelopes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange2DProfileOrFaceEnvelopeInput\_var" is a variable referencing an Arrange2DProfileOrFaceEnvelopeInput object. |

"arrange2DProfileOrFaceEnvelopeInput\_var" is a variable referencing an Arrange2DProfileOrFaceEnvelopeInput object. ```` ``` #include <Fusion/Arrange/Arrange2DProfileOrFaceEnvelopeInput.h>  // Get the value of the property. std::vector<Ptr<Base>> propertyValue = arrange2DProfileOrFaceEnvelopeInput_var->profilesOrFaces();  // Set the value of the property, where value_var is a Base. bool returnValue = arrange2DProfileOrFaceEnvelopeInput_var->profilesOrFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [Base](Base.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |