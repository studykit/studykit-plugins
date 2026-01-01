# SketchSpline3DProxy Object

Derived from: [SketchSpline3D](../SketchSpline3D/SketchSpline3D.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchSpline3DProxy/SketchSpline3DProxy_Delete.md) | Method that deletes the sketch entity. |
| [Disconnect](../SketchSpline3DProxy/SketchSpline3DProxy_Disconnect.md) | Method that removes an existing fit point from the spline. This method can have the effect of deleting the sketch point if it is not associated with any other sketch entity. |
| [GetHandle](../SketchSpline3DProxy/SketchSpline3DProxy_GetHandle.md) | Method that returns the fit point handle at the given fit point. The method returns Nothing if the handle is not enabled at the input fit point. |
| [GetHandleStatus](../SketchSpline3DProxy/SketchSpline3DProxy_GetHandleStatus.md) | Method that returns whether the handle at a given fit point is enabled or disabled. |
| [GetReferenceKey](../SketchSpline3DProxy/SketchSpline3DProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [InsertFitPoint](../SketchSpline3DProxy/SketchSpline3DProxy_InsertFitPoint.md) | Method that inserts a new fit point into the spline and returns the inserted fit point. |
| [SetHandleStatus](../SketchSpline3DProxy/SketchSpline3DProxy_SetHandleStatus.md) | Method that sets whether the handle at a given fit point is enabled or disabled. |
| [Split](../SketchSpline3DProxy/SketchSpline3DProxy_Split.md) | Method that splits the spline at the specified location. After the split, the original object (the one on which this method was called) represents the part of the spline associated with the original start point. The SketchSpline3D object returned by this method represents the part of the spline associated with the original end point. The curvature of the final result may differ from the original spline. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchSpline3DProxy/SketchSpline3DProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchSpline3DProxy/SketchSpline3DProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Closed](../SketchSpline3DProxy/SketchSpline3DProxy_Closed.md) | Specifies whether the curve is closed. Setting a curve to be closed will cause it to close and be periodic. |
| [Constraints3D](../SketchSpline3DProxy/SketchSpline3DProxy_Constraints3D.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../SketchSpline3DProxy/SketchSpline3DProxy_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Construction](../SketchSpline3DProxy/SketchSpline3DProxy_Construction.md) | Gets / sets the Sketch3D Construction Property. |
| [ContainingOccurrence](../SketchSpline3DProxy/SketchSpline3DProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [CurvatureDisplay](../SketchSpline3DProxy/SketchSpline3DProxy_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the spline. |
| [EndSketchPoint](../SketchSpline3DProxy/SketchSpline3DProxy_EndSketchPoint.md) | Property that gets the that defines the position of the end of the spline. |
| [EndTangentScale](../SketchSpline3DProxy/SketchSpline3DProxy_EndTangentScale.md) | Gets and sets the tangent scale parameter at the end point of the spline. |
| [FitMethod](../SketchSpline3DProxy/SketchSpline3DProxy_FitMethod.md) | Specifies the fit method for the spline. |
| [FitPoint](../SketchSpline3DProxy/SketchSpline3DProxy_FitPoint.md) | Property that returns the at the specified index. The indices correspond to the fit points in order from the start to the end of the spline. An Index of 1 returns the first SketchPoint3D. The FitPointCount property returns the total number of fit points for the spline. |
| [FitPointCount](../SketchSpline3DProxy/SketchSpline3DProxy_FitPointCount.md) | Property that returns the number of fit points for the spline. |
| [Geometry](../SketchSpline3DProxy/SketchSpline3DProxy_Geometry.md) | Gets and sets a BSplineCurve geometry object. The object returned represents a 'snapshot' view of the current state of the sketch spline. |
| [HasReferenceComponent](../SketchSpline3DProxy/SketchSpline3DProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Length](../SketchSpline3DProxy/SketchSpline3DProxy_Length.md) | Double property that returns the length of the entity in centimeters. |
| [NativeObject](../SketchSpline3DProxy/SketchSpline3DProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../SketchSpline3DProxy/SketchSpline3DProxy_OwnedBy.md) | Property indicating entity or entities that own this object. |
| [Parent](../SketchSpline3DProxy/SketchSpline3DProxy_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchSpline3DProxy/SketchSpline3DProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Reference](../SketchSpline3DProxy/SketchSpline3DProxy_Reference.md) | Gets and sets whether this entity is a reference entity or not. |
| [ReferenceComponent](../SketchSpline3DProxy/SketchSpline3DProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchSpline3DProxy/SketchSpline3DProxy_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation. |
| [StartSketchPoint](../SketchSpline3DProxy/SketchSpline3DProxy_StartSketchPoint.md) | Property that returns the that defines the position of the start of the spline. |
| [StartTangentScale](../SketchSpline3DProxy/SketchSpline3DProxy_StartTangentScale.md) | Gets and sets the tangent scale parameter at the start point of the spline. |
| [Tension](../SketchSpline3DProxy/SketchSpline3DProxy_Tension.md) | Gets and sets the tension for the spline. |
| [Type](../SketchSpline3DProxy/SketchSpline3DProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6
