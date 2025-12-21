# SketchSpline Object

Derived from: [SketchEntity](../SketchEntity/SketchEntity.md) Object

## Description

The SketchSpline object represents a spline within a sketch. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchSpline/SketchSpline_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetCustomLineType](../SketchSpline/SketchSpline_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetHandle](../SketchSpline/SketchSpline_GetHandle.md) | Method that returns the fit point handle at the given fit point. The method returns Nothing if the handle is not enabled at the input fit point. |
| [GetHandleStatus](../SketchSpline/SketchSpline_GetHandleStatus.md) | Method that returns whether the handle at a given fit point is enabled or disabled. |
| [GetReferenceKey](../SketchSpline/SketchSpline_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [InsertFitPoint](../SketchSpline/SketchSpline_InsertFitPoint.md) | Method that inserts a new fit point into the spline. |
| [SetCustomLineType](../SketchSpline/SketchSpline_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |
| [SetHandleStatus](../SketchSpline/SketchSpline_SetHandleStatus.md) | Method that sets whether the handle at a given fit point is enabled or disabled. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchSpline/SketchSpline_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchSpline/SketchSpline_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Closed](../SketchSpline/SketchSpline_Closed.md) | Specifies whether the curve is closed. Setting a curve to be closed will cause it to close and be periodic. |
| [Constraints](../SketchSpline/SketchSpline_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchSpline/SketchSpline_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchSpline/SketchSpline_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingSketchBlock](../SketchSpline/SketchSpline_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [CurvatureDisplay](../SketchSpline/SketchSpline_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the spline. |
| [DisabledActionTypes](../SketchSpline/SketchSpline_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [EndSketchPoint](../SketchSpline/SketchSpline_EndSketchPoint.md) | Property that gets the that defines the position of the end of the spline. |
| [FitMethod](../SketchSpline/SketchSpline_FitMethod.md) | Specifies the fit method for the spline. |
| [FitPoint](../SketchSpline/SketchSpline_FitPoint.md) | Property that returns the SketchPoint at the specified index. The indices correspond to the fit points in order from the start to the end of the spline. An Index of 1 returns the first SketchPoint. The FitPointCount property returns the total number of fits points for the spline. |
| [FitPointCount](../SketchSpline/SketchSpline_FitPointCount.md) | Property that returns the number of fit points for the spline. |
| [Geometry](../SketchSpline/SketchSpline_Geometry.md) | Property that returns a geometry object. The object returned represents a snapshot view of the current state of the sketch spline. |
| [Geometry3d](../SketchSpline/SketchSpline_Geometry3d.md) | Read-only property that returns the BSplineCurve geometry that represents this sketch spline in model space. |
| [HasReferenceComponent](../SketchSpline/SketchSpline_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Layer](../SketchSpline/SketchSpline_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [Length](../SketchSpline/SketchSpline_Length.md) | Double property that returns the length of the entity in centimeters. |
| [LineDefinitionSpace](../SketchSpline/SketchSpline_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this sketch spline. |
| [LineScale](../SketchSpline/SketchSpline_LineScale.md) | Gets and sets the LineScale applied to this sketch spline. |
| [LineType](../SketchSpline/SketchSpline_LineType.md) | Gets and sets the LineType applied to this sketch spline. |
| [LineWeight](../SketchSpline/SketchSpline_LineWeight.md) | Gets and sets the LineWeight applied to this sketch spline. |
| [OverrideColor](../SketchSpline/SketchSpline_OverrideColor.md) | Gets and sets the color applied to this sketch spline. |
| [OwnedBy](../SketchSpline/SketchSpline_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchSpline/SketchSpline_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchSpline/SketchSpline_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchSpline/SketchSpline_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchSpline/SketchSpline_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchSpline/SketchSpline_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchSpline/SketchSpline_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchSpline/SketchSpline_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [StartSketchPoint](../SketchSpline/SketchSpline_StartSketchPoint.md) | Property that returns the that defines the position of the start of the line. |
| [Tension](../SketchSpline/SketchSpline_Tension.md) | Gets and sets the tension for the spline. |
| [Type](../SketchSpline/SketchSpline_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[OffsetSplineDimConstraint.Spline](../OffsetSplineDimConstraint/OffsetSplineDimConstraint_Spline.md), [OffsetSplineDimConstraintProxy.Spline](../OffsetSplineDimConstraintProxy/OffsetSplineDimConstraintProxy_Spline.md), [SketchControlPointSpline.ConvertToSpline](../SketchControlPointSpline/SketchControlPointSpline_ConvertToSpline.md), [SketchControlPointSplineProxy.ConvertToSpline](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_ConvertToSpline.md), [SketchFixedSpline.ConvertToSpline](../SketchFixedSpline/SketchFixedSpline_ConvertToSpline.md), [SketchFixedSplineProxy.ConvertToSpline](../SketchFixedSplineProxy/SketchFixedSplineProxy_ConvertToSpline.md), [SketchOffsetSpline.ConvertToSpline](../SketchOffsetSpline/SketchOffsetSpline_ConvertToSpline.md), [SketchOffsetSpline.OriginalSpline](../SketchOffsetSpline/SketchOffsetSpline_OriginalSpline.md), [SketchOffsetSplineProxy.ConvertToSpline](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_ConvertToSpline.md), [SketchOffsetSplineProxy.OriginalSpline](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_OriginalSpline.md), [SketchSplineHandle.Spline](../SketchSplineHandle/SketchSplineHandle_Spline.md), [SketchSplineHandleProxy.Spline](../SketchSplineHandleProxy/SketchSplineHandleProxy_Spline.md), [SketchSplineProxy.NativeObject](../SketchSplineProxy/SketchSplineProxy_NativeObject.md), [SketchSplines.Add](../SketchSplines/SketchSplines_Add.md), [SketchSplines.Item](../SketchSplines/SketchSplines_Item.md), [SplineFitPointConstraint.Spline](../SplineFitPointConstraint/SplineFitPointConstraint_Spline.md), [SplineFitPointConstraintProxy.Spline](../SplineFitPointConstraintProxy/SplineFitPointConstraintProxy_Spline.md)

## Derived Classes

[SketchSplineProxy](../SketchSplineProxy/SketchSplineProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch Display Entities](../../sample-programs/SketchEntity_Sample.md) | This sample demonstrates the query functionality available for sketch entities. |
| [Spline - create NURBS](../../sample-programs/SketchFixedSpline_Sample.md) | This sample demonstrates the creation of a sketch spline using a geometry definition (a NURB). The API also supports creation of 3D sketch splines in a similar way. |
| [Sketch Spline](../../sample-programs/SketchSpline_Sample.md) | This sample demonstrates creating and manipulating a sketch spline. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |