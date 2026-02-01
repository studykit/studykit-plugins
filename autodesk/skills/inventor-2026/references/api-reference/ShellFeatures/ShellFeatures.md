# ShellFeatures Object

## Description

The ShellFeatures collection object provides access to all of the objects in a component definition and provides methods to create additional ShellFeatures.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../ShellFeatures/ShellFeatures_Add.md) | Method that creates a new ShellFeature. The new created ShellFeature is returned. |
| [CreateDefinition](../ShellFeatures/ShellFeatures_CreateDefinition.md) | Method that creates a new ShellDefinition object. The object returned by this method isused to define the inputs for a shell feature and is provided as the argument to the Add method of the ShellFeatures collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ShellFeatures/ShellFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../ShellFeatures/ShellFeatures_Count.md) | Property that returns the number of items in this collection. |
| [Item](../ShellFeatures/ShellFeatures_Item.md) | Returns the specified object in the collection. The index can be numeric or the object name. |
| [Type](../ShellFeatures/ShellFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[PartFeatures.ShellFeatures](../PartFeatures/PartFeatures_ShellFeatures.md), [SheetMetalFeatures.ShellFeatures](../SheetMetalFeatures/SheetMetalFeatures_ShellFeatures.md)

## Version

Introduced in version 5
