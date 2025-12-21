# SketchCircle3D Object

Derived from: [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) Object

## Description

The SketchCircle3D object represents a circle within a 3D sketch. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchCircle3D/SketchCircle3D_Delete.md) | Method that deletes the sketch entity. |
| [GetReferenceKey](../SketchCircle3D/SketchCircle3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchCircle3D/SketchCircle3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Area](../SketchCircle3D/SketchCircle3D_Area.md) | Double property that returns the area of the entity in square centimeters. |
| [AttributeSets](../SketchCircle3D/SketchCircle3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CenterPoint](../SketchCircle3D/SketchCircle3D_CenterPoint.md) | Property that returns the point that defines the position of the center of the circle. |
| [Constraints3D](../SketchCircle3D/SketchCircle3D_Constraints3D.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../SketchCircle3D/SketchCircle3D_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Construction](../SketchCircle3D/SketchCircle3D_Construction.md) | Gets / sets the Sketch3D Construction Property. |
| [CurvatureDisplay](../SketchCircle3D/SketchCircle3D_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the circle. |
| [Geometry](../SketchCircle3D/SketchCircle3D_Geometry.md) | Gets and sets a Circle geometry object. The object returned represents a 'snapshot' view of the current state of the sketch circle. |
| [HasReferenceComponent](../SketchCircle3D/SketchCircle3D_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Length](../SketchCircle3D/SketchCircle3D_Length.md) | Gets the Length of the circle. |
| [OwnedBy](../SketchCircle3D/SketchCircle3D_OwnedBy.md) | Property indicating entity or entities that own this object. |
| [Parent](../SketchCircle3D/SketchCircle3D_Parent.md) | Property that returns the parent sketch of the entity. |
| [Radius](../SketchCircle3D/SketchCircle3D_Radius.md) | Gets the Radius of the circle. |
| [RangeBox](../SketchCircle3D/SketchCircle3D_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Reference](../SketchCircle3D/SketchCircle3D_Reference.md) | Gets and sets whether this entity is a reference entity or not. |
| [ReferenceComponent](../SketchCircle3D/SketchCircle3D_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchCircle3D/SketchCircle3D_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation. |
| [Type](../SketchCircle3D/SketchCircle3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SketchCircle3DProxy.NativeObject](../SketchCircle3DProxy/SketchCircle3DProxy_NativeObject.md), [SketchCircles3D.AddByCenterRadius](../SketchCircles3D/SketchCircles3D_AddByCenterRadius.md), [SketchCircles3D.AddByThreePoints](../SketchCircles3D/SketchCircles3D_AddByThreePoints.md), [SketchCircles3D.Item](../SketchCircles3D/SketchCircles3D_Item.md)

## Derived Classes

[SketchCircle3DProxy](../SketchCircle3DProxy/SketchCircle3DProxy.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |