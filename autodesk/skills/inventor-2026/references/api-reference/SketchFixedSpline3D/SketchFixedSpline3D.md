# SketchFixedSpline3D Object

Derived from: [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) Object

## Description

The SketchFixedSpline3D object represents a fixed spline within a sketch. These splines are created using the geometry definition (BSplineCurve). See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToSpline](../SketchFixedSpline3D/SketchFixedSpline3D_ConvertToSpline.md) | Method that converts the fixed spline to a SketchSpline3D object. This method is currently only valid for SketchFixedSpline3D objects that were created using a BSplineCurve as input. |
| [Delete](../SketchFixedSpline3D/SketchFixedSpline3D_Delete.md) | Method that deletes the sketch entity. |
| [Edit](../SketchFixedSpline3D/SketchFixedSpline3D_Edit.md) | Method that edits a fixed sketch spline based on an input NURBS definition. This method is only valid for SketchFixedSpline3D objects that were created using a BSplineCurve as input. This method will fail if the curve was created with an Edge. |
| [EditByEdge](../SketchFixedSpline3D/SketchFixedSpline3D_EditByEdge.md) | Method that edits the geometry of a fixed sketch spline based on an input transient Edge. |
| [GetReferenceKey](../SketchFixedSpline3D/SketchFixedSpline3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchFixedSpline3D/SketchFixedSpline3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchFixedSpline3D/SketchFixedSpline3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Closed](../SketchFixedSpline3D/SketchFixedSpline3D_Closed.md) | Boolean property that gets whether the curve is closed. A periodic curve is closed and curvature continuous at the closure. |
| [Constraints3D](../SketchFixedSpline3D/SketchFixedSpline3D_Constraints3D.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../SketchFixedSpline3D/SketchFixedSpline3D_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Construction](../SketchFixedSpline3D/SketchFixedSpline3D_Construction.md) | Gets / sets the Sketch3D Construction Property. |
| [EndSketchPoint](../SketchFixedSpline3D/SketchFixedSpline3D_EndSketchPoint.md) | Property that returns the that defines the position of the end of the spline. |
| [Geometry](../SketchFixedSpline3D/SketchFixedSpline3D_Geometry.md) | Gets and sets a BSplineCurve3d geometry object. The object returned represents a 'snapshot' view of the current state of the sketch fixed spline. |
| [HasReferenceComponent](../SketchFixedSpline3D/SketchFixedSpline3D_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [IsDefinedByEdge](../SketchFixedSpline3D/SketchFixedSpline3D_IsDefinedByEdge.md) | Property that indicates if this SketchFixedSpline3D object is defined by a BSplineCurve or was created using an Edge as \input. Returns True if it was created using an Edge. Returns False if it was created using a BSplineCurve. |
| [Length](../SketchFixedSpline3D/SketchFixedSpline3D_Length.md) | Double property that returns the length of the entity in centimeters. |
| [OwnedBy](../SketchFixedSpline3D/SketchFixedSpline3D_OwnedBy.md) | Property indicating entity or entities that own this object. |
| [Parent](../SketchFixedSpline3D/SketchFixedSpline3D_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchFixedSpline3D/SketchFixedSpline3D_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Reference](../SketchFixedSpline3D/SketchFixedSpline3D_Reference.md) | Gets and sets whether this entity is a reference entity or not. |
| [ReferenceComponent](../SketchFixedSpline3D/SketchFixedSpline3D_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchFixedSpline3D/SketchFixedSpline3D_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation. |
| [StartSketchPoint](../SketchFixedSpline3D/SketchFixedSpline3D_StartSketchPoint.md) | Property that returns the that defines the position of the start of the spline. |
| [Type](../SketchFixedSpline3D/SketchFixedSpline3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SketchFixedSpline3DProxy.NativeObject](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_NativeObject.md), [SketchFixedSplines3D.Add](../SketchFixedSplines3D/SketchFixedSplines3D_Add.md), [SketchFixedSplines3D.AddByEdge](../SketchFixedSplines3D/SketchFixedSplines3D_AddByEdge.md), [SketchFixedSplines3D.Item](../SketchFixedSplines3D/SketchFixedSplines3D_Item.md)

## Derived Classes

[SketchFixedSpline3DProxy](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy.md)

## Version

Introduced in version 9
