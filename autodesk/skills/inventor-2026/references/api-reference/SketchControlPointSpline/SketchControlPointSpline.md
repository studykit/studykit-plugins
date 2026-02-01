# SketchControlPointSpline Object

Derived from: [SketchEntity](../SketchEntity/SketchEntity.md) Object

## Description

The SketchControlPointSpline object represents a control point spline within a sketch. These splines are created by defining the vertices of a control polygon of a NURBS curve. The properties and methods listed below are in addition to those supported by the SketchEntity object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToSpline](../SketchControlPointSpline/SketchControlPointSpline_ConvertToSpline.md) | Method that inserts a new control point into the existing control point spline. |
| [Delete](../SketchControlPointSpline/SketchControlPointSpline_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetCustomLineType](../SketchControlPointSpline/SketchControlPointSpline_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../SketchControlPointSpline/SketchControlPointSpline_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [InsertKnot](../SketchControlPointSpline/SketchControlPointSpline_InsertKnot.md) | Method that inserts a knot into the existing control point spline. The effect of this will be that the shape of the curve is maintained, but the control polygon will change shape and one additional point will be added. |
| [SetCustomLineType](../SketchControlPointSpline/SketchControlPointSpline_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchControlPointSpline/SketchControlPointSpline_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchControlPointSpline/SketchControlPointSpline_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Constraints](../SketchControlPointSpline/SketchControlPointSpline_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchControlPointSpline/SketchControlPointSpline_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchControlPointSpline/SketchControlPointSpline_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingSketchBlock](../SketchControlPointSpline/SketchControlPointSpline_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [ControlPoint](../SketchControlPointSpline/SketchControlPointSpline_ControlPoint.md) | Read-only property that returns the SketchPoint at the specified index. The indices correspond to the control points in order from the start to the end of the spline. An Index of 1 returns the first SketchPoint. The ControlPointCount property returns the total number of control points for the spline. Deleting the returned sketch point will delete the control point from the spline. |
| [ControlPointCount](../SketchControlPointSpline/SketchControlPointSpline_ControlPointCount.md) | Read-only property that returns the number of control points defining the control point spline. |
| [ControlPolygonSide](../SketchControlPointSpline/SketchControlPointSpline_ControlPolygonSide.md) | Read-only property that returns the SketchLine that represents a side of the control polygon. The indices correspond to the control polygon edges in order from the start to the end of the spline. An Index of 1 returns the first edge, with the last side being ControlPointCount -1 since there is one less side than number of control points. |
| [CurvatureDisplay](../SketchControlPointSpline/SketchControlPointSpline_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the spline. |
| [DisabledActionTypes](../SketchControlPointSpline/SketchControlPointSpline_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [EndSketchPoint](../SketchControlPointSpline/SketchControlPointSpline_EndSketchPoint.md) | Read-only property that returns the sketch point that defines the position of the end of the spline. |
| [Geometry](../SketchControlPointSpline/SketchControlPointSpline_Geometry.md) | Read-only property that returns a BSplineCurve2d geometry object. The object returned represents a 'snapshot' view of the current state of the spline. |
| [Geometry3d](../SketchControlPointSpline/SketchControlPointSpline_Geometry3d.md) | Read-only property that returns b-spline geometry that represents this spline in model space. |
| [HasReferenceComponent](../SketchControlPointSpline/SketchControlPointSpline_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [IsClosed](../SketchControlPointSpline/SketchControlPointSpline_IsClosed.md) | Read-only property that returns whether the curve is closed. |
| [Layer](../SketchControlPointSpline/SketchControlPointSpline_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [Length](../SketchControlPointSpline/SketchControlPointSpline_Length.md) | Returns the length of the entity in centimeters. |
| [LineDefinitionSpace](../SketchControlPointSpline/SketchControlPointSpline_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this sketch spline. |
| [LineScale](../SketchControlPointSpline/SketchControlPointSpline_LineScale.md) | Gets and sets the LineScale applied to this sketch spline. |
| [LineType](../SketchControlPointSpline/SketchControlPointSpline_LineType.md) | Gets and sets the LineType applied to this sketch spline. |
| [LineWeight](../SketchControlPointSpline/SketchControlPointSpline_LineWeight.md) | Gets and sets the LineWeight applied to this entity. |
| [OverrideColor](../SketchControlPointSpline/SketchControlPointSpline_OverrideColor.md) | Gets and sets the color applied to this sketch spline. |
| [OwnedBy](../SketchControlPointSpline/SketchControlPointSpline_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchControlPointSpline/SketchControlPointSpline_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchControlPointSpline/SketchControlPointSpline_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchControlPointSpline/SketchControlPointSpline_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchControlPointSpline/SketchControlPointSpline_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchControlPointSpline/SketchControlPointSpline_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchControlPointSpline/SketchControlPointSpline_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchControlPointSpline/SketchControlPointSpline_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [StartSketchPoint](../SketchControlPointSpline/SketchControlPointSpline_StartSketchPoint.md) | Read-only property that returns the sketch point that defines the position of the start of the spline. |
| [Type](../SketchControlPointSpline/SketchControlPointSpline_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SketchControlPointSplineProxy.NativeObject](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_NativeObject.md), [SketchControlPointSplines.Add](../SketchControlPointSplines/SketchControlPointSplines_Add.md), [SketchControlPointSplines.Item](../SketchControlPointSplines/SketchControlPointSplines_Item.md)

## Derived Classes

[SketchControlPointSplineProxy](../SketchControlPointSplineProxy/SketchControlPointSplineProxy.md)

## Version

Introduced in version 2014
