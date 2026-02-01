# ArrangeEnvelopeDefinition Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeEnvelopeDefinition.h>

## Description

The ArrangeEnvelope object is the base class for the different types of arrangement envelopes and provides access to the information that defines the envelope(s). This defines the settings of the envelope and the EnvelopeResult provides access to the resulting envelope and its contents.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ArrangeEnvelopeDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [frameWidth](ArrangeEnvelopeDefinition_frameWidth.htm) | Returns the parameter that controls the width of the envelope frame. This defines the offset distance of the objects from the edge of the frame. You can modify the value by using the properties on the returned ModelParameter object. |
| [isPartialArrangeAllowed](ArrangeEnvelopeDefinition_isPartialArrangeAllowed.htm) | Gets and sets if a partial arrange is allowed for this envelope. |
| [isValid](ArrangeEnvelopeDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectSpacing](ArrangeEnvelopeDefinition_objectSpacing.htm) | Returns the parameter that controls the space between objects in the arrangement. You can modify the value by using the properties on the returned ModelParameter object. |
| [objectType](ArrangeEnvelopeDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentArrange](ArrangeEnvelopeDefinition_parentArrange.htm) | Returns the parent ArrangeFeature this envelope is associated with. |
| [placementClearance](ArrangeEnvelopeDefinition_placementClearance.htm) | Returns the parameter that controls the offset of the objects from the base plane of the arrangement (the "up" direction). You can modify the value by using the properties on the returned ModelParameter object. |

## Accessed From

[Arrange3DResultEnvelope.envelopeDefinition](Arrange3DResultEnvelope_envelopeDefinition.htm), [ArrangeFeature.envelopeDefinition](ArrangeFeature_envelopeDefinition.htm), [ArrangePlaneResultEnvelope.envelopeDefinition](ArrangePlaneResultEnvelope_envelopeDefinition.htm), [ArrangeProfileOrFaceResultEnvelope.envelopeDefinition](ArrangeProfileOrFaceResultEnvelope_envelopeDefinition.htm), [ArrangeResultEnvelope.envelopeDefinition](ArrangeResultEnvelope_envelopeDefinition.htm)

## Derived Classes

[Arrange3DEnvelopeDefinition](Arrange3DEnvelopeDefinition.htm), [ArrangePlaneEnvelopeDefinition](ArrangePlaneEnvelopeDefinition.htm), [ArrangeProfileOrFaceEnvelopeDefinition](ArrangeProfileOrFaceEnvelopeDefinition.htm)

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |