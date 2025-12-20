# SketchPoint3D Object

Derived from: [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) Object

## Description

The SketchPoint3D object represents a point within a 3D sketch. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConnectTo](../SketchPoint3D/SketchPoint3D_ConnectTo.md) | Method that connects this sketch point to the input point. Valid inputs are SketchPoint3D, SketchPoint, Vertex or WorkPoint. This method is the UI equivalent of 'Add Coincident Constraint'. The point being constrained is the sketch point on which this method is called and the input point is the constraining point. This method will fail if a coincident constraint exists between this sketch point and a vertex; i.e. this sketch point must be underconstrained. |
| [Delete](../SketchPoint3D/SketchPoint3D_Delete.md) | Method that deletes the sketch entity. |
| [GetReferenceKey](../SketchPoint3D/SketchPoint3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [MoveBy](../SketchPoint3D/SketchPoint3D_MoveBy.md) | Method that moves the sketch point a delta distance from its current location. Movement of a sketch point is limited by the constraints currently defined on the sketch. If a sketch is partially constrained it will perform the move within the range allowed by the constraints. Because of this, the result of a move may not always be exactly what was specified. |
| [MoveTo](../SketchPoint3D/SketchPoint3D_MoveTo.md) | Method that moves the sketch point to an explicit x-y-z location. Movement of a sketch point is limited by the constraints currently defined on the sketch. If a sketch is partially constrained it will perform the move within the range allowed by the constraints. Because of this, the result of a move may not always be exactly what was specified. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchPoint3D/SketchPoint3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttachedEntities](../SketchPoint3D/SketchPoint3D_AttachedEntities.md) | Property that returns the collection of objects that are connected to this point. |
| [AttributeSets](../SketchPoint3D/SketchPoint3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Constraints3D](../SketchPoint3D/SketchPoint3D_Constraints3D.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../SketchPoint3D/SketchPoint3D_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Construction](../SketchPoint3D/SketchPoint3D_Construction.md) | Gets / sets the Sketch3D Construction Property. |
| [Geometry](../SketchPoint3D/SketchPoint3D_Geometry.md) | Gets and sets a Point geometry object. The object returned represents a 'snapshot' view of the current state of the sketch point. |
| [HasReferenceComponent](../SketchPoint3D/SketchPoint3D_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [HoleCenter](../SketchPoint3D/SketchPoint3D_HoleCenter.md) | Defines if the sketch point is being displayed as a hole center. |
| [OwnedBy](../SketchPoint3D/SketchPoint3D_OwnedBy.md) | Property indicating entity or entities that own this object. |
| [Parent](../SketchPoint3D/SketchPoint3D_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchPoint3D/SketchPoint3D_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Reference](../SketchPoint3D/SketchPoint3D_Reference.md) | Gets and sets whether this entity is a reference entity or not. |
| [ReferenceComponent](../SketchPoint3D/SketchPoint3D_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchPoint3D/SketchPoint3D_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation. |
| [Type](../SketchPoint3D/SketchPoint3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[MidpointConstraint3D.Point](../MidpointConstraint3D/MidpointConstraint3D_Point.md), [MidpointConstraint3DProxy.Point](../MidpointConstraint3DProxy/MidpointConstraint3DProxy_Point.md), [OnFaceCurve.EndSketchPoint](../OnFaceCurve/OnFaceCurve_EndSketchPoint.md), [OnFaceCurve.FitPoint](../OnFaceCurve/OnFaceCurve_FitPoint.md), [OnFaceCurve.StartSketchPoint](../OnFaceCurve/OnFaceCurve_StartSketchPoint.md), [OnFaceCurveProxy.EndSketchPoint](../OnFaceCurveProxy/OnFaceCurveProxy_EndSketchPoint.md), [OnFaceCurveProxy.FitPoint](../OnFaceCurveProxy/OnFaceCurveProxy_FitPoint.md), [OnFaceCurveProxy.StartSketchPoint](../OnFaceCurveProxy/OnFaceCurveProxy_StartSketchPoint.md), [PointAndPlaneDistanceDimConstraint3D.Point](../PointAndPlaneDistanceDimConstraint3D/PointAndPlaneDistanceDimConstraint3D_Point.md), [PointAndPlaneDistanceDimConstraint3DProxy.Point](../PointAndPlaneDistanceDimConstraint3DProxy/PointAndPlaneDistanceDimConstraint3DProxy_Point.md), [ProfileEntity3D.EndSketchPoint](../ProfileEntity3D/ProfileEntity3D_EndSketchPoint.md), [ProfileEntity3D.StartSketchPoint](../ProfileEntity3D/ProfileEntity3D_StartSketchPoint.md), [ProfileEntity3DProxy.EndSketchPoint](../ProfileEntity3DProxy/ProfileEntity3DProxy_EndSketchPoint.md), [ProfileEntity3DProxy.StartSketchPoint](../ProfileEntity3DProxy/ProfileEntity3DProxy_StartSketchPoint.md), [SketchArc3D.EndSketchPoint](../SketchArc3D/SketchArc3D_EndSketchPoint.md), [SketchArc3D.StartSketchPoint](../SketchArc3D/SketchArc3D_StartSketchPoint.md), [SketchArc3DProxy.EndSketchPoint](../SketchArc3DProxy/SketchArc3DProxy_EndSketchPoint.md), [SketchArc3DProxy.StartSketchPoint](../SketchArc3DProxy/SketchArc3DProxy_StartSketchPoint.md), [SketchControlPointSpline3D.ControlPoint](../SketchControlPointSpline3D/SketchControlPointSpline3D_ControlPoint.md), [SketchControlPointSpline3D.EndSketchPoint](../SketchControlPointSpline3D/SketchControlPointSpline3D_EndSketchPoint.md), [SketchControlPointSpline3D.StartSketchPoint](../SketchControlPointSpline3D/SketchControlPointSpline3D_StartSketchPoint.md), [SketchControlPointSpline3DProxy.ControlPoint](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_ControlPoint.md), [SketchControlPointSpline3DProxy.EndSketchPoint](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_EndSketchPoint.md), [SketchControlPointSpline3DProxy.StartSketchPoint](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_StartSketchPoint.md), [SketchEllipticalArc3D.EndSketchPoint](../SketchEllipticalArc3D/SketchEllipticalArc3D_EndSketchPoint.md), [SketchEllipticalArc3D.StartSketchPoint](../SketchEllipticalArc3D/SketchEllipticalArc3D_StartSketchPoint.md), [SketchEllipticalArc3DProxy.EndSketchPoint](../SketchEllipticalArc3DProxy/SketchEllipticalArc3DProxy_EndSketchPoint.md), [SketchEllipticalArc3DProxy.StartSketchPoint](../SketchEllipticalArc3DProxy/SketchEllipticalArc3DProxy_StartSketchPoint.md), [SketchEquationCurve3D.EndSketchPoint](../SketchEquationCurve3D/SketchEquationCurve3D_EndSketchPoint.md), [SketchEquationCurve3D.StartSketchPoint](../SketchEquationCurve3D/SketchEquationCurve3D_StartSketchPoint.md), [SketchEquationCurve3DProxy.EndSketchPoint](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_EndSketchPoint.md), [SketchEquationCurve3DProxy.StartSketchPoint](../SketchEquationCurve3DProxy/SketchEquationCurve3DProxy_StartSketchPoint.md), [SketchFixedSpline3D.EndSketchPoint](../SketchFixedSpline3D/SketchFixedSpline3D_EndSketchPoint.md), [SketchFixedSpline3D.StartSketchPoint](../SketchFixedSpline3D/SketchFixedSpline3D_StartSketchPoint.md), [SketchFixedSpline3DProxy.EndSketchPoint](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_EndSketchPoint.md), [SketchFixedSpline3DProxy.StartSketchPoint](../SketchFixedSpline3DProxy/SketchFixedSpline3DProxy_StartSketchPoint.md), [SketchLine3D.EndSketchPoint](../SketchLine3D/SketchLine3D_EndSketchPoint.md), [SketchLine3D.StartSketchPoint](../SketchLine3D/SketchLine3D_StartSketchPoint.md), [SketchLine3DProxy.EndSketchPoint](../SketchLine3DProxy/SketchLine3DProxy_EndSketchPoint.md), [SketchLine3DProxy.StartSketchPoint](../SketchLine3DProxy/SketchLine3DProxy_StartSketchPoint.md), [SketchPoint3DProxy.NativeObject](../SketchPoint3DProxy/SketchPoint3DProxy_NativeObject.md), [SketchPoints3D.Add](../SketchPoints3D/SketchPoints3D_Add.md), [SketchPoints3D.Item](../SketchPoints3D/SketchPoints3D_Item.md), [SketchSpline3D.EndSketchPoint](../SketchSpline3D/SketchSpline3D_EndSketchPoint.md), [SketchSpline3D.FitPoint](../SketchSpline3D/SketchSpline3D_FitPoint.md), [SketchSpline3D.InsertFitPoint](../SketchSpline3D/SketchSpline3D_InsertFitPoint.md), [SketchSpline3D.StartSketchPoint](../SketchSpline3D/SketchSpline3D_StartSketchPoint.md), [SketchSpline3DProxy.EndSketchPoint](../SketchSpline3DProxy/SketchSpline3DProxy_EndSketchPoint.md), [SketchSpline3DProxy.FitPoint](../SketchSpline3DProxy/SketchSpline3DProxy_FitPoint.md), [SketchSpline3DProxy.InsertFitPoint](../SketchSpline3DProxy/SketchSpline3DProxy_InsertFitPoint.md), [SketchSpline3DProxy.StartSketchPoint](../SketchSpline3DProxy/SketchSpline3DProxy_StartSketchPoint.md), [SketchSplineHandle3D.EndSketchPoint](../SketchSplineHandle3D/SketchSplineHandle3D_EndSketchPoint.md), [SketchSplineHandle3D.FitPoint](../SketchSplineHandle3D/SketchSplineHandle3D_FitPoint.md), [SketchSplineHandle3D.StartSketchPoint](../SketchSplineHandle3D/SketchSplineHandle3D_StartSketchPoint.md), [SketchSplineHandle3DProxy.EndSketchPoint](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_EndSketchPoint.md), [SketchSplineHandle3DProxy.FitPoint](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_FitPoint.md), [SketchSplineHandle3DProxy.StartSketchPoint](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_StartSketchPoint.md)

## Derived Classes

[SketchPoint3DProxy](../SketchPoint3DProxy/SketchPoint3DProxy.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |