# SketchOffsetSplineProxy Object

Derived from: [SketchOffsetSpline](../SketchOffsetSpline/SketchOffsetSpline.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToSpline](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_ConvertToSpline.md) | Method that converts the offset spline to a SketchSpline object and breaks the association to the spline from which it is offset. |
| [Delete](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetCustomLineType](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetCustomLineType](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Closed](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_Closed.md) | Boolean property that gets whether the curve is closed. A periodic curve is closed and curvature continuous at the closure. |
| [Constraints](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingOccurrence](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ContainingSketchBlock](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [CurvatureDisplay](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the offset spline. |
| [DisabledActionTypes](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [EndSketchPoint](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_EndSketchPoint.md) | Property that returns the that defines the position of the end of the spline. |
| [Geometry](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_Geometry.md) | Property that returns a geometry object. The object returned represents a "snapshot" view of the current state of the offset sketch spline. |
| [Geometry3d](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_Geometry3d.md) | Read-only property that returns b-spline geometry that represents this spline in model space. |
| [HasReferenceComponent](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Layer](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [Length](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_Length.md) | Double property that returns the length of the entity in centimeters. |
| [LineDefinitionSpace](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this sketch spline. |
| [LineScale](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_LineScale.md) | Gets and sets the LineScale applied to this sketch spline. |
| [LineType](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_LineType.md) | Gets and sets the LineType applied to this sketch spline. |
| [LineWeight](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_LineWeight.md) | Gets and sets the LineWeight applied to this sketch spline. |
| [NativeObject](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OriginalSpline](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_OriginalSpline.md) | Returns the original spline that was used as the source to create the offset spline. |
| [OverrideColor](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_OverrideColor.md) | Gets and sets the color applied to this sketch spline. |
| [OwnedBy](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [StartSketchPoint](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_StartSketchPoint.md) | Property that returns the that defines the position of the start of the spline. |
| [Type](../SketchOffsetSplineProxy/SketchOffsetSplineProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |