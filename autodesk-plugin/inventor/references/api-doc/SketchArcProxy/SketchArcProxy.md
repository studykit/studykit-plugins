# SketchArcProxy Object

Derived from: [SketchArc](../SketchArc/SketchArc.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchArcProxy/SketchArcProxy_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetCustomLineType](../SketchArcProxy/SketchArcProxy_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../SketchArcProxy/SketchArcProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetCustomLineType](../SketchArcProxy/SketchArcProxy_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchArcProxy/SketchArcProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchArcProxy/SketchArcProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CenterSketchPoint](../SketchArcProxy/SketchArcProxy_CenterSketchPoint.md) | Property that gets the sketch point that defines the position of the center of the arc. |
| [Constraints](../SketchArcProxy/SketchArcProxy_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchArcProxy/SketchArcProxy_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchArcProxy/SketchArcProxy_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingOccurrence](../SketchArcProxy/SketchArcProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ContainingSketchBlock](../SketchArcProxy/SketchArcProxy_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [CurvatureDisplay](../SketchArcProxy/SketchArcProxy_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the arc. |
| [DisabledActionTypes](../SketchArcProxy/SketchArcProxy_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [EndSketchPoint](../SketchArcProxy/SketchArcProxy_EndSketchPoint.md) | Property that returns the that defines the position of the end of the arc. |
| [Geometry](../SketchArcProxy/SketchArcProxy_Geometry.md) | Property that returns an geometry object. The object returned represents a 'snapshot' view of the current state of the sketch arc. |
| [Geometry3d](../SketchArcProxy/SketchArcProxy_Geometry3d.md) | Read-only property that returns arc geometry that represents this arc in model space. |
| [HasReferenceComponent](../SketchArcProxy/SketchArcProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Layer](../SketchArcProxy/SketchArcProxy_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [Length](../SketchArcProxy/SketchArcProxy_Length.md) | Property that returns the length of the entity in centimeters. |
| [LineDefinitionSpace](../SketchArcProxy/SketchArcProxy_LineDefinitionSpace.md) | Gets and sets the lineDefinitionSpace applied to this sketch line. |
| [LineScale](../SketchArcProxy/SketchArcProxy_LineScale.md) | Gets and sets the lineScale applied to this sketch line. |
| [LineType](../SketchArcProxy/SketchArcProxy_LineType.md) | Gets and sets the lineType applied to this sketch line. |
| [LineWeight](../SketchArcProxy/SketchArcProxy_LineWeight.md) | Gets and sets the lineWeight applied to this sketch line. |
| [NativeObject](../SketchArcProxy/SketchArcProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OverrideColor](../SketchArcProxy/SketchArcProxy_OverrideColor.md) | Gets and sets the color applied to this sketch arc. |
| [OwnedBy](../SketchArcProxy/SketchArcProxy_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchArcProxy/SketchArcProxy_Parent.md) | Property that returns the parent sketch of the entity. |
| [Radius](../SketchArcProxy/SketchArcProxy_Radius.md) | Property that returns the radius of the arc. |
| [RangeBox](../SketchArcProxy/SketchArcProxy_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchArcProxy/SketchArcProxy_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchArcProxy/SketchArcProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchArcProxy/SketchArcProxy_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchArcProxy/SketchArcProxy_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchArcProxy/SketchArcProxy_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [StartAngle](../SketchArcProxy/SketchArcProxy_StartAngle.md) | Double property that returns the start angle of the arc. This is measured counterclockwise from the X axis of the sketch in radians. |
| [StartSketchPoint](../SketchArcProxy/SketchArcProxy_StartSketchPoint.md) | Property that gets the that defines the position of the start of the arc. |
| [SweepAngle](../SketchArcProxy/SketchArcProxy_SweepAngle.md) | Double property that returns the sweep angle of the arc. This is measured counterclockwise from the start angle of the arc in radians. |
| [Type](../SketchArcProxy/SketchArcProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |