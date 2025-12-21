# SketchArc3D Object

Derived from: [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) Object

## Description

The SketchArc3D object represents an arc within a 3D sketch. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchArc3D/SketchArc3D_Delete.md) | Method that deletes the sketch entity. |
| [GetReferenceKey](../SketchArc3D/SketchArc3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchArc3D/SketchArc3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchArc3D/SketchArc3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CenterPoint](../SketchArc3D/SketchArc3D_CenterPoint.md) | Property that returns the center point of the arc. |
| [Constraints3D](../SketchArc3D/SketchArc3D_Constraints3D.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../SketchArc3D/SketchArc3D_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Construction](../SketchArc3D/SketchArc3D_Construction.md) | Gets / sets the Sketch3D Construction Property. |
| [CurvatureDisplay](../SketchArc3D/SketchArc3D_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the arc. |
| [EndSketchPoint](../SketchArc3D/SketchArc3D_EndSketchPoint.md) | Property that gets the that defines the position of the end of the arc. |
| [Geometry](../SketchArc3D/SketchArc3D_Geometry.md) | Gets and sets an Arc3d geometry object. The object returned represents a 'snapshot' view of the current state of the sketch arc. |
| [HasReferenceComponent](../SketchArc3D/SketchArc3D_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Length](../SketchArc3D/SketchArc3D_Length.md) | Double property that returns the length of the entity in centimeters. |
| [OwnedBy](../SketchArc3D/SketchArc3D_OwnedBy.md) | Property indicating entity or entities that own this object. |
| [Parent](../SketchArc3D/SketchArc3D_Parent.md) | Property that returns the parent sketch of the entity. |
| [Radius](../SketchArc3D/SketchArc3D_Radius.md) | Gets the Radius of the arc. |
| [RangeBox](../SketchArc3D/SketchArc3D_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Reference](../SketchArc3D/SketchArc3D_Reference.md) | Gets and sets whether this entity is a reference entity or not. |
| [ReferenceComponent](../SketchArc3D/SketchArc3D_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchArc3D/SketchArc3D_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation. |
| [StartAngle](../SketchArc3D/SketchArc3D_StartAngle.md) | Gets the StartAngle of the arc. |
| [StartSketchPoint](../SketchArc3D/SketchArc3D_StartSketchPoint.md) | Property that gets the that defines the position of the start of the arc. |
| [SweepAngle](../SketchArc3D/SketchArc3D_SweepAngle.md) | Gets the SweepAngle of the arc. |
| [Type](../SketchArc3D/SketchArc3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BendConstraint.Arc](../BendConstraint/BendConstraint_Arc.md), [BendConstraintProxy.Arc](../BendConstraintProxy/BendConstraintProxy_Arc.md), [SketchArc3DProxy.NativeObject](../SketchArc3DProxy/SketchArc3DProxy_NativeObject.md), [SketchArcs3D.AddAsBend](../SketchArcs3D/SketchArcs3D_AddAsBend.md), [SketchArcs3D.AddByCenterStartEndPoint](../SketchArcs3D/SketchArcs3D_AddByCenterStartEndPoint.md), [SketchArcs3D.AddByCenterStartSweepAngle](../SketchArcs3D/SketchArcs3D_AddByCenterStartSweepAngle.md), [SketchArcs3D.AddByThreePoints](../SketchArcs3D/SketchArcs3D_AddByThreePoints.md), [SketchArcs3D.Item](../SketchArcs3D/SketchArcs3D_Item.md)

## Derived Classes

[SketchArc3DProxy](../SketchArc3DProxy/SketchArc3DProxy.md)

## Version

Introduced in version 6
