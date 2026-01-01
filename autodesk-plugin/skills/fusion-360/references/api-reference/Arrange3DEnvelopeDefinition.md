# Arrange3DEnvelopeDefinition Object

Derived from: [ArrangeEnvelopeDefinition](ArrangeEnvelopeDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange3DEnvelopeDefinition.h>

## Description

The Arrange3DEnvelope object represents an 3D arrange envelope.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Arrange3DEnvelopeDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ceilingClearance](Arrange3DEnvelopeDefinition_ceilingClearance.htm) | Returns the parameter that controls the clearance of the objects from the top of the envelope volume. You can modify the value by using the properties on the returned ModelParameter object. |
| [frameWidth](Arrange3DEnvelopeDefinition_frameWidth.htm) | Returns the parameter that controls the width of the envelope frame. This defines the offset distance of the objects from the edge of the frame. You can modify the value by using the properties on the returned ModelParameter object. |
| [height](Arrange3DEnvelopeDefinition_height.htm) | Returns the parameter that controls the height of the envelope volume. This defines the You can modify the value by using the properties on the returned ModelParameter object. |
| [isPartialArrangeAllowed](Arrange3DEnvelopeDefinition_isPartialArrangeAllowed.htm) | Gets and sets if a partial arrange is allowed for this envelope. |
| [isValid](Arrange3DEnvelopeDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [length](Arrange3DEnvelopeDefinition_length.htm) | Returns the parameter that controls the length of the envelope volume. This defines the You can modify the value by using the properties on the returned ModelParameter object. |
| [objectSpacing](Arrange3DEnvelopeDefinition_objectSpacing.htm) | Returns the parameter that controls the space between objects in the arrangement. You can modify the value by using the properties on the returned ModelParameter object. |
| [objectType](Arrange3DEnvelopeDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [originXOffset](Arrange3DEnvelopeDefinition_originXOffset.htm) | Returns the parameter that controls the X offset of the envelope volume from the origin of the construction plane. You can modify the value by using the properties on the returned ModelParameter object. |
| [originYOffset](Arrange3DEnvelopeDefinition_originYOffset.htm) | Returns the parameter that controls the Y offset of the envelope volume from the origin of the construction plane. You can modify the value by using the properties on the returned ModelParameter object. |
| [parentArrange](Arrange3DEnvelopeDefinition_parentArrange.htm) | Returns the parent ArrangeFeature this envelope is associated with. |
| [placementClearance](Arrange3DEnvelopeDefinition_placementClearance.htm) | Returns the parameter that controls the offset of the objects from the base plane of the arrangement (the "up" direction). You can modify the value by using the properties on the returned ModelParameter object. |
| [plane](Arrange3DEnvelopeDefinition_plane.htm) | Gets and sets the ConstructionPlane the envelope is defined on. |
| [width](Arrange3DEnvelopeDefinition_width.htm) | Returns the parameter that controls the width of the envelope volume. This defines the You can modify the value by using the properties on the returned ModelParameter object. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |