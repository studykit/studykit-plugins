# SketchFixedSplineProxy Object

Derived from: [SketchFixedSpline](../SketchFixedSpline/SketchFixedSpline.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToSpline](../SketchFixedSplineProxy/SketchFixedSplineProxy_ConvertToSpline.md) | Method that converts the fixed spline to a SketchSpline object. |
| [Delete](../SketchFixedSplineProxy/SketchFixedSplineProxy_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [Edit](../SketchFixedSplineProxy/SketchFixedSplineProxy_Edit.md) | Method that edits a fixed sketch spline based on an input NURBS definition. |
| [GetCustomLineType](../SketchFixedSplineProxy/SketchFixedSplineProxy_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../SketchFixedSplineProxy/SketchFixedSplineProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetCustomLineType](../SketchFixedSplineProxy/SketchFixedSplineProxy_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchFixedSplineProxy/SketchFixedSplineProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchFixedSplineProxy/SketchFixedSplineProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Closed](../SketchFixedSplineProxy/SketchFixedSplineProxy_Closed.md) | Boolean property that gets whether the curve is closed. A periodic curve is closed and curvature continuous at the closure. |
| [Constraints](../SketchFixedSplineProxy/SketchFixedSplineProxy_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchFixedSplineProxy/SketchFixedSplineProxy_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchFixedSplineProxy/SketchFixedSplineProxy_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingOccurrence](../SketchFixedSplineProxy/SketchFixedSplineProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ContainingSketchBlock](../SketchFixedSplineProxy/SketchFixedSplineProxy_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [DisabledActionTypes](../SketchFixedSplineProxy/SketchFixedSplineProxy_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [EndSketchPoint](../SketchFixedSplineProxy/SketchFixedSplineProxy_EndSketchPoint.md) | Property that returns the that defines the position of the end of the spline. |
| [Geometry](../SketchFixedSplineProxy/SketchFixedSplineProxy_Geometry.md) | Property that returns a geometry object. The object returned represents a 'snapshot' view of the current state of the fixed sketch spline. |
| [Geometry3d](../SketchFixedSplineProxy/SketchFixedSplineProxy_Geometry3d.md) | Read-only property that returns B-Spline geometry that represents this spline in model space. |
| [HasReferenceComponent](../SketchFixedSplineProxy/SketchFixedSplineProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Layer](../SketchFixedSplineProxy/SketchFixedSplineProxy_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [Length](../SketchFixedSplineProxy/SketchFixedSplineProxy_Length.md) | Double property that returns the length of the entity in centimeters. |
| [LineDefinitionSpace](../SketchFixedSplineProxy/SketchFixedSplineProxy_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this sketch fixed spline. |
| [LineScale](../SketchFixedSplineProxy/SketchFixedSplineProxy_LineScale.md) | Gets and sets the LineScale applied to this sketch fixed spline. |
| [LineType](../SketchFixedSplineProxy/SketchFixedSplineProxy_LineType.md) | Gets and sets the LineType applied to this sketch fixed spline. |
| [LineWeight](../SketchFixedSplineProxy/SketchFixedSplineProxy_LineWeight.md) | Gets and sets the LineWeight applied to this sketch fixed spline. |
| [NativeObject](../SketchFixedSplineProxy/SketchFixedSplineProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OverrideColor](../SketchFixedSplineProxy/SketchFixedSplineProxy_OverrideColor.md) | Gets and sets the color applied to this sketch fixed spline. |
| [OwnedBy](../SketchFixedSplineProxy/SketchFixedSplineProxy_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchFixedSplineProxy/SketchFixedSplineProxy_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchFixedSplineProxy/SketchFixedSplineProxy_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchFixedSplineProxy/SketchFixedSplineProxy_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchFixedSplineProxy/SketchFixedSplineProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchFixedSplineProxy/SketchFixedSplineProxy_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchFixedSplineProxy/SketchFixedSplineProxy_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchFixedSplineProxy/SketchFixedSplineProxy_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [StartSketchPoint](../SketchFixedSplineProxy/SketchFixedSplineProxy_StartSketchPoint.md) | Property that returns the that defines the position of the start of the spline. |
| [Type](../SketchFixedSplineProxy/SketchFixedSplineProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9
