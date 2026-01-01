# CoilFeatures Object

## Description

The CoilFeatures collection object provides access to all of the objects in a component definition and provides methods to create additional CoilFeature objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddByPitchAndHeight](../CoilFeatures/CoilFeatures_AddByPitchAndHeight.md) | Method that creates a new CoilFeature whose extent is defined by specifying pitch and total height. The new CoilFeature is returned. |
| [AddByPitchAndRevolution](../CoilFeatures/CoilFeatures_AddByPitchAndRevolution.md) | Method that creates a new CoilFeature whose extent is defined by specifying the pitch and number of revolutions. The new CoilFeature is returned. |
| [AddByRevolutionAndHeight](../CoilFeatures/CoilFeatures_AddByRevolutionAndHeight.md) | Method that creates a new CoilFeature whose extent is defined by specifying the number of revolutions and the total height. The new CoilFeature is returned. |
| [AddSpiral](../CoilFeatures/CoilFeatures_AddSpiral.md) | Method that creates a new CoilFeature that sweeps a specified angle. The new CoilFeature is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CoilFeatures/CoilFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../CoilFeatures/CoilFeatures_Count.md) | Property that returns the number of items in this collection. |
| [Item](../CoilFeatures/CoilFeatures_Item.md) | Returns the specified CoilFeature object from the collection. |
| [Type](../CoilFeatures/CoilFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[PartFeatures.CoilFeatures](../PartFeatures/PartFeatures_CoilFeatures.md), [SheetMetalFeatures.CoilFeatures](../SheetMetalFeatures/SheetMetalFeatures_CoilFeatures.md)

## Version

Introduced in version 5
