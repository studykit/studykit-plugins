# UserCoordinateSystems Object

## Description

The UserCoordinateSystems collection object contains all user coordinate systems within the document and provides methods to create additional ones.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../UserCoordinateSystems/UserCoordinateSystems_Add.md) | Method that creates a new User Coordinate System. The newly created UserCoordinateSystem object is returned. |
| [CreateDefinition](../UserCoordinateSystems/UserCoordinateSystems_CreateDefinition.md) | Method that creates a new UserCoordinateSystemDefinition object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../UserCoordinateSystems/UserCoordinateSystems_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../UserCoordinateSystems/UserCoordinateSystems_Count.md) | Property that returns the number of items in the collection. |
| [Item](../UserCoordinateSystems/UserCoordinateSystems_Item.md) | Returns the specified UserCoordinateSystem object from the collection. |
| [Type](../UserCoordinateSystems/UserCoordinateSystems_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.UserCoordinateSystems](../AssemblyComponentDefinition/AssemblyComponentDefinition_UserCoordinateSystems.md), [FlatPattern.UserCoordinateSystems](../FlatPattern/FlatPattern_UserCoordinateSystems.md), [PartComponentDefinition.UserCoordinateSystems](../PartComponentDefinition/PartComponentDefinition_UserCoordinateSystems.md), [SheetMetalComponentDefinition.UserCoordinateSystems](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_UserCoordinateSystems.md), [WeldmentComponentDefinition.UserCoordinateSystems](../WeldmentComponentDefinition/WeldmentComponentDefinition_UserCoordinateSystems.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [UCS by three points](../../sample-programs/UserCoordinateSystems_Add_Sample.md) | This sample demonstrates the creation of a User Coordinate System (UCS) based on 3 points that define the origin, x-direction and y-direction for the UCS. |
| [UCS by transformation matrix](../../sample-programs/UserCoordinateSystems_CreateDefinition_Sample.md) | This sample demonstrates the creation of a user coordinate system (UCS) by specifying a transformation matrix. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |