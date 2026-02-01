# ArrangePlaneEnvelopeDefinition Object

Derived from: [ArrangeEnvelopeDefinition](ArrangeEnvelopeDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangePlaneEnvelopeDefinition.h>

## Description

The ArrangePlaneEnvelope object represents an arrange envelope defined by a construction plane. This defines the settings of the envelope and the EnvelopeResult provides access to the resulting envelope and its contents.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ArrangePlaneEnvelopeDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [envelopeSpacing](ArrangePlaneEnvelopeDefinition_envelopeSpacing.htm) | Returns the parameter that controls the offset distance between envelopes when there is more than one. You can modify the value by using the properties on the returned ModelParameter object. |
| [frameWidth](ArrangePlaneEnvelopeDefinition_frameWidth.htm) | Returns the parameter that controls the width of the envelope frame. This defines the offset distance of the objects from the edge of the frame. You can modify the value by using the properties on the returned ModelParameter object. |
| [isPartialArrangeAllowed](ArrangePlaneEnvelopeDefinition_isPartialArrangeAllowed.htm) | Gets and sets if a partial arrange is allowed for this envelope. |
| [isValid](ArrangePlaneEnvelopeDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [length](ArrangePlaneEnvelopeDefinition_length.htm) | Returns the parameter that controls the length of the envelope frame. This defines the You can modify the value by using the properties on the returned ModelParameter object. |
| [objectSpacing](ArrangePlaneEnvelopeDefinition_objectSpacing.htm) | Returns the parameter that controls the space between objects in the arrangement. You can modify the value by using the properties on the returned ModelParameter object. |
| [objectType](ArrangePlaneEnvelopeDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [originXOffset](ArrangePlaneEnvelopeDefinition_originXOffset.htm) | Returns the parameter that controls the X offset of the frame from the origin of the construction plane. You can modify the value by using the properties on the returned ModelParameter object. |
| [originYOffset](ArrangePlaneEnvelopeDefinition_originYOffset.htm) | Returns the parameter that controls the Y offset of the frame from the origin of the construction plane. You can modify the value by using the properties on the returned ModelParameter object. |
| [parentArrange](ArrangePlaneEnvelopeDefinition_parentArrange.htm) | Returns the parent ArrangeFeature this envelope is associated with. |
| [placementClearance](ArrangePlaneEnvelopeDefinition_placementClearance.htm) | Returns the parameter that controls the offset of the objects from the base plane of the arrangement (the "up" direction). You can modify the value by using the properties on the returned ModelParameter object. |
| [plane](ArrangePlaneEnvelopeDefinition_plane.htm) | Gets and sets the ConstructionPlane the envelope is defined on. |
| [quantity](ArrangePlaneEnvelopeDefinition_quantity.htm) | Returns the parameter that defines the number of envelopes that can be created. A value of -1 indicates that there is no limit. |
| [width](ArrangePlaneEnvelopeDefinition_width.htm) | Returns the parameter that controls the width of the envelope frame. This defines the You can modify the value by using the properties on the returned ModelParameter object. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |