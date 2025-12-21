# SketchSpline3D Object

Derived from: [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) Object

## Description

The SketchSpline3D object represents a spline within a 3D sketch. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchSpline3D/SketchSpline3D_Delete.md) | Method that deletes the sketch entity. |
| [Disconnect](../SketchSpline3D/SketchSpline3D_Disconnect.md) | Method that removes an existing fit point from the spline. This method can have the effect of deleting the sketch point if it is not associated with any other sketch entity. |
| [GetHandle](../SketchSpline3D/SketchSpline3D_GetHandle.md) | Method that returns the fit point handle at the given fit point. The method returns Nothing if the handle is not enabled at the input fit point. |
| [GetHandleStatus](../SketchSpline3D/SketchSpline3D_GetHandleStatus.md) | Method that returns whether the handle at a given fit point is enabled or disabled. |
| [GetReferenceKey](../SketchSpline3D/SketchSpline3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [InsertFitPoint](../SketchSpline3D/SketchSpline3D_InsertFitPoint.md) | Method that inserts a new fit point into the spline and returns the inserted fit point. |
| [SetHandleStatus](../SketchSpline3D/SketchSpline3D_SetHandleStatus.md) | Method that sets whether the handle at a given fit point is enabled or disabled. |
| [Split](../SketchSpline3D/SketchSpline3D_Split.md) | Method that splits the spline at the specified location. After the split, the original object (the one on which this method was called) represents the part of the spline associated with the original start point. The SketchSpline3D object returned by this method represents the part of the spline associated with the original end point. The curvature of the final result may differ from the original spline. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchSpline3D/SketchSpline3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchSpline3D/SketchSpline3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Closed](../SketchSpline3D/SketchSpline3D_Closed.md) | Specifies whether the curve is closed. Setting a curve to be closed will cause it to close and be periodic. |
| [Constraints3D](../SketchSpline3D/SketchSpline3D_Constraints3D.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../SketchSpline3D/SketchSpline3D_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Construction](../SketchSpline3D/SketchSpline3D_Construction.md) | Gets / sets the Sketch3D Construction Property. |
| [CurvatureDisplay](../SketchSpline3D/SketchSpline3D_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the spline. |
| [EndSketchPoint](../SketchSpline3D/SketchSpline3D_EndSketchPoint.md) | Property that gets the that defines the position of the end of the spline. |
| [EndTangentScale](../SketchSpline3D/SketchSpline3D_EndTangentScale.md) | Gets and sets the tangent scale parameter at the end point of the spline. |
| [FitMethod](../SketchSpline3D/SketchSpline3D_FitMethod.md) | Specifies the fit method for the spline. |
| [FitPoint](../SketchSpline3D/SketchSpline3D_FitPoint.md) | Property that returns the at the specified index. The indices correspond to the fit points in order from the start to the end of the spline. An Index of 1 returns the first SketchPoint3D. The FitPointCount property returns the total number of fit points for the spline. |
| [FitPointCount](../SketchSpline3D/SketchSpline3D_FitPointCount.md) | Property that returns the number of fit points for the spline. |
| [Geometry](../SketchSpline3D/SketchSpline3D_Geometry.md) | Gets and sets a BSplineCurve geometry object. The object returned represents a 'snapshot' view of the current state of the sketch spline. |
| [HasReferenceComponent](../SketchSpline3D/SketchSpline3D_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Length](../SketchSpline3D/SketchSpline3D_Length.md) | Double property that returns the length of the entity in centimeters. |
| [OwnedBy](../SketchSpline3D/SketchSpline3D_OwnedBy.md) | Property indicating entity or entities that own this object. |
| [Parent](../SketchSpline3D/SketchSpline3D_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchSpline3D/SketchSpline3D_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Reference](../SketchSpline3D/SketchSpline3D_Reference.md) | Gets and sets whether this entity is a reference entity or not. |
| [ReferenceComponent](../SketchSpline3D/SketchSpline3D_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchSpline3D/SketchSpline3D_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation. |
| [StartSketchPoint](../SketchSpline3D/SketchSpline3D_StartSketchPoint.md) | Property that returns the that defines the position of the start of the spline. |
| [StartTangentScale](../SketchSpline3D/SketchSpline3D_StartTangentScale.md) | Gets and sets the tangent scale parameter at the start point of the spline. |
| [Tension](../SketchSpline3D/SketchSpline3D_Tension.md) | Gets and sets the tension for the spline. |
| [Type](../SketchSpline3D/SketchSpline3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SketchControlPointSpline3D.ConvertToSpline](../SketchControlPointSpline3D/SketchControlPointSpline3D_ConvertToSpline.md), [SketchControlPointSpline3DProxy.ConvertToSpline](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_ConvertToSpline.md), [SketchFixedSpline3D.ConvertToSpline](../SketchFixedSpline3D/SketchFixedSpline3D_ConvertToSpline.md), [SketchFixedSpline3DProxy.ConvertToSpline](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_ConvertToSpline.md), [SketchSpline3D.Split](../SketchSpline3D/SketchSpline3D_Split.md), [SketchSpline3DProxy.NativeObject](../SketchSpline3DProxy/SketchSpline3DProxy_NativeObject.md), [SketchSpline3DProxy.Split](../SketchSpline3DProxy/SketchSpline3DProxy_Split.md), [SketchSplineHandle3D.Spline](../SketchSplineHandle3D/SketchSplineHandle3D_Spline.md), [SketchSplineHandle3DProxy.Spline](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_Spline.md), [SketchSplines3D.Add](../SketchSplines3D/SketchSplines3D_Add.md), [SketchSplines3D.Item](../SketchSplines3D/SketchSplines3D_Item.md), [SplineLengthDimConstraint3D.Spline](../SplineLengthDimConstraint3D/SplineLengthDimConstraint3D_Spline.md), [SplineLengthDimConstraint3DProxy.Spline](../SplineLengthDimConstraint3DProxy/SplineLengthDimConstraint3DProxy_Spline.md)

## Derived Classes

[SketchSpline3DProxy](../SketchSpline3DProxy/SketchSpline3DProxy.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |