# SketchLine3D Object

Derived from: [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) Object

## Description

The SketchLine3D object represents a line within a 3D sketch. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchLine3D/SketchLine3D_Delete.md) | Method that deletes the sketch entity. |
| [GetReferenceKey](../SketchLine3D/SketchLine3D_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchLine3D/SketchLine3D_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchLine3D/SketchLine3D_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Constraints3D](../SketchLine3D/SketchLine3D_Constraints3D.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of geometric and bend constraints. |
| [ConstraintStatus](../SketchLine3D/SketchLine3D_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [Construction](../SketchLine3D/SketchLine3D_Construction.md) | Gets / sets the Sketch3D Construction Property. |
| [EndSketchPoint](../SketchLine3D/SketchLine3D_EndSketchPoint.md) | Property that returns the that defines the position of the end of the line. |
| [Geometry](../SketchLine3D/SketchLine3D_Geometry.md) | Gets and sets a LineSegment geometry object. The object returned represents a 'snapshot' view of the current state of the sketch line. |
| [HasReferenceComponent](../SketchLine3D/SketchLine3D_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Length](../SketchLine3D/SketchLine3D_Length.md) | Double property that returns the length of the entity in centimeters. |
| [OwnedBy](../SketchLine3D/SketchLine3D_OwnedBy.md) | Property indicating entity or entities that own this object. |
| [Parent](../SketchLine3D/SketchLine3D_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchLine3D/SketchLine3D_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Reference](../SketchLine3D/SketchLine3D_Reference.md) | Gets and sets whether this entity is a reference entity or not. |
| [ReferenceComponent](../SketchLine3D/SketchLine3D_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchLine3D/SketchLine3D_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. This property returns the model entity the sketch entity is dependent on. The Reference property indicates whether the sketch entity is driven by a model entity or not. If the sketch entity is not referencing a model entity, this property will return Nothing. This property can also return nothing even when the sketch entity is referencing a model entity in the case where the model entity has been consumed by some subsequent modeling operation. |
| [StartSketchPoint](../SketchLine3D/SketchLine3D_StartSketchPoint.md) | Property that returns the that defines the position of the start of the line. |
| [Type](../SketchLine3D/SketchLine3D_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BendConstraint.LineOne](../BendConstraint/BendConstraint_LineOne.md), [BendConstraint.LineTwo](../BendConstraint/BendConstraint_LineTwo.md), [BendConstraintProxy.LineOne](../BendConstraintProxy/BendConstraintProxy_LineOne.md), [BendConstraintProxy.LineTwo](../BendConstraintProxy/BendConstraintProxy_LineTwo.md), [LineLengthDimConstraint3D.Line](../LineLengthDimConstraint3D/LineLengthDimConstraint3D_Line.md), [LineLengthDimConstraint3DProxy.Line](../LineLengthDimConstraint3DProxy/LineLengthDimConstraint3DProxy_Line.md), [MidpointConstraint3D.Line](../MidpointConstraint3D/MidpointConstraint3D_Line.md), [MidpointConstraint3DProxy.Line](../MidpointConstraint3DProxy/MidpointConstraint3DProxy_Line.md), [ParallelToXAxisConstraint3D.Line](../ParallelToXAxisConstraint3D/ParallelToXAxisConstraint3D_Line.md), [ParallelToXAxisConstraint3DProxy.Line](../ParallelToXAxisConstraint3DProxy/ParallelToXAxisConstraint3DProxy_Line.md), [ParallelToYAxisConstraint3D.Line](../ParallelToYAxisConstraint3D/ParallelToYAxisConstraint3D_Line.md), [ParallelToYAxisConstraint3DProxy.Line](../ParallelToYAxisConstraint3DProxy/ParallelToYAxisConstraint3DProxy_Line.md), [ParallelToZAxisConstraint3D.Line](../ParallelToZAxisConstraint3D/ParallelToZAxisConstraint3D_Line.md), [ParallelToZAxisConstraint3DProxy.Line](../ParallelToZAxisConstraint3DProxy/ParallelToZAxisConstraint3DProxy_Line.md), [SketchControlPointSpline3D.ControlPolygonSide](../SketchControlPointSpline3D/SketchControlPointSpline3D_ControlPolygonSide.md), [SketchControlPointSpline3DProxy.ControlPolygonSide](../SketchControlPointSpline3DProxy/SketchControlPointSpline3DProxy_ControlPolygonSide.md), [SketchLine3DProxy.NativeObject](../SketchLine3DProxy/SketchLine3DProxy_NativeObject.md), [SketchLines3D.AddByTwoPoints](../SketchLines3D/SketchLines3D_AddByTwoPoints.md), [SketchLines3D.Item](../SketchLines3D/SketchLines3D_Item.md), [TwoLineAngleDimConstraint3D.LineOne](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D_LineOne.md), [TwoLineAngleDimConstraint3D.LineTwo](../TwoLineAngleDimConstraint3D/TwoLineAngleDimConstraint3D_LineTwo.md), [TwoLineAngleDimConstraint3DProxy.LineOne](../TwoLineAngleDimConstraint3DProxy/TwoLineAngleDimConstraint3DProxy_LineOne.md), [TwoLineAngleDimConstraint3DProxy.LineTwo](../TwoLineAngleDimConstraint3DProxy/TwoLineAngleDimConstraint3DProxy_LineTwo.md)

## Derived Classes

[SketchLine3DProxy](../SketchLine3DProxy/SketchLine3DProxy.md), [SketchSplineHandle3D](../SketchSplineHandle3D/SketchSplineHandle3D.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a 3D sketch dimension](../../sample-programs/DimensionConstraints3D_AddTwoPointDistance_Sample.md) | This sample demonstrates the creation of a 3d sketch line and a dimension between the start and the end points of the line. |
| [Loft Feature With Non-Planar Section](../../sample-programs/LoftFeature_Sample.md) | This sample demonstrates the creation of a loft feature. It uses two sections for the loft, one is from a 2d sketch and the other is a non-planar section from a 3d sketch. Because one of the sketches isn't planar, a surface is created instead of a solid. |

## Version

Introduced in version 6
