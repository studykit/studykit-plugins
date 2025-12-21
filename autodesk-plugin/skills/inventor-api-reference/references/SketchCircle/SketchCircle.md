# SketchCircle Object

Derived from: [SketchEntity](../SketchEntity/SketchEntity.md) Object

## Description

The SketchCircle object represents a circle within a sketch. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchCircle/SketchCircle_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetCustomLineType](../SketchCircle/SketchCircle_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../SketchCircle/SketchCircle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetCustomLineType](../SketchCircle/SketchCircle_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchCircle/SketchCircle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Area](../SketchCircle/SketchCircle_Area.md) | Double property that returns the area of the entity in square centimeters. |
| [AttributeSets](../SketchCircle/SketchCircle_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CenterSketchPoint](../SketchCircle/SketchCircle_CenterSketchPoint.md) | Property that gets the sketch point that defines the position of the center of the circle. |
| [Constraints](../SketchCircle/SketchCircle_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchCircle/SketchCircle_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchCircle/SketchCircle_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingSketchBlock](../SketchCircle/SketchCircle_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [CurvatureDisplay](../SketchCircle/SketchCircle_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the circle. |
| [DisabledActionTypes](../SketchCircle/SketchCircle_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [Geometry](../SketchCircle/SketchCircle_Geometry.md) | Property that returns a Circle2d geometry object. The object returned represents a snapshot view of the current state of the sketch circle. |
| [Geometry3d](../SketchCircle/SketchCircle_Geometry3d.md) | Read-only property that returns circle geometry that represents this circle in model space. |
| [HasReferenceComponent](../SketchCircle/SketchCircle_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Layer](../SketchCircle/SketchCircle_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [Length](../SketchCircle/SketchCircle_Length.md) | Property that returns the length of the entity in centimeters. |
| [LineDefinitionSpace](../SketchCircle/SketchCircle_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this sketch circle. |
| [LineScale](../SketchCircle/SketchCircle_LineScale.md) | Gets and sets the LineScale applied to this sketch circle. |
| [LineType](../SketchCircle/SketchCircle_LineType.md) | Gets and sets the LineType applied to this sketch circle. |
| [LineWeight](../SketchCircle/SketchCircle_LineWeight.md) | Gets and sets the LineWeight applied to this sketch circle. |
| [OverrideColor](../SketchCircle/SketchCircle_OverrideColor.md) | Gets and sets the color applied to this sketch circl. |
| [OwnedBy](../SketchCircle/SketchCircle_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchCircle/SketchCircle_Parent.md) | Property that returns the parent sketch of the entity. |
| [Radius](../SketchCircle/SketchCircle_Radius.md) | Gets and sets the radius of the circle. |
| [RangeBox](../SketchCircle/SketchCircle_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchCircle/SketchCircle_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchCircle/SketchCircle_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchCircle/SketchCircle_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchCircle/SketchCircle_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchCircle/SketchCircle_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [Type](../SketchCircle/SketchCircle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SketchCircleProxy.NativeObject](../SketchCircleProxy/SketchCircleProxy_NativeObject.md), [SketchCircles.AddByCenterRadius](../SketchCircles/SketchCircles_AddByCenterRadius.md), [SketchCircles.AddByThreePoints](../SketchCircles/SketchCircles_AddByThreePoints.md), [SketchCircles.Item](../SketchCircles/SketchCircles_Item.md)

## Derived Classes

[SketchCircleProxy](../SketchCircleProxy/SketchCircleProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Create sheet metal lofted flange feature](../../sample-programs/LoftedFlangeFeatures_Add_Sample.md) | The following sample demonstrates the creation of a sheet metal lofted flange feature. |
| [Sketch from Face Silhouette](../../sample-programs/PlanarSketch_AddBySilhouette_Sample.md) | This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder. |
| [Sketch Edit Orientation](../../sample-programs/PlanarSketch_NaturalAxisDirection_Sample.md) | This sample demonstrates modifying the orientation of a sketch. |
| [Sketch Add Oriented](../../sample-programs/PlanarSketches_AddWithOrientation_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.AddWithOrientation method. |
| [Sketch Display Entities](../../sample-programs/SketchEntity_Sample.md) | This sample demonstrates the query functionality available for sketch entities. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |