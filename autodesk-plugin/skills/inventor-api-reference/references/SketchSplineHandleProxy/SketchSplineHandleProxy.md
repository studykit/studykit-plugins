# SketchSplineHandleProxy Object

Derived from: [SketchSplineHandle](../SketchSplineHandle/SketchSplineHandle.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchSplineHandleProxy/SketchSplineHandleProxy_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetCustomLineType](../SketchSplineHandleProxy/SketchSplineHandleProxy_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../SketchSplineHandleProxy/SketchSplineHandleProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetCustomLineType](../SketchSplineHandleProxy/SketchSplineHandleProxy_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchSplineHandleProxy/SketchSplineHandleProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchSplineHandleProxy/SketchSplineHandleProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Centerline](../SketchSplineHandleProxy/SketchSplineHandleProxy_Centerline.md) | Gets and sets whether the line behaves as a centerline or not. |
| [Constraints](../SketchSplineHandleProxy/SketchSplineHandleProxy_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchSplineHandleProxy/SketchSplineHandleProxy_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchSplineHandleProxy/SketchSplineHandleProxy_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingOccurrence](../SketchSplineHandleProxy/SketchSplineHandleProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ContainingSketchBlock](../SketchSplineHandleProxy/SketchSplineHandleProxy_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [DisabledActionTypes](../SketchSplineHandleProxy/SketchSplineHandleProxy_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [EndSketchPoint](../SketchSplineHandleProxy/SketchSplineHandleProxy_EndSketchPoint.md) | Property that returns the that defines the position of the end of the line. |
| [FitPoint](../SketchSplineHandleProxy/SketchSplineHandleProxy_FitPoint.md) | Property that returns the fit point associated with the handle. |
| [Geometry](../SketchSplineHandleProxy/SketchSplineHandleProxy_Geometry.md) | Property that returns a LineSegment2d geometry object. The object returned represents a snapshot view of the current state of the sketch line. |
| [Geometry3d](../SketchSplineHandleProxy/SketchSplineHandleProxy_Geometry3d.md) | Read-only property that returns line segment geometry that represents this line in model space. |
| [HasReferenceComponent](../SketchSplineHandleProxy/SketchSplineHandleProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Layer](../SketchSplineHandleProxy/SketchSplineHandleProxy_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [Length](../SketchSplineHandleProxy/SketchSplineHandleProxy_Length.md) | Double property that returns the length of the entity in centimeters. |
| [LineDefinitionSpace](../SketchSplineHandleProxy/SketchSplineHandleProxy_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this sketch line. |
| [LineScale](../SketchSplineHandleProxy/SketchSplineHandleProxy_LineScale.md) | Gets and sets the LineScale applied to this sketch line. |
| [LineType](../SketchSplineHandleProxy/SketchSplineHandleProxy_LineType.md) | Gets and sets the LineType applied to this sketch line. |
| [LineWeight](../SketchSplineHandleProxy/SketchSplineHandleProxy_LineWeight.md) | Gets and sets the LineWeight applied to this sketch line. |
| [NativeObject](../SketchSplineHandleProxy/SketchSplineHandleProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OverrideColor](../SketchSplineHandleProxy/SketchSplineHandleProxy_OverrideColor.md) | Gets and sets the color applied to this sketch line. |
| [OwnedBy](../SketchSplineHandleProxy/SketchSplineHandleProxy_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchSplineHandleProxy/SketchSplineHandleProxy_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchSplineHandleProxy/SketchSplineHandleProxy_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchSplineHandleProxy/SketchSplineHandleProxy_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchSplineHandleProxy/SketchSplineHandleProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchSplineHandleProxy/SketchSplineHandleProxy_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchSplineHandleProxy/SketchSplineHandleProxy_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchSplineHandleProxy/SketchSplineHandleProxy_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [Spline](../SketchSplineHandleProxy/SketchSplineHandleProxy_Spline.md) | Property that returns the spline associated with the handle. |
| [StartSketchPoint](../SketchSplineHandleProxy/SketchSplineHandleProxy_StartSketchPoint.md) | Property that returns the that defines the position of the start of the line. |
| [Tangent](../SketchSplineHandleProxy/SketchSplineHandleProxy_Tangent.md) | Gets and sets the tangent vector at the fit point associated with this handle. |
| [Type](../SketchSplineHandleProxy/SketchSplineHandleProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Weight](../SketchSplineHandleProxy/SketchSplineHandleProxy_Weight.md) | Gets and sets the tangent weight at the fit point associated with this handle. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |