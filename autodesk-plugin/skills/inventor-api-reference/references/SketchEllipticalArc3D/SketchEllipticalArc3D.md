# SketchEllipticalArc3D Object

Derived from: [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) Object

## Description

The SketchEllipticalArc3D object represents an elliptical arc within a 3D sketch. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchEllipticalArc3D/SketchEllipticalArc3D_Delete.md) | Method that deletes the sketch entity. |
| [GetReferenceKey](../SketchEllipticalArc3D/SketchEllipticalArc3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchEllipticalArc3D/SketchEllipticalArc3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchEllipticalArc3D/SketchEllipticalArc3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CenterPoint](../SketchEllipticalArc3D/SketchEllipticalArc3D_CenterPoint.md) | Property that returns the center point of the elliptical arc. |
| [Constraints3D](../SketchEllipticalArc3D/SketchEllipticalArc3D_Constraints3D.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../SketchEllipticalArc3D/SketchEllipticalArc3D_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Construction](../SketchEllipticalArc3D/SketchEllipticalArc3D_Construction.md) | Gets / sets the Sketch3D Construction Property. |
| [CurvatureDisplay](../SketchEllipticalArc3D/SketchEllipticalArc3D_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the elliptical arc. |
| [EndSketchPoint](../SketchEllipticalArc3D/SketchEllipticalArc3D_EndSketchPoint.md) | Property that gets the that defines the position of the end of the elliptical arc. |
| [Geometry](../SketchEllipticalArc3D/SketchEllipticalArc3D_Geometry.md) | Gets and sets an EllipticalArc geometry object. The object returned represents a 'snapshot' view of the current state of the sketch ellipse. |
| [HasReferenceComponent](../SketchEllipticalArc3D/SketchEllipticalArc3D_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Length](../SketchEllipticalArc3D/SketchEllipticalArc3D_Length.md) | Double property that returns the length of the entity in centimeters. |
| [MajorAxisVector](../SketchEllipticalArc3D/SketchEllipticalArc3D_MajorAxisVector.md) | Gets the MajorAxisVector of the elliptical arc. |
| [MajorRadius](../SketchEllipticalArc3D/SketchEllipticalArc3D_MajorRadius.md) | Gets the MajorRadius of the elliptical arc. |
| [MinorRadius](../SketchEllipticalArc3D/SketchEllipticalArc3D_MinorRadius.md) | Gets the MinorRadius of the elliptical arc. |
| [OwnedBy](../SketchEllipticalArc3D/SketchEllipticalArc3D_OwnedBy.md) | Property indicating entity or entities that own this object. |
| [Parent](../SketchEllipticalArc3D/SketchEllipticalArc3D_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchEllipticalArc3D/SketchEllipticalArc3D_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Reference](../SketchEllipticalArc3D/SketchEllipticalArc3D_Reference.md) | Gets and sets whether this entity is a reference entity or not. |
| [ReferenceComponent](../SketchEllipticalArc3D/SketchEllipticalArc3D_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchEllipticalArc3D/SketchEllipticalArc3D_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation. |
| [StartAngle](../SketchEllipticalArc3D/SketchEllipticalArc3D_StartAngle.md) | Gets the StartAngle of the elliptical arc. |
| [StartSketchPoint](../SketchEllipticalArc3D/SketchEllipticalArc3D_StartSketchPoint.md) | Property that returns the that defines the position of the start of the elliptical arc. |
| [SweepAngle](../SketchEllipticalArc3D/SketchEllipticalArc3D_SweepAngle.md) | Gets the SweepAngle of the elliptical arc. |
| [Type](../SketchEllipticalArc3D/SketchEllipticalArc3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SketchEllipticalArc3DProxy.NativeObject](../SketchEllipticalArc3DProxy/SketchEllipticalArc3DProxy_NativeObject.md), [SketchEllipticalArcs3D.Item](../SketchEllipticalArcs3D/SketchEllipticalArcs3D_Item.md)

## Derived Classes

[SketchEllipticalArc3DProxy](../SketchEllipticalArc3DProxy/SketchEllipticalArc3DProxy.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |