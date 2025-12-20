# UserCoordinateSystem Object

## Description

The UserCoordinateSystem object represents a user coordinate system.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../UserCoordinateSystem/UserCoordinateSystem_Delete.md) | Method that deletes the UserCoordinateSystem. |
| [GetReferenceKey](../UserCoordinateSystem/UserCoordinateSystem_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../UserCoordinateSystem/UserCoordinateSystem_SetEndOfPart.md) | Method that repositions the end of part marker relative to the object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../UserCoordinateSystem/UserCoordinateSystem_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../UserCoordinateSystem/UserCoordinateSystem_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Definition](../UserCoordinateSystem/UserCoordinateSystem_Definition.md) | Property that returns the UserCoordinateSystemDefinition object that can be used to get and set the inputs for the coordinate system and redefine the coordinate system. |
| [HealthStatus](../UserCoordinateSystem/UserCoordinateSystem_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../UserCoordinateSystem/UserCoordinateSystem_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature (such as a ClientFeature). If True, the OwnedBy property returns the feature. |
| [Name](../UserCoordinateSystem/UserCoordinateSystem_Name.md) | Gets and sets the name of the UserCoordinateSystem. |
| [Origin](../UserCoordinateSystem/UserCoordinateSystem_Origin.md) | Property that returns the work point that represents the origin of the coordinate system. |
| [OwnedBy](../UserCoordinateSystem/UserCoordinateSystem_OwnedBy.md) | Property that returns the PartFeature object that owns this object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parent](../UserCoordinateSystem/UserCoordinateSystem_Parent.md) | Property that returns the parent ComponentDefinition object. |
| [Transformation](../UserCoordinateSystem/UserCoordinateSystem_Transformation.md) | Gets and sets the transformation matrix for the coordinate system. |
| [Type](../UserCoordinateSystem/UserCoordinateSystem_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../UserCoordinateSystem/UserCoordinateSystem_Visible.md) | Gets and sets the visibility of the coordinate system. |
| [XAngle](../UserCoordinateSystem/UserCoordinateSystem_XAngle.md) | Property that returns the parameter associated with the rotation angle about the x-axis. |
| [XAxis](../UserCoordinateSystem/UserCoordinateSystem_XAxis.md) | Property that returns the work axis that represents the x-axis of the coordinate system. |
| [XOffset](../UserCoordinateSystem/UserCoordinateSystem_XOffset.md) | Property that returns the parameter associated with the X offset value. |
| [XYPlane](../UserCoordinateSystem/UserCoordinateSystem_XYPlane.md) | Property that returns the work plane that represents the X-Y plane of the coordinate system. |
| [XZPlane](../UserCoordinateSystem/UserCoordinateSystem_XZPlane.md) | Property that returns the work plane that represents the X-Z plane of the coordinate system. |
| [YAngle](../UserCoordinateSystem/UserCoordinateSystem_YAngle.md) | Property that returns the parameter associated with the rotation angle about the y-axis. |
| [YAxis](../UserCoordinateSystem/UserCoordinateSystem_YAxis.md) | Property that returns the work axis that represents the y-axis of the coordinate system. |
| [YOffset](../UserCoordinateSystem/UserCoordinateSystem_YOffset.md) | Property that returns the parameter associated with the Y offset value. |
| [YZPlane](../UserCoordinateSystem/UserCoordinateSystem_YZPlane.md) | Property that returns the work plane that represents the Y-Z plane of the coordinate system. |
| [ZAngle](../UserCoordinateSystem/UserCoordinateSystem_ZAngle.md) | Property that returns the parameter associated with the rotation angle about the z-axis. |
| [ZAxis](../UserCoordinateSystem/UserCoordinateSystem_ZAxis.md) | Property that returns the work axis that represents the z-axis of the coordinate system. |
| [ZOffset](../UserCoordinateSystem/UserCoordinateSystem_ZOffset.md) | Property that returns the parameter associated with the Z offset value. |

## Accessed From

[BIMComponentDescription.UserCoordinateSystemOrientation](../BIMComponentDescription/BIMComponentDescription_UserCoordinateSystemOrientation.md), [UserCoordinateSystemDefinition.Parent](../UserCoordinateSystemDefinition/UserCoordinateSystemDefinition_Parent.md), [UserCoordinateSystemProxy.NativeObject](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_NativeObject.md), [UserCoordinateSystems.Add](../UserCoordinateSystems/UserCoordinateSystems_Add.md), [UserCoordinateSystems.Item](../UserCoordinateSystems/UserCoordinateSystems_Item.md)

## Derived Classes

[UserCoordinateSystemProxy](../UserCoordinateSystemProxy/UserCoordinateSystemProxy.md)

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