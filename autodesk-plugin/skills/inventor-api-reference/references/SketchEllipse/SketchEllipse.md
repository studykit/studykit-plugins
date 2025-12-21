# SketchEllipse Object

Derived from: [SketchEntity](../SketchEntity/SketchEntity.md) Object

## Description

The SketchEllipse object represents an ellipse within a sketch. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SketchEllipse/SketchEllipse_Delete.md) | Method that deletes the sketch entity. This method will fail in the case where this object was created as a result of a derived part. The HasReferenceComponent property can be used to determine when this is the case. |
| [GetCustomLineType](../SketchEllipse/SketchEllipse_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../SketchEllipse/SketchEllipse_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetCustomLineType](../SketchEllipse/SketchEllipse_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchEllipse/SketchEllipse_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Area](../SketchEllipse/SketchEllipse_Area.md) | Double property that returns the area of the entity in square centimeters. |
| [AttributeSets](../SketchEllipse/SketchEllipse_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CenterSketchPoint](../SketchEllipse/SketchEllipse_CenterSketchPoint.md) | Property that gets the sketch point that defines the position of the center of the ellipse. |
| [Constraints](../SketchEllipse/SketchEllipse_Constraints.md) | Property that returns a collection of sketch constraints that are tied directly to this entity. This collection consists of both geometric and dimension constraints. |
| [ConstraintStatus](../SketchEllipse/SketchEllipse_ConstraintStatus.md) | Read-only property that returns the constraint status of the sketch. Possible return values are kFullyConstrainedConstraintStatus, kOverConstrainedConstraintStatus, kUnderConstrainedConstraintStatus, and kUnknownConstraintStatus. |
| [Construction](../SketchEllipse/SketchEllipse_Construction.md) | Gets and sets whether the entity behaves as a construction entity or not. |
| [ContainingSketchBlock](../SketchEllipse/SketchEllipse_ContainingSketchBlock.md) | Property that returns the sketch block that contains this object. This is the same SketchBlock returned as the last item in the SketchBlockPath property. This property returns Nothing if this object does not belong to a sketch block and lives directly under a sketch. |
| [CurvatureDisplay](../SketchEllipse/SketchEllipse_CurvatureDisplay.md) | Specifies whether curvature information is displayed for the ellipse. |
| [DisabledActionTypes](../SketchEllipse/SketchEllipse_DisabledActionTypes.md) | Gets and sets whether specific user actions are blocked on this sketch geometry. |
| [Geometry](../SketchEllipse/SketchEllipse_Geometry.md) | Property that returns an EllipseFull2d geometry object. The object returned represents a snapshot view of the current state of the sketch ellipse. |
| [Geometry3d](../SketchEllipse/SketchEllipse_Geometry3d.md) | Read-only property that returns ellipse geometry that represents this ellipse in model space. |
| [HasReferenceComponent](../SketchEllipse/SketchEllipse_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Layer](../SketchEllipse/SketchEllipse_Layer.md) | Gets and sets the layer applied to this sketch entity. |
| [Length](../SketchEllipse/SketchEllipse_Length.md) | Gets the length of the ellipse. |
| [LineDefinitionSpace](../SketchEllipse/SketchEllipse_LineDefinitionSpace.md) | Gets and sets the LineDefinitionSpace applied to this sketch line. |
| [LineScale](../SketchEllipse/SketchEllipse_LineScale.md) | Gets and sets the LineScale applied to this sketch line. |
| [LineType](../SketchEllipse/SketchEllipse_LineType.md) | Gets and sets the LineType applied to this sketch line. |
| [LineWeight](../SketchEllipse/SketchEllipse_LineWeight.md) | Gets and sets the LineWeight applied to this sketch line. |
| [MajorAxisVector](../SketchEllipse/SketchEllipse_MajorAxisVector.md) | Gets and sets the major axis vector. This vector defines the direction of the major axis. |
| [MajorRadius](../SketchEllipse/SketchEllipse_MajorRadius.md) | Gets and sets the major radius. |
| [MinorRadius](../SketchEllipse/SketchEllipse_MinorRadius.md) | Gets and sets the minor radius. |
| [OverrideColor](../SketchEllipse/SketchEllipse_OverrideColor.md) | Gets and sets the color applied to this sketch line. |
| [OwnedBy](../SketchEllipse/SketchEllipse_OwnedBy.md) | Indicates entity or entities that own this object. |
| [Parent](../SketchEllipse/SketchEllipse_Parent.md) | Property that returns the parent sketch of the entity. |
| [RangeBox](../SketchEllipse/SketchEllipse_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Reference](../SketchEllipse/SketchEllipse_Reference.md) | Gets and sets whether this entity is a reference entity or not. It is only valid to set this property to False. |
| [ReferenceComponent](../SketchEllipse/SketchEllipse_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../SketchEllipse/SketchEllipse_ReferencedEntity.md) | Property that returns the object this entity is dependent on. When sketch entities are created by projecting model edges or intersecting the model, the resulting entities are driven by the original model entities and cannot be modified. |
| [SketchBlockPath](../SketchEllipse/SketchEllipse_SketchBlockPath.md) | Property that returns the path of sketch blocks at the leaf of which this sketch object is found. The enumerator returns a count of 0 if the object lives directly under a sketch. |
| [SketchOnly](../SketchEllipse/SketchEllipse_SketchOnly.md) | Gets and sets whether this entity is visible only when editing the sketch. |
| [Type](../SketchEllipse/SketchEllipse_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SketchEllipseProxy.NativeObject](../SketchEllipseProxy/SketchEllipseProxy_NativeObject.md), [SketchEllipses.Add](../SketchEllipses/SketchEllipses_Add.md), [SketchEllipses.Item](../SketchEllipses/SketchEllipses_Item.md)

## Derived Classes

[SketchEllipseProxy](../SketchEllipseProxy/SketchEllipseProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch Display Entities](../../sample-programs/SketchEntity_Sample.md) | This sample demonstrates the query functionality available for sketch entities. |

## Version

Introduced in version 5
