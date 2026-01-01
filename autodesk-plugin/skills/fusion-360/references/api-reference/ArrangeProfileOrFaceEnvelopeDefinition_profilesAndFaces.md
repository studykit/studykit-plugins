# ArrangeProfileOrFaceEnvelopeDefinition.profilesAndFaces Property

Parent Object: [ArrangeProfileOrFaceEnvelopeDefinition](ArrangeProfileOrFaceEnvelopeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeProfileOrFaceEnvelopeDefinition.h>

## Description

Gets and sets an array containing any combination of Profile and planar BRepFace objects. These objects define the shapes of the envelopes. Currently, if a Profile is used, it must be the only Profile in its parent sketch.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeProfileOrFaceEnvelopeDefinition\_var" is a variable referencing an ArrangeProfileOrFaceEnvelopeDefinition object. |

"arrangeProfileOrFaceEnvelopeDefinition\_var" is a variable referencing an ArrangeProfileOrFaceEnvelopeDefinition object. ```` ``` #include <Fusion/Arrange/ArrangeProfileOrFaceEnvelopeDefinition.h>  // Get the value of the property. std::vector<Ptr<Base>> propertyValue = arrangeProfileOrFaceEnvelopeDefinition_var->profilesAndFaces();  // Set the value of the property, where value_var is a Base. bool returnValue = arrangeProfileOrFaceEnvelopeDefinition_var->profilesAndFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [Base](Base.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |