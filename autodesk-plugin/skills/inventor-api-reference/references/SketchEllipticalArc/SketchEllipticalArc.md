# SketchEllipticalArc Object

Derived from: [SketchEntity](../SketchEntity/SketchEntity.md) Object

## Description

The SketchEllipticalArc object represents an elliptical arc within a sketch. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchEllipticalArc/SketchEllipticalArc_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetCustomLineType](../SketchEllipticalArc/SketchEllipticalArc_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../SketchEllipticalArc/SketchEllipticalArc_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetCustomLineType](../SketchEllipticalArc/SketchEllipticalArc_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchEllipticalArc/SketchEllipticalArc_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchEllipticalArc/SketchEllipticalArc_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CenterSketchPoint](../SketchEllipticalArc/SketchEllipticalArc_CenterSketchPoint.md) | Property that gets the sketch point that defines the position of the center of the elliptical arc. |
| [Constraints](../SketchEllipticalArc/SketchEllipticalArc_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchEllipticalArc/SketchEllipticalArc_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchEllipticalArc/SketchEllipticalArc_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingSketchBlock](../SketchEllipticalArc/SketchEllipticalArc_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [CurvatureDisplay](../SketchEllipticalArc/SketchEllipticalArc_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the elliptical arc. |
| [DisabledActionTypes](../SketchEllipticalArc/SketchEllipticalArc_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [EndSketchPoint](../SketchEllipticalArc/SketchEllipticalArc_EndSketchPoint.md) | Property that returns the end of the elliptical arc. |
| [Geometry](../SketchEllipticalArc/SketchEllipticalArc_Geometry.md) | Property that returns an EllipticalArc2d geometry object. The object returned represents a snapshot view of the current state of the sketch elliptical arc. |
| [Geometry3d](../SketchEllipticalArc/SketchEllipticalArc_Geometry3d.md) | Read-only property that returns elliptical arc geometry that represents this elliptical arc in model space. |
| [HasReferenceComponent](../SketchEllipticalArc/SketchEllipticalArc_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Layer](../SketchEllipticalArc/SketchEllipticalArc_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [Length](../SketchEllipticalArc/SketchEllipticalArc_Length.md) | Double property that returns the length of the entity in centimeters. |
| [LineDefinitionSpace](../SketchEllipticalArc/SketchEllipticalArc_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this elliptical arc. |
| [LineScale](../SketchEllipticalArc/SketchEllipticalArc_LineScale.md) | Gets and sets the LineScale applied to this elliptical arc. |
| [LineType](../SketchEllipticalArc/SketchEllipticalArc_LineType.md) | Gets and sets the LineType applied to this elliptical arc. |
| [LineWeight](../SketchEllipticalArc/SketchEllipticalArc_LineWeight.md) | Gets and sets the LineWeight applied to this elliptical arc. |
| [MajorAxisVector](../SketchEllipticalArc/SketchEllipticalArc_MajorAxisVector.md) | Gets and sets the major axis vector. This vector defines the direction of the major axis. |
| [MajorRadius](../SketchEllipticalArc/SketchEllipticalArc_MajorRadius.md) | Gets and sets the major radius. |
| [MinorRadius](../SketchEllipticalArc/SketchEllipticalArc_MinorRadius.md) | Gets and sets the minor radius. |
| [OverrideColor](../SketchEllipticalArc/SketchEllipticalArc_OverrideColor.md) | Gets and sets the color applied to this elliptical arc. |
| [OwnedBy](../SketchEllipticalArc/SketchEllipticalArc_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchEllipticalArc/SketchEllipticalArc_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchEllipticalArc/SketchEllipticalArc_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchEllipticalArc/SketchEllipticalArc_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchEllipticalArc/SketchEllipticalArc_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchEllipticalArc/SketchEllipticalArc_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchEllipticalArc/SketchEllipticalArc_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchEllipticalArc/SketchEllipticalArc_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [StartAngle](../SketchEllipticalArc/SketchEllipticalArc_StartAngle.md) | Double property that returns the start angle of the elliptical arc. This is measured counterclockwise from the major axis in radians. |
| [StartSketchPoint](../SketchEllipticalArc/SketchEllipticalArc_StartSketchPoint.md) | Property that gets the start of the elliptical arc. |
| [SweepAngle](../SketchEllipticalArc/SketchEllipticalArc_SweepAngle.md) | Double property that returns the sweep angle of the elliptical arc. This is measured counterclockwise from the major axis in radians. |
| [Type](../SketchEllipticalArc/SketchEllipticalArc_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SketchEllipticalArcProxy.NativeObject](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_NativeObject.md), [SketchEllipticalArcs.Add](../SketchEllipticalArcs/SketchEllipticalArcs_Add.md), [SketchEllipticalArcs.Item](../SketchEllipticalArcs/SketchEllipticalArcs_Item.md)

## Derived Classes

[SketchEllipticalArcProxy](../SketchEllipticalArcProxy/SketchEllipticalArcProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sketch elliptical arc](../../sample-programs/SketchEllipticalArc_Sample.md) | This sample demonstrates creating an elliptical arc in a sketch and dimensioning its minor radius. |
| [Sketch Display Entities](../../sample-programs/SketchEntity_Sample.md) | This sample demonstrates the query functionality available for sketch entities. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |