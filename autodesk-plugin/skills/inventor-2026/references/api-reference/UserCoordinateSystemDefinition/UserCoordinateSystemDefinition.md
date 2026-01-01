# UserCoordinateSystemDefinition Object

## Description

The UserCoordinateSystemDefinition object represents the information that defines a coordinate system. You can use this object as input to the UserCoordinateSystems.Add method to create the actual coordinate system.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetByThreePoints](../UserCoordinateSystemDefinition/UserCoordinateSystemDefinition_GetByThreePoints.md) | Method that gets the inputs that fully define the coordinate system. The objects returned will be Nothing if the coordinate system was not parametrically defined (i.e. if the DefinitionType property returns kTransformationDefinitionType). This method returns a failure in assembly documents. |
| [SetByThreePoints](../UserCoordinateSystemDefinition/UserCoordinateSystemDefinition_SetByThreePoints.md) | Method that sets the inputs that fully define the coordinate system. This method returns a failure in assembly documents. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../UserCoordinateSystemDefinition/UserCoordinateSystemDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DefinitionType](../UserCoordinateSystemDefinition/UserCoordinateSystemDefinition_DefinitionType.md) | Property that returns how the inputs for the coordinate system are defined. This can return either kTransformationDefinitionType or kThreePointsDefinitionType. |
| [Parent](../UserCoordinateSystemDefinition/UserCoordinateSystemDefinition_Parent.md) | Property that returns the parent UserCoordinateSystem of this definition. In the case where this is a newly created UserCoordinateSystemDefinition object, this property will return Nothing because there is not a logical parent for the object. |
| [Transformation](../UserCoordinateSystemDefinition/UserCoordinateSystemDefinition_Transformation.md) | Gets and puts the transformation matrix. |
| [Type](../UserCoordinateSystemDefinition/UserCoordinateSystemDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[UserCoordinateSystem.Definition](../UserCoordinateSystem/UserCoordinateSystem_Definition.md), [UserCoordinateSystemProxy.Definition](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_Definition.md), [UserCoordinateSystems.CreateDefinition](../UserCoordinateSystems/UserCoordinateSystems_CreateDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [UCS by three points](../../sample-programs/UserCoordinateSystems_Add_Sample.md) | This sample demonstrates the creation of a User Coordinate System (UCS) based on 3 points that define the origin, x-direction and y-direction for the UCS. |
| [UCS by transformation matrix](../../sample-programs/UserCoordinateSystems_CreateDefinition_Sample.md) | This sample demonstrates the creation of a user coordinate system (UCS) by specifying a transformation matrix. |

## Version

Introduced in version 2011
