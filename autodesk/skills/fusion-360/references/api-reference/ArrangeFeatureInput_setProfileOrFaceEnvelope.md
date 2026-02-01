# ArrangeFeatureInput.setProfileOrFaceEnvelope Method

Parent Object: [ArrangeFeatureInput](ArrangeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeatureInput.h>

## Description

Defines an envelope defined by one or more profiles or planar faces. Only a single envelope input can exist at time. Calling this method will cause any existing envelope input object to be invalid.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeatureInput\_var" is a variable referencing an [ArrangeFeatureInput](ArrangeFeatureInput.htm) object.```` ``` returnValue = arrangeFeatureInput_var.setProfileOrFaceEnvelope(profilesOrFaces) ``` ```` |

"arrangeFeatureInput\_var" is a variable referencing an [ArrangeFeatureInput](ArrangeFeatureInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Arrange2DProfileOrFaceEnvelopeInput](Arrange2DProfileOrFaceEnvelopeInput.htm) | Returns the created Arrange2DProfileOrFaceEnvelopeInput object or null if the creation fails. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| profilesOrFaces | Base[] | An array of Profile and planar BRepFace objects that define the shape of the available envelopes. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |