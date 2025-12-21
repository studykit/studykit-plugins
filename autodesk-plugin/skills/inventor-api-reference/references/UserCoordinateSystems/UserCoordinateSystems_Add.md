# UserCoordinateSystems.Add Method

Parent Object: [UserCoordinateSystems](../UserCoordinateSystems/UserCoordinateSystems.md)

## Description

Method that creates a new User Coordinate System. The newly created UserCoordinateSystem object is returned.

## Syntax

UserCoordinateSystems.**Add**( ***Definition*** As [UserCoordinateSystemDefinition](../UserCoordinateSystemDefinition/UserCoordinateSystemDefinition.md) ) As [UserCoordinateSystem](../UserCoordinateSystem/UserCoordinateSystem.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Definition | [UserCoordinateSystemDefinition](../UserCoordinateSystemDefinition/UserCoordinateSystemDefinition.md) | Input UserCoordinateSystemDefinition object that defines the coordinate system you want to create. A UserCoordinateSystemDefinition object can be created using the UserCoordinateSystems.CreateDefinition method. It can also be obtained from an existing UserCoordinateSystem object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [UCS by three points](../../sample-programs/UserCoordinateSystems_Add_Sample.md) | This sample demonstrates the creation of a User Coordinate System (UCS) based on 3 points that define the origin, x-direction and y-direction for the UCS. |
| [UCS by transformation matrix](../../sample-programs/UserCoordinateSystems_CreateDefinition_Sample.md) | This sample demonstrates the creation of a user coordinate system (UCS) by specifying a transformation matrix. |

## Version

Introduced in version 2011
