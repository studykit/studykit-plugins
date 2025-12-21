# SketchArc Object

Derived from: [SketchEntity](../SketchEntity/SketchEntity.md) Object

## Description

The SketchArc object represents an arc within a sketch. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchArc/SketchArc_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetCustomLineType](../SketchArc/SketchArc_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../SketchArc/SketchArc_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetCustomLineType](../SketchArc/SketchArc_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchArc/SketchArc_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchArc/SketchArc_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CenterSketchPoint](../SketchArc/SketchArc_CenterSketchPoint.md) | Property that gets the sketch point that defines the position of the center of the arc. |
| [Constraints](../SketchArc/SketchArc_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchArc/SketchArc_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchArc/SketchArc_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingSketchBlock](../SketchArc/SketchArc_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [CurvatureDisplay](../SketchArc/SketchArc_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the arc. |
| [DisabledActionTypes](../SketchArc/SketchArc_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [EndSketchPoint](../SketchArc/SketchArc_EndSketchPoint.md) | Property that returns the that defines the position of the end of the arc. |
| [Geometry](../SketchArc/SketchArc_Geometry.md) | Property that returns an geometry object. The object returned represents a 'snapshot' view of the current state of the sketch arc. |
| [Geometry3d](../SketchArc/SketchArc_Geometry3d.md) | Read-only property that returns arc geometry that represents this arc in model space. |
| [HasReferenceComponent](../SketchArc/SketchArc_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Layer](../SketchArc/SketchArc_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [Length](../SketchArc/SketchArc_Length.md) | Property that returns the length of the entity in centimeters. |
| [LineDefinitionSpace](../SketchArc/SketchArc_LineDefinitionSpace.md) | Gets and sets the lineDefinitionSpace applied to this sketch line. |
| [LineScale](../SketchArc/SketchArc_LineScale.md) | Gets and sets the lineScale applied to this sketch line. |
| [LineType](../SketchArc/SketchArc_LineType.md) | Gets and sets the lineType applied to this sketch line. |
| [LineWeight](../SketchArc/SketchArc_LineWeight.md) | Gets and sets the lineWeight applied to this sketch line. |
| [OverrideColor](../SketchArc/SketchArc_OverrideColor.md) | Gets and sets the color applied to this sketch arc. |
| [OwnedBy](../SketchArc/SketchArc_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchArc/SketchArc_Parent.md) | Property that returns the parent sketch of the entity. |
| [Radius](../SketchArc/SketchArc_Radius.md) | Property that returns the radius of the arc. |
| [RangeBox](../SketchArc/SketchArc_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchArc/SketchArc_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchArc/SketchArc_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchArc/SketchArc_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchArc/SketchArc_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchArc/SketchArc_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [StartAngle](../SketchArc/SketchArc_StartAngle.md) | Double property that returns the start angle of the arc. This is measured counterclockwise from the X axis of the sketch in radians. |
| [StartSketchPoint](../SketchArc/SketchArc_StartSketchPoint.md) | Property that gets the that defines the position of the start of the arc. |
| [SweepAngle](../SketchArc/SketchArc_SweepAngle.md) | Double property that returns the sweep angle of the arc. This is measured counterclockwise from the start angle of the arc in radians. |
| [Type](../SketchArc/SketchArc_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[MidpointConstraint.Arc](../MidpointConstraint/MidpointConstraint_Arc.md), [MidpointConstraintProxy.Arc](../MidpointConstraintProxy/MidpointConstraintProxy_Arc.md), [SketchArcProxy.NativeObject](../SketchArcProxy/SketchArcProxy_NativeObject.md), [SketchArcs.AddByCenterStartEndPoint](../SketchArcs/SketchArcs_AddByCenterStartEndPoint.md), [SketchArcs.AddByCenterStartSweepAngle](../SketchArcs/SketchArcs_AddByCenterStartSweepAngle.md), [SketchArcs.AddByFillet](../SketchArcs/SketchArcs_AddByFillet.md), [SketchArcs.AddByThreePoints](../SketchArcs/SketchArcs_AddByThreePoints.md), [SketchArcs.Item](../SketchArcs/SketchArcs_Item.md)

## Derived Classes

[SketchArcProxy](../SketchArcProxy/SketchArcProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch Display Entities](../../sample-programs/SketchEntity_Sample.md) | This sample demonstrates the query functionality available for sketch entities. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |