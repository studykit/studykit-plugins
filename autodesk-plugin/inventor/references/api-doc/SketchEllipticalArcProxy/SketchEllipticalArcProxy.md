# SketchEllipticalArcProxy Object

Derived from: [SketchEllipticalArc](../SketchEllipticalArc/SketchEllipticalArc.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetCustomLineType](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetCustomLineType](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CenterSketchPoint](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_CenterSketchPoint.md) | Property that gets the sketch point that defines the position of the center of the elliptical arc. |
| [Constraints](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingOccurrence](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ContainingSketchBlock](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [CurvatureDisplay](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the elliptical arc. |
| [DisabledActionTypes](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [EndSketchPoint](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_EndSketchPoint.md) | Property that returns the end of the elliptical arc. |
| [Geometry](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_Geometry.md) | Property that returns an EllipticalArc2d geometry object. The object returned represents a snapshot view of the current state of the sketch elliptical arc. |
| [Geometry3d](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_Geometry3d.md) | Read-only property that returns elliptical arc geometry that represents this elliptical arc in model space. |
| [HasReferenceComponent](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Layer](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [Length](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_Length.md) | Double property that returns the length of the entity in centimeters. |
| [LineDefinitionSpace](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this elliptical arc. |
| [LineScale](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_LineScale.md) | Gets and sets the LineScale applied to this elliptical arc. |
| [LineType](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_LineType.md) | Gets and sets the LineType applied to this elliptical arc. |
| [LineWeight](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_LineWeight.md) | Gets and sets the LineWeight applied to this elliptical arc. |
| [MajorAxisVector](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_MajorAxisVector.md) | Gets and sets the major axis vector. This vector defines the direction of the major axis. |
| [MajorRadius](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_MajorRadius.md) | Gets and sets the major radius. |
| [MinorRadius](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_MinorRadius.md) | Gets and sets the minor radius. |
| [NativeObject](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OverrideColor](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_OverrideColor.md) | Gets and sets the color applied to this elliptical arc. |
| [OwnedBy](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [StartAngle](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_StartAngle.md) | Double property that returns the start angle of the elliptical arc. This is measured counterclockwise from the major axis in radians. |
| [StartSketchPoint](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_StartSketchPoint.md) | Property that gets the start of the elliptical arc. |
| [SweepAngle](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_SweepAngle.md) | Double property that returns the sweep angle of the elliptical arc. This is measured counterclockwise from the major axis in radians. |
| [Type](../SketchEllipticalArcProxy/SketchEllipticalArcProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |