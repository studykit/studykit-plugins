# SketchSplineHandle3DProxy Object

Derived from: [SketchSplineHandle3D](../SketchSplineHandle3D/SketchSplineHandle3D.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_Delete.md) | Method that deletes the sketch entity. |
| [GetReferenceKey](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Constraints3D](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_Constraints3D.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Construction](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_Construction.md) | Gets / sets the Sketch3D Construction Property. |
| [ContainingOccurrence](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [EndSketchPoint](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_EndSketchPoint.md) | Property that returns the that defines the position of the end of the line. |
| [FitPoint](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_FitPoint.md) | Property that returns the fit point associated with the handle. |
| [Geometry](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_Geometry.md) | Gets and sets a LineSegment geometry object. The object returned represents a 'snapshot' view of the current state of the sketch line. |
| [HasReferenceComponent](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Length](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_Length.md) | Double property that returns the length of the entity in centimeters. |
| [NativeObject](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_OwnedBy.md) | Property indicating entity or entities that own this object. |
| [Parent](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Reference](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_Reference.md) | Gets and sets whether this entity is a reference entity or not. |
| [ReferenceComponent](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation. |
| [Spline](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_Spline.md) | Property that returns the spline associated with the handle. |
| [StartSketchPoint](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_StartSketchPoint.md) | Property that returns the that defines the position of the start of the line. |
| [Tangent](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_Tangent.md) | Gets and sets the tangent vector at the fit point associated with this handle. |
| [Type](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Weight](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_Weight.md) | Gets and sets the tangent weight at the fit point associated with this handle. |

## Version

Introduced in version 2008
