# Balloon Object

## Description

The Balloon object provides the ability to access existing balloons.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../Balloon/Balloon_Delete.md) | Method to delete this Balloon. |
| [GetBalloonType](../Balloon/Balloon_GetBalloonType.md) | Method that gets the balloon type. |
| [GetReferenceKey](../Balloon/Balloon_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SaveItemOverridesToBOM](../Balloon/Balloon_SaveItemOverridesToBOM.md) | Method that saves any overrides to the item values in the balloon to the model BOM. Only the overrides applies to the BallonValueSet.Value property are saved. The value of the OverrideValue property is ignored. |
| [SetBalloonType](../Balloon/Balloon_SetBalloonType.md) | Method that sets the balloon type. |
| [SortValueSets](../Balloon/Balloon_SortValueSets.md) | Method that sorts the balloon value sets. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Balloon/Balloon_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Attached](../Balloon/Balloon_Attached.md) | Property that returns whether the balloon is attached to a component. |
| [AttributeSets](../Balloon/Balloon_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BalloonValueSets](../Balloon/Balloon_BalloonValueSets.md) | This property gets the collection of objects. See the BalloonValueSets and BalloonValueSet objects for more information. |
| [Layer](../Balloon/Balloon_Layer.md) | Gets and sets the layer applied to this balloons. |
| [Leader](../Balloon/Balloon_Leader.md) | Property that returns the leader associated with the balloon. |
| [Parent](../Balloon/Balloon_Parent.md) | Property returning the parent sheet (the sheet object this balloon is associated with). |
| [ParentView](../Balloon/Balloon_ParentView.md) | Property that returns the parent DrawingView object. In other words, the sheet contains a view with which this balloon is associated. |
| [PlacementDirection](../Balloon/Balloon_PlacementDirection.md) | Gets and sets the direction in which to place attached balloons. |
| [Position](../Balloon/Balloon_Position.md) | Gets and sets the position of the balloon on the Sheet. |
| [Style](../Balloon/Balloon_Style.md) | Gets and sets the associated BalloonStyle object. |
| [Type](../Balloon/Balloon_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Balloons.Add](../Balloons/Balloons_Add.md), [Balloons.Item](../Balloons/Balloons_Item.md), [BalloonValueSet.Parent](../BalloonValueSet/BalloonValueSet_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Balloons - edit](../../sample-programs/Balloons_Sample.md) | This sample demonstrates the editing of balloons in a drawing. |
| [Find component referenced by balloon](../../sample-programs/BalloonValueSet_ReferencedRow_Sample.md) | This sample demonstrates how to find the component that a balloon references. |

## Version

Introduced in version 9
