# ArrangeFeatureInput.setPlaneEnvelope Method

Parent Object: [ArrangeFeatureInput](ArrangeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeatureInput.h>

## Description

Defines an envelope input defined by a plane for the arrange feature. Only a single envelope input can exist at a time. Calling this method will cause any existing envelope object input that has been created for this input to be invalid.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeatureInput\_var" is a variable referencing an [ArrangeFeatureInput](ArrangeFeatureInput.htm) object.```` ``` returnValue = arrangeFeatureInput_var.setPlaneEnvelope(plane, length, width) ``` ```` |

"arrangeFeatureInput\_var" is a variable referencing an [ArrangeFeatureInput](ArrangeFeatureInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Arrange2DPlaneEnvelopeInput](Arrange2DPlaneEnvelopeInput.htm) | Returns the created Arrange2DPlaneEnvelopeInput object or null if the creation fails. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| plane | [ConstructionPlane](ConstructionPlane.htm) | The Construction plane the envelope will be on. |
| length | [ValueInput](ValueInput.htm) | The length of the envelope. This is the size of the envelope as measured along the X axis of the specified construction plane.   This value will become a parameter when the arrangement is created. If the ValueInput is created using a real number it is in centimeters. If you use a string, it is evaluated the same as a value would be in the command dialog and uses the current document units. For example, if the document units are inch and you specific "0.25" it will result in 1/4 inch clearance. Using a string, you can also specify the units as part of the expression, such as "0.25 in + 2 mm". And you can define equations like "PartSize + 2 mm" where "PartSize" is an existing parameter. |
| width | [ValueInput](ValueInput.htm) | The width of the envelope. This is the size of the envelope as measured along the Y axis of the specified construction plane.   This value will become a parameter when the arrangement is created. If the ValueInput is created using a real number it is in centimeters. If you use a string, it is evaluated the same as a value would be in the command dialog and uses the current document units. For example, if the document units are inch and you specific "0.25" it will result in 1/4 inch clearance. Using a string, you can also specify the units as part of the expression, such as "0.25 in + 2 mm". And you can define equations like "PartSize + 2 mm" where "PartSize" is an existing parameter. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |