# SketchControlPointSplineProxy Object

Derived from: [SketchControlPointSpline](../SketchControlPointSpline/SketchControlPointSpline.md) Object

## Description

Proxy for the SketchControlPointSpline object. This object is used to represent a SketchControlPointSpline object from a part in an assembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToSpline](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_ConvertToSpline.md) | Method that inserts a new control point into the existing control point spline. |
| [Delete](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetCustomLineType](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [InsertKnot](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_InsertKnot.md) | Method that inserts a knot into the existing control point spline. The effect of this will be that the shape of the curve is maintained, but the control polygon will change shape and one additional point will be added. |
| [SetCustomLineType](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Constraints](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingOccurrence](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ContainingSketchBlock](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [ControlPoint](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_ControlPoint.md) | Read-only property that returns the SketchPoint at the specified index. The indices correspond to the control points in order from the start to the end of the spline. An Index of 1 returns the first SketchPoint. The ControlPointCount property returns the total number of control points for the spline. Deleting the returned sketch point will delete the control point from the spline. |
| [ControlPointCount](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_ControlPointCount.md) | Read-only property that returns the number of control points defining the control point spline. |
| [ControlPolygonSide](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_ControlPolygonSide.md) | Read-only property that returns the SketchLine that represents a side of the control polygon. The indices correspond to the control polygon edges in order from the start to the end of the spline. An Index of 1 returns the first edge, with the last side being ControlPointCount -1 since there is one less side than number of control points. |
| [CurvatureDisplay](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the spline. |
| [DisabledActionTypes](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [EndSketchPoint](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_EndSketchPoint.md) | Read-only property that returns the sketch point that defines the position of the end of the spline. |
| [Geometry](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_Geometry.md) | Read-only property that returns a BSplineCurve2d geometry object. The object returned represents a 'snapshot' view of the current state of the spline. |
| [Geometry3d](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_Geometry3d.md) | Read-only property that returns b-spline geometry that represents this spline in model space. |
| [HasReferenceComponent](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [IsClosed](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_IsClosed.md) | Read-only property that returns whether the curve is closed. |
| [Layer](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [Length](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_Length.md) | Returns the length of the entity in centimeters. |
| [LineDefinitionSpace](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this sketch spline. |
| [LineScale](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_LineScale.md) | Gets and sets the LineScale applied to this sketch spline. |
| [LineType](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_LineType.md) | Gets and sets the LineType applied to this sketch spline. |
| [LineWeight](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_LineWeight.md) | Gets and sets the LineWeight applied to this entity. |
| [NativeObject](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OverrideColor](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_OverrideColor.md) | Gets and sets the color applied to this sketch spline. |
| [OwnedBy](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [StartSketchPoint](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_StartSketchPoint.md) | Read-only property that returns the sketch point that defines the position of the start of the spline. |
| [Type](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |