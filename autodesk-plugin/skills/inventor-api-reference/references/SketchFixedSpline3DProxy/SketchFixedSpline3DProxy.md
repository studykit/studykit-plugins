# SketchFixedSpline3DProxy Object

Derived from: [SketchFixedSpline3D](../SketchFixedSpline3D/SketchFixedSpline3D.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToSpline](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_ConvertToSpline.md) | Method that converts the fixed spline to a SketchSpline3D object. This method is currently only valid for SketchFixedSpline3D objects that were created using a BSplineCurve as input. |
| [Delete](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_Delete.md) | Method that deletes the sketch entity. |
| [Edit](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_Edit.md) | Method that edits a fixed sketch spline based on an input NURBS definition. This method is only valid for SketchFixedSpline3D objects that were created using a BSplineCurve as input. This method will fail if the curve was created with an Edge. |
| [EditByEdge](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_EditByEdge.md) | Method that edits the geometry of a fixed sketch spline based on an input transient Edge. |
| [GetReferenceKey](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Closed](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_Closed.md) | Boolean property that gets whether the curve is closed. A periodic curve is closed and curvature continuous at the closure. |
| [Constraints3D](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_Constraints3D.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Construction](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_Construction.md) | Gets / sets the Sketch3D Construction Property. |
| [ContainingOccurrence](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [EndSketchPoint](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_EndSketchPoint.md) | Property that returns the that defines the position of the end of the spline. |
| [Geometry](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_Geometry.md) | Gets and sets a BSplineCurve3d geometry object. The object returned represents a 'snapshot' view of the current state of the sketch fixed spline. |
| [HasReferenceComponent](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [IsDefinedByEdge](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_IsDefinedByEdge.md) | Property that indicates if this SketchFixedSpline3D object is defined by a BSplineCurve or was created using an Edge as \input. Returns True if it was created using an Edge. Returns False if it was created using a BSplineCurve. |
| [Length](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_Length.md) | Double property that returns the length of the entity in centimeters. |
| [NativeObject](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_OwnedBy.md) | Property indicating entity or entities that own this object. |
| [Parent](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Reference](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_Reference.md) | Gets and sets whether this entity is a reference entity or not. |
| [ReferenceComponent](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation. |
| [StartSketchPoint](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_StartSketchPoint.md) | Property that returns the that defines the position of the start of the spline. |
| [Type](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9
