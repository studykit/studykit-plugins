# MoveFaceDefinition Object

## Description

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../MoveFaceDefinition/MoveFaceDefinition_Copy.md) | Method that creates a copy of this MoveFaceDefinition object. The new MoveFaceDefinition object is independent of any feature. It can edited and used as input to edit an existing feature or to create a new Move Face feature. |
| [SetDirectionAndDistanceMoveType](../MoveFaceDefinition/MoveFaceDefinition_SetDirectionAndDistanceMoveType.md) | Method that sets the move face type to kDirectionAndDistanceMoveType. The move is defined using a direction and a distance along the direction. |
| [SetFreeMoveType](../MoveFaceDefinition/MoveFaceDefinition_SetFreeMoveType.md) | Method that sets the move face type to kFreeMoveType. The move is defined using a matrix that defines the transform to be applies to the face(s). |
| [SetPlanarMoveType](../MoveFaceDefinition/MoveFaceDefinition_SetPlanarMoveType.md) | Method that sets the move face type to kPlanarMoveType. The move is defined using two points, and optionally, a plane for the move. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MoveFaceDefinition/MoveFaceDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AutomaticBlending](../MoveFaceDefinition/MoveFaceDefinition_AutomaticBlending.md) | Gets and sets whether the move operation should propagate to adjacent tangent faces. |
| [Faces](../MoveFaceDefinition/MoveFaceDefinition_Faces.md) | Gets and sets the FaceCollection object that contains the faces that are used to define the Move Face feature. |
| [MoveFaceType](../MoveFaceDefinition/MoveFaceDefinition_MoveFaceType.md) | Property that returns the method used to define the type of the move face operation. The valid values for this property are kDirectionAndDistanceMoveType, kPlanarMoveType, and kFreeMoveType. This property is initialized to kFreeMoveType when the definition is created. Use the MoveFaceTypeDefinition property to get the corresponding definition object. |
| [MoveFaceTypeDefinition](../MoveFaceDefinition/MoveFaceDefinition_MoveFaceTypeDefinition.md) | Property that returns the definition object that defines the type of move. |
| [Parent](../MoveFaceDefinition/MoveFaceDefinition_Parent.md) | Property that returns the parent MoveFaceFeature of this MoveFaceDefinition object. |
| [Type](../MoveFaceDefinition/MoveFaceDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DirectionAndDistanceMoveDefinition.Parent](../DirectionAndDistanceMoveDefinition/DirectionAndDistanceMoveDefinition_Parent.md), [FreeMoveDefinition.Parent](../FreeMoveDefinition/FreeMoveDefinition_Parent.md), [MoveFaceDefinition.Copy](../MoveFaceDefinition/MoveFaceDefinition_Copy.md), [MoveFaceFeature.Definition](../MoveFaceFeature/MoveFaceFeature_Definition.md), [MoveFaceFeatureProxy.Definition](../MoveFaceFeatureProxy/MoveFaceFeatureProxy_Definition.md), [MoveFaceFeatures.CreateDefinition](../MoveFaceFeatures/MoveFaceFeatures_CreateDefinition.md), [PlanarMoveDefinition.Parent](../PlanarMoveDefinition/PlanarMoveDefinition_Parent.md)

## Version

Introduced in version 2011
