# SketchLine Object

Derived from: [SketchEntity](../SketchEntity/SketchEntity.md) Object

## Description

The SketchLine object represents a line within a sketch. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchLine/SketchLine_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetCustomLineType](../SketchLine/SketchLine_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../SketchLine/SketchLine_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetCustomLineType](../SketchLine/SketchLine_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchLine/SketchLine_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchLine/SketchLine_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Centerline](../SketchLine/SketchLine_Centerline.md) | Gets and sets whether the line behaves as a centerline or not. |
| [Constraints](../SketchLine/SketchLine_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchLine/SketchLine_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchLine/SketchLine_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingSketchBlock](../SketchLine/SketchLine_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [DisabledActionTypes](../SketchLine/SketchLine_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [EndSketchPoint](../SketchLine/SketchLine_EndSketchPoint.md) | Property that returns the that defines the position of the end of the line. |
| [Geometry](../SketchLine/SketchLine_Geometry.md) | Property that returns a LineSegment2d geometry object. The object returned represents a snapshot view of the current state of the sketch line. |
| [Geometry3d](../SketchLine/SketchLine_Geometry3d.md) | Read-only property that returns line segment geometry that represents this line in model space. |
| [HasReferenceComponent](../SketchLine/SketchLine_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Layer](../SketchLine/SketchLine_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [Length](../SketchLine/SketchLine_Length.md) | Double property that returns the length of the entity in centimeters. |
| [LineDefinitionSpace](../SketchLine/SketchLine_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this sketch line. |
| [LineScale](../SketchLine/SketchLine_LineScale.md) | Gets and sets the LineScale applied to this sketch line. |
| [LineType](../SketchLine/SketchLine_LineType.md) | Gets and sets the LineType applied to this sketch line. |
| [LineWeight](../SketchLine/SketchLine_LineWeight.md) | Gets and sets the LineWeight applied to this sketch line. |
| [OverrideColor](../SketchLine/SketchLine_OverrideColor.md) | Gets and sets the color applied to this sketch line. |
| [OwnedBy](../SketchLine/SketchLine_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchLine/SketchLine_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchLine/SketchLine_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchLine/SketchLine_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchLine/SketchLine_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchLine/SketchLine_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchLine/SketchLine_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchLine/SketchLine_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [StartSketchPoint](../SketchLine/SketchLine_StartSketchPoint.md) | Property that returns the that defines the position of the start of the line. |
| [Type](../SketchLine/SketchLine_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BendPartFeature.BendLine](../BendPartFeature/BendPartFeature_BendLine.md), [BendPartFeatureProxy.BendLine](../BendPartFeatureProxy/BendPartFeatureProxy_BendLine.md), [EqualLengthConstraint.LineOne](../EqualLengthConstraint/EqualLengthConstraint_LineOne.md), [EqualLengthConstraint.LineTwo](../EqualLengthConstraint/EqualLengthConstraint_LineTwo.md), [EqualLengthConstraintProxy.LineOne](../EqualLengthConstraintProxy/EqualLengthConstraintProxy_LineOne.md), [EqualLengthConstraintProxy.LineTwo](../EqualLengthConstraintProxy/EqualLengthConstraintProxy_LineTwo.md), [FoldDefinition.BendLine](../FoldDefinition/FoldDefinition_BendLine.md), [MidpointConstraint.Line](../MidpointConstraint/MidpointConstraint_Line.md), [MidpointConstraintProxy.Line](../MidpointConstraintProxy/MidpointConstraintProxy_Line.md), [OffsetDimConstraint.Line](../OffsetDimConstraint/OffsetDimConstraint_Line.md), [OffsetDimConstraintProxy.Line](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_Line.md), [SketchControlPointSpline.ControlPolygonSide](../SketchControlPointSpline/SketchControlPointSpline_ControlPolygonSide.md), [SketchControlPointSplineProxy.ControlPolygonSide](../SketchControlPointSplineProxy/SketchControlPointSplineProxy_ControlPolygonSide.md), [SketchLineProxy.NativeObject](../SketchLineProxy/SketchLineProxy_NativeObject.md), [SketchLines.AddByMidEndPoints](../SketchLines/SketchLines_AddByMidEndPoints.md), [SketchLines.AddByTwoPoints](../SketchLines/SketchLines_AddByTwoPoints.md), [SketchLines.Item](../SketchLines/SketchLines_Item.md), [SymmetryConstraint.SymmetryLine](../SymmetryConstraint/SymmetryConstraint_SymmetryLine.md), [SymmetryConstraintProxy.SymmetryLine](../SymmetryConstraintProxy/SymmetryConstraintProxy_SymmetryLine.md), [TwoLineAngleDimConstraint.LineOne](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint_LineOne.md), [TwoLineAngleDimConstraint.LineTwo](../TwoLineAngleDimConstraint/TwoLineAngleDimConstraint_LineTwo.md), [TwoLineAngleDimConstraintProxy.LineOne](../TwoLineAngleDimConstraintProxy/TwoLineAngleDimConstraintProxy_LineOne.md), [TwoLineAngleDimConstraintProxy.LineTwo](../TwoLineAngleDimConstraintProxy/TwoLineAngleDimConstraintProxy_LineTwo.md)

## Derived Classes

[SketchLineProxy](../SketchLineProxy/SketchLineProxy.md), [SketchSplineHandle](../SketchSplineHandle/SketchSplineHandle.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Defer sketch updates](../../sample-programs/Sketch_DeferUpdates_Sample.md) | This sample demonstrates the sketch defer update functionality. |
| [Sketch Lines](../../sample-programs/Sketch_SketchLines_Sample.md) | This sample demonstrates creating lines. It uses all of the various methods to create lines, both singly and as rectangles. |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |
| [Sketch Display Entities](../../sample-programs/SketchEntity_Sample.md) | This sample demonstrates the query functionality available for sketch entities. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |
| [Sketch Text Add](../../sample-programs/TextBoxes_Sample.md) | This sample illustrates creating text in a sketch. |

## Version

Introduced in version 5
