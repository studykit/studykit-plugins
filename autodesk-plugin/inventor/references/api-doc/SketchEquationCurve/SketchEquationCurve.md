# SketchEquationCurve Object

Derived from: [SketchEntity](../SketchEntity/SketchEntity.md) Object

## Description

The SketchEquationCurve object represents an equation curve within a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchEquationCurve/SketchEquationCurve_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetCustomLineType](../SketchEquationCurve/SketchEquationCurve_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetEquation](../SketchEquationCurve/SketchEquationCurve_GetEquation.md) | Method that returns all of the information that defines the equation for this curve. To edit the equation use the SetEquation method. |
| [GetReferenceKey](../SketchEquationCurve/SketchEquationCurve_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetCustomLineType](../SketchEquationCurve/SketchEquationCurve_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |
| [SetEquation](../SketchEquationCurve/SketchEquationCurve_SetEquation.md) | Method that returns edits the information of the curve. You can use the GetEquation method to get the current equation values. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchEquationCurve/SketchEquationCurve_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SketchEquationCurve/SketchEquationCurve_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Constraints](../SketchEquationCurve/SketchEquationCurve_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchEquationCurve/SketchEquationCurve_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchEquationCurve/SketchEquationCurve_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingSketchBlock](../SketchEquationCurve/SketchEquationCurve_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [CurvatureDisplay](../SketchEquationCurve/SketchEquationCurve_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the spline. |
| [DisabledActionTypes](../SketchEquationCurve/SketchEquationCurve_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [EndSketchPoint](../SketchEquationCurve/SketchEquationCurve_EndSketchPoint.md) | Read-only property that returns the sketch point that defines the position of the end of the spline. |
| [Geometry](../SketchEquationCurve/SketchEquationCurve_Geometry.md) | Read-only property that retruns a BSplineCurve2d geometry object. The object returned represents a 'snapshot' view of the current state of the spline. |
| [Geometry3d](../SketchEquationCurve/SketchEquationCurve_Geometry3d.md) | Read-only property that returns b-spline geometry that represents this spline in model space. |
| [HasReferenceComponent](../SketchEquationCurve/SketchEquationCurve_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Layer](../SketchEquationCurve/SketchEquationCurve_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [Length](../SketchEquationCurve/SketchEquationCurve_Length.md) | Gets the length of the entity in centimeters. |
| [LineDefinitionSpace](../SketchEquationCurve/SketchEquationCurve_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this sketch spline. |
| [LineScale](../SketchEquationCurve/SketchEquationCurve_LineScale.md) | Gets and sets the LineScale applied to this sketch spline. |
| [LineType](../SketchEquationCurve/SketchEquationCurve_LineType.md) | Gets and sets the LineType applied to this sketch spline. |
| [LineWeight](../SketchEquationCurve/SketchEquationCurve_LineWeight.md) | Gets and sets the LineWeight applied to this sketch spline. |
| [OverrideColor](../SketchEquationCurve/SketchEquationCurve_OverrideColor.md) | Gets and sets the color applied to this sketch spline. |
| [OwnedBy](../SketchEquationCurve/SketchEquationCurve_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchEquationCurve/SketchEquationCurve_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchEquationCurve/SketchEquationCurve_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchEquationCurve/SketchEquationCurve_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchEquationCurve/SketchEquationCurve_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchEquationCurve/SketchEquationCurve_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchEquationCurve/SketchEquationCurve_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchEquationCurve/SketchEquationCurve_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [StartSketchPoint](../SketchEquationCurve/SketchEquationCurve_StartSketchPoint.md) | Gets the sketch point that defines the position of the start of the elliptical arc. |
| [Type](../SketchEquationCurve/SketchEquationCurve_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SketchEquationCurveProxy.NativeObject](../SketchEquationCurveProxy/SketchEquationCurveProxy_NativeObject.md), [SketchEquationCurves.Add](../SketchEquationCurves/SketchEquationCurves_Add.md), [SketchEquationCurves.Item](../SketchEquationCurves/SketchEquationCurves_Item.md)

## Derived Classes

[SketchEquationCurveProxy](../SketchEquationCurveProxy/SketchEquationCurveProxy.md)

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |