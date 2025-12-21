# SketchEntity3D Object

## Description

The SketchEntity object is the base class for all geometric sketch entities. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchEntity3D/SketchEntity3D_Delete.md) | Method that deletes the sketch entity. |
| [GetReferenceKey](../SketchEntity3D/SketchEntity3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchEntity3D/SketchEntity3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchEntity3D/SketchEntity3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Constraints3D](../SketchEntity3D/SketchEntity3D_Constraints3D.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../SketchEntity3D/SketchEntity3D_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Construction](../SketchEntity3D/SketchEntity3D_Construction.md) | Gets / sets the Sketch3D Construction Property. |
| [HasReferenceComponent](../SketchEntity3D/SketchEntity3D_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [OwnedBy](../SketchEntity3D/SketchEntity3D_OwnedBy.md) | Property indicating entity or entities that own this object. |
| [Parent](../SketchEntity3D/SketchEntity3D_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchEntity3D/SketchEntity3D_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Reference](../SketchEntity3D/SketchEntity3D_Reference.md) | Gets and sets whether this entity is a reference entity or not. |
| [ReferenceComponent](../SketchEntity3D/SketchEntity3D_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchEntity3D/SketchEntity3D_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation. |
| [Type](../SketchEntity3D/SketchEntity3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CustomConstraint3D.Entity](../CustomConstraint3D/CustomConstraint3D_Entity.md), [CustomConstraint3DProxy.Entity](../CustomConstraint3DProxy/CustomConstraint3DProxy_Entity.md), [EqualConstraint3D.EntityOne](../EqualConstraint3D/EqualConstraint3D_EntityOne.md), [EqualConstraint3D.EntityTwo](../EqualConstraint3D/EqualConstraint3D_EntityTwo.md), [EqualConstraint3DProxy.EntityOne](../EqualConstraint3DProxy/EqualConstraint3DProxy_EntityOne.md), [EqualConstraint3DProxy.EntityTwo](../EqualConstraint3DProxy/EqualConstraint3DProxy_EntityTwo.md), [OnFaceConstraint3D.Entity](../OnFaceConstraint3D/OnFaceConstraint3D_Entity.md), [OnFaceConstraint3DProxy.Entity](../OnFaceConstraint3DProxy/OnFaceConstraint3DProxy_Entity.md), [ParallelToXYPlaneConstraint3D.Entity](../ParallelToXYPlaneConstraint3D/ParallelToXYPlaneConstraint3D_Entity.md), [ParallelToXYPlaneConstraint3DProxy.Entity](../ParallelToXYPlaneConstraint3DProxy/ParallelToXYPlaneConstraint3DProxy_Entity.md), [ParallelToXZPlaneConstraint3D.Entity](../ParallelToXZPlaneConstraint3D/ParallelToXZPlaneConstraint3D_Entity.md), [ParallelToXZPlaneConstraint3DProxy.Entity](../ParallelToXZPlaneConstraint3DProxy/ParallelToXZPlaneConstraint3DProxy_Entity.md), [ParallelToYZPlaneConstraint3D.Entity](../ParallelToYZPlaneConstraint3D/ParallelToYZPlaneConstraint3D_Entity.md), [ParallelToYZPlaneConstraint3DProxy.Entity](../ParallelToYZPlaneConstraint3DProxy/ParallelToYZPlaneConstraint3DProxy_Entity.md), [ProfileEntity3D.SketchEntity](../ProfileEntity3D/ProfileEntity3D_SketchEntity.md), [ProfileEntity3DProxy.SketchEntity](../ProfileEntity3DProxy/ProfileEntity3DProxy_SketchEntity.md), [RadiusDimConstraint3D.Entity](../RadiusDimConstraint3D/RadiusDimConstraint3D_Entity.md), [RadiusDimConstraint3DProxy.Entity](../RadiusDimConstraint3DProxy/RadiusDimConstraint3DProxy_Entity.md), [Sketch3D.Include](../Sketch3D/Sketch3D_Include.md), [Sketch3DProxy.Include](../Sketch3DProxy/Sketch3DProxy_Include.md), [SketchEntities3DEnumerator.Item](../SketchEntities3DEnumerator/SketchEntities3DEnumerator_Item.md), [SmoothConstraint3D.EntityOne](../SmoothConstraint3D/SmoothConstraint3D_EntityOne.md), [SmoothConstraint3D.EntityTwo](../SmoothConstraint3D/SmoothConstraint3D_EntityTwo.md), [SmoothConstraint3DProxy.EntityOne](../SmoothConstraint3DProxy/SmoothConstraint3DProxy_EntityOne.md), [SmoothConstraint3DProxy.EntityTwo](../SmoothConstraint3DProxy/SmoothConstraint3DProxy_EntityTwo.md), [TangentConstraint3D.EntityOne](../TangentConstraint3D/TangentConstraint3D_EntityOne.md), [TangentConstraint3D.EntityTwo](../TangentConstraint3D/TangentConstraint3D_EntityTwo.md), [TangentConstraint3DProxy.EntityOne](../TangentConstraint3DProxy/TangentConstraint3DProxy_EntityOne.md), [TangentConstraint3DProxy.EntityTwo](../TangentConstraint3DProxy/TangentConstraint3DProxy_EntityTwo.md)

## Derived Classes

[HelicalCurve](../HelicalCurve/HelicalCurve.md), [SketchArc3D](../SketchArc3D/SketchArc3D.md), [SketchCircle3D](../SketchCircle3D/SketchCircle3D.md), [SketchControlPointSpline3D](../SketchControlPointSpline3D/SketchControlPointSpline3D.md), [SketchEllipse3D](../SketchEllipse3D/SketchEllipse3D.md), [SketchEllipticalArc3D](../SketchEllipticalArc3D/SketchEllipticalArc3D.md), [SketchEquationCurve3D](../SketchEquationCurve3D/SketchEquationCurve3D.md), [SketchFixedSpline3D](../SketchFixedSpline3D/SketchFixedSpline3D.md), [SketchLine3D](../SketchLine3D/SketchLine3D.md), [SketchPoint3D](../SketchPoint3D/SketchPoint3D.md), [SketchSpline3D](../SketchSpline3D/SketchSpline3D.md)

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |