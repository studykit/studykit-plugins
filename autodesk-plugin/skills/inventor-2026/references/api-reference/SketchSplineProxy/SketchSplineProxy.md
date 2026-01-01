# SketchSplineProxy Object

Derived from: [SketchSpline](../SketchSpline/SketchSpline.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchSplineProxy/SketchSplineProxy_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetCustomLineType](../SketchSplineProxy/SketchSplineProxy_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetHandle](../SketchSplineProxy/SketchSplineProxy_GetHandle.md) | Method that returns the fit point handle at the given fit point. The method returns Nothing if the handle is not enabled at the input fit point. |
| [GetHandleStatus](../SketchSplineProxy/SketchSplineProxy_GetHandleStatus.md) | Method that returns whether the handle at a given fit point is enabled or disabled. |
| [GetReferenceKey](../SketchSplineProxy/SketchSplineProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [InsertFitPoint](../SketchSplineProxy/SketchSplineProxy_InsertFitPoint.md) | Method that inserts a new fit point into the spline. |
| [SetCustomLineType](../SketchSplineProxy/SketchSplineProxy_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |
| [SetHandleStatus](../SketchSplineProxy/SketchSplineProxy_SetHandleStatus.md) | Method that sets whether the handle at a given fit point is enabled or disabled. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchSplineProxy/SketchSplineProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchSplineProxy/SketchSplineProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Closed](../SketchSplineProxy/SketchSplineProxy_Closed.md) | Specifies whether the curve is closed. Setting a curve to be closed will cause it to close and be periodic. |
| [Constraints](../SketchSplineProxy/SketchSplineProxy_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchSplineProxy/SketchSplineProxy_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchSplineProxy/SketchSplineProxy_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingOccurrence](../SketchSplineProxy/SketchSplineProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ContainingSketchBlock](../SketchSplineProxy/SketchSplineProxy_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [CurvatureDisplay](../SketchSplineProxy/SketchSplineProxy_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the spline. |
| [DisabledActionTypes](../SketchSplineProxy/SketchSplineProxy_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [EndSketchPoint](../SketchSplineProxy/SketchSplineProxy_EndSketchPoint.md) | Property that gets the that defines the position of the end of the spline. |
| [FitMethod](../SketchSplineProxy/SketchSplineProxy_FitMethod.md) | Specifies the fit method for the spline. |
| [FitPoint](../SketchSplineProxy/SketchSplineProxy_FitPoint.md) | Property that returns the SketchPoint at the specified index. The indices correspond to the fit points in order from the start to the end of the spline. An Index of 1 returns the first SketchPoint. The FitPointCount property returns the total number of fits points for the spline. |
| [FitPointCount](../SketchSplineProxy/SketchSplineProxy_FitPointCount.md) | Property that returns the number of fit points for the spline. |
| [Geometry](../SketchSplineProxy/SketchSplineProxy_Geometry.md) | Property that returns a geometry object. The object returned represents a snapshot view of the current state of the sketch spline. |
| [Geometry3d](../SketchSplineProxy/SketchSplineProxy_Geometry3d.md) | Read-only property that returns the BSplineCurve geometry that represents this sketch spline in model space. |
| [HasReferenceComponent](../SketchSplineProxy/SketchSplineProxy_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Layer](../SketchSplineProxy/SketchSplineProxy_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [Length](../SketchSplineProxy/SketchSplineProxy_Length.md) | Double property that returns the length of the entity in centimeters. |
| [LineDefinitionSpace](../SketchSplineProxy/SketchSplineProxy_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this sketch spline. |
| [LineScale](../SketchSplineProxy/SketchSplineProxy_LineScale.md) | Gets and sets the LineScale applied to this sketch spline. |
| [LineType](../SketchSplineProxy/SketchSplineProxy_LineType.md) | Gets and sets the LineType applied to this sketch spline. |
| [LineWeight](../SketchSplineProxy/SketchSplineProxy_LineWeight.md) | Gets and sets the LineWeight applied to this sketch spline. |
| [NativeObject](../SketchSplineProxy/SketchSplineProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OverrideColor](../SketchSplineProxy/SketchSplineProxy_OverrideColor.md) | Gets and sets the color applied to this sketch spline. |
| [OwnedBy](../SketchSplineProxy/SketchSplineProxy_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchSplineProxy/SketchSplineProxy_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchSplineProxy/SketchSplineProxy_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchSplineProxy/SketchSplineProxy_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchSplineProxy/SketchSplineProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchSplineProxy/SketchSplineProxy_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchSplineProxy/SketchSplineProxy_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchSplineProxy/SketchSplineProxy_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [StartSketchPoint](../SketchSplineProxy/SketchSplineProxy_StartSketchPoint.md) | Property that returns the that defines the position of the start of the line. |
| [Tension](../SketchSplineProxy/SketchSplineProxy_Tension.md) | Gets and sets the tension for the spline. |
| [Type](../SketchSplineProxy/SketchSplineProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6
