# SketchControlPointSpline3DProxy Object

Derived from: [SketchControlPointSpline3D](../SketchControlPointSpline3D/SketchControlPointSpline3D.md) Object

## Description

The proxy representation of a SketchControlPointSpline3D object. This represents a part SketchControlPointSpline3D object within an assembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToSpline](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_ConvertToSpline.md) | Method that inserts a new control point into the existing control point spline. |
| [Delete](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_Delete.md) | Method that deletes the sketch entity. |
| [GetReferenceKey](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [InsertKnot](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_InsertKnot.md) | Method that inserts a knot into the existing control point spline. The effect of this will be that the shape of the curve is maintained, but the control polygon will change shape and one additional point will be added. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Constraints3D](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_Constraints3D.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Construction](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_Construction.md) | Gets / sets the Sketch3D Construction Property. |
| [ContainingOccurrence](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ControlPoint](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_ControlPoint.md) | Read-only property that returns the SketchPoint3D at the specified index. The indices correspond to the control points in order from the start to the end of the spline. The ControlPointCount property returns the total number of control points for the spline. Deleting the returned sketch point will delete the control point from the spline. |
| [ControlPointCount](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_ControlPointCount.md) | Read-only property that returns the number of control points defining the control point spline. |
| [ControlPolygonSide](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_ControlPolygonSide.md) | Read-only property that returns the SketchLine3D object that represents a side of the control polygon. The indices correspond to the control polygon edges in order from the start to the end of the spline. |
| [CurvatureDisplay](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the spline. |
| [EndSketchPoint](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_EndSketchPoint.md) | Read-only property that returns the sketch point that defines the position of the end of the spline. |
| [Geometry](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_Geometry.md) | Read-only property that gets a BSplineCurve2d geometry object. The object returned represents a 'snapshot' view of the current state of the spline. |
| [HasReferenceComponent](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [IsClosed](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_IsClosed.md) | Read-only property that returns whether the curve is closed. |
| [Length](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_Length.md) | Gets the length of the entity in centimeters. |
| [NativeObject](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_OwnedBy.md) | Property indicating entity or entities that own this object. |
| [Parent](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Reference](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_Reference.md) | Gets and sets whether this entity is a reference entity or not. |
| [ReferenceComponent](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation. |
| [StartSketchPoint](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_StartSketchPoint.md) | Returns the sketch point that defines the position of the start of the spline. |
| [Type](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |