# SketchArc3DProxy Object

Derived from: [SketchArc3D](../SketchArc3D/SketchArc3D.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchArc3DProxy/SketchArc3DProxy_Delete.md) | Method that deletes the sketch entity. |
| [GetReferenceKey](../SketchArc3DProxy/SketchArc3DProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchArc3DProxy/SketchArc3DProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchArc3DProxy/SketchArc3DProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CenterPoint](../SketchArc3DProxy/SketchArc3DProxy_CenterPoint.md) | Property that returns the center point of the arc. |
| [Constraints3D](../SketchArc3DProxy/SketchArc3DProxy_Constraints3D.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../SketchArc3DProxy/SketchArc3DProxy_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Construction](../SketchArc3DProxy/SketchArc3DProxy_Construction.md) | Gets / sets the Sketch3D Construction Property. |
| [ContainingOccurrence](../SketchArc3DProxy/SketchArc3DProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [CurvatureDisplay](../SketchArc3DProxy/SketchArc3DProxy_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the arc. |
| [EndSketchPoint](../SketchArc3DProxy/SketchArc3DProxy_EndSketchPoint.md) | Property that gets the that defines the position of the end of the arc. |
| [Geometry](../SketchArc3DProxy/SketchArc3DProxy_Geometry.md) | Gets and sets an Arc3d geometry object. The object returned represents a 'snapshot' view of the current state of the sketch arc. |
| [HasReferenceComponent](../SketchArc3DProxy/SketchArc3DProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Length](../SketchArc3DProxy/SketchArc3DProxy_Length.md) | Double property that returns the length of the entity in centimeters. |
| [NativeObject](../SketchArc3DProxy/SketchArc3DProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../SketchArc3DProxy/SketchArc3DProxy_OwnedBy.md) | Property indicating entity or entities that own this object. |
| [Parent](../SketchArc3DProxy/SketchArc3DProxy_Parent.md) | Property that returns the parent sketch of the entity. |
| [Radius](../SketchArc3DProxy/SketchArc3DProxy_Radius.md) | Gets the Radius of the arc. |
| [RangeBox](../SketchArc3DProxy/SketchArc3DProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Reference](../SketchArc3DProxy/SketchArc3DProxy_Reference.md) | Gets and sets whether this entity is a reference entity or not. |
| [ReferenceComponent](../SketchArc3DProxy/SketchArc3DProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchArc3DProxy/SketchArc3DProxy_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation. |
| [StartAngle](../SketchArc3DProxy/SketchArc3DProxy_StartAngle.md) | Gets the StartAngle of the arc. |
| [StartSketchPoint](../SketchArc3DProxy/SketchArc3DProxy_StartSketchPoint.md) | Property that gets the that defines the position of the start of the arc. |
| [SweepAngle](../SketchArc3DProxy/SketchArc3DProxy_SweepAngle.md) | Gets the SweepAngle of the arc. |
| [Type](../SketchArc3DProxy/SketchArc3DProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6
