# SketchOffsetSpline Object

Derived from: [SketchEntity](../SketchEntity/SketchEntity.md) Object

## Description

The SketchOffsetSpline object represents an offset spline within a sketch. These special splines are created as a result of offsetting splines and ellipses in a sketch. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToSpline](../SketchOffsetSpline/SketchOffsetSpline_ConvertToSpline.md) | Method that converts the offset spline to a SketchSpline object and breaks the association to the spline from which it is offset. |
| [Delete](../SketchOffsetSpline/SketchOffsetSpline_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetCustomLineType](../SketchOffsetSpline/SketchOffsetSpline_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../SketchOffsetSpline/SketchOffsetSpline_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetCustomLineType](../SketchOffsetSpline/SketchOffsetSpline_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchOffsetSpline/SketchOffsetSpline_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchOffsetSpline/SketchOffsetSpline_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Closed](../SketchOffsetSpline/SketchOffsetSpline_Closed.md) | Boolean property that gets whether the curve is closed. A periodic curve is closed and curvature continuous at the closure. |
| [Constraints](../SketchOffsetSpline/SketchOffsetSpline_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchOffsetSpline/SketchOffsetSpline_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchOffsetSpline/SketchOffsetSpline_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingSketchBlock](../SketchOffsetSpline/SketchOffsetSpline_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [CurvatureDisplay](../SketchOffsetSpline/SketchOffsetSpline_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the offset spline. |
| [DisabledActionTypes](../SketchOffsetSpline/SketchOffsetSpline_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [EndSketchPoint](../SketchOffsetSpline/SketchOffsetSpline_EndSketchPoint.md) | Property that returns the that defines the position of the end of the spline. |
| [Geometry](../SketchOffsetSpline/SketchOffsetSpline_Geometry.md) | Property that returns a geometry object. The object returned represents a "snapshot" view of the current state of the offset sketch spline. |
| [Geometry3d](../SketchOffsetSpline/SketchOffsetSpline_Geometry3d.md) | Read-only property that returns b-spline geometry that represents this spline in model space. |
| [HasReferenceComponent](../SketchOffsetSpline/SketchOffsetSpline_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Layer](../SketchOffsetSpline/SketchOffsetSpline_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [Length](../SketchOffsetSpline/SketchOffsetSpline_Length.md) | Double property that returns the length of the entity in centimeters. |
| [LineDefinitionSpace](../SketchOffsetSpline/SketchOffsetSpline_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this sketch spline. |
| [LineScale](../SketchOffsetSpline/SketchOffsetSpline_LineScale.md) | Gets and sets the LineScale applied to this sketch spline. |
| [LineType](../SketchOffsetSpline/SketchOffsetSpline_LineType.md) | Gets and sets the LineType applied to this sketch spline. |
| [LineWeight](../SketchOffsetSpline/SketchOffsetSpline_LineWeight.md) | Gets and sets the LineWeight applied to this sketch spline. |
| [OriginalSpline](../SketchOffsetSpline/SketchOffsetSpline_OriginalSpline.md) | Returns the original spline that was used as the source to create the offset spline. |
| [OverrideColor](../SketchOffsetSpline/SketchOffsetSpline_OverrideColor.md) | Gets and sets the color applied to this sketch spline. |
| [OwnedBy](../SketchOffsetSpline/SketchOffsetSpline_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchOffsetSpline/SketchOffsetSpline_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchOffsetSpline/SketchOffsetSpline_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchOffsetSpline/SketchOffsetSpline_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchOffsetSpline/SketchOffsetSpline_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchOffsetSpline/SketchOffsetSpline_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchOffsetSpline/SketchOffsetSpline_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchOffsetSpline/SketchOffsetSpline_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [StartSketchPoint](../SketchOffsetSpline/SketchOffsetSpline_StartSketchPoint.md) | Property that returns the that defines the position of the start of the spline. |
| [Type](../SketchOffsetSpline/SketchOffsetSpline_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[OffsetSplineDimConstraint.OffsetSpline](../OffsetSplineDimConstraint/OffsetSplineDimConstraint_OffsetSpline.md), [OffsetSplineDimConstraintProxy.OffsetSpline](../OffsetSplineDimConstraintProxy/OffsetSplineDimConstraintProxy_OffsetSpline.md), [SketchOffsetSplineProxy.NativeObject](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_NativeObject.md), [SketchOffsetSplines.Item](../SketchOffsetSplines/SketchOffsetSplines_Item.md)

## Derived Classes

[SketchOffsetSplineProxy](../SketchOffsetSplineProxy/SketchOffsetSplineProxy.md)

## Version

Introduced in version 9
