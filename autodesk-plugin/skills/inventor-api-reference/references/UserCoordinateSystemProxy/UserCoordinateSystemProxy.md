# UserCoordinateSystemProxy Object

Derived from: [UserCoordinateSystem](../UserCoordinateSystem/UserCoordinateSystem.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_Delete.md) | Method that deletes the UserCoordinateSystem. |
| [GetReferenceKey](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetEndOfPart](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_SetEndOfPart.md) | Method that repositions the end of part marker relative to the object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_Definition.md) | Property that returns the UserCoordinateSystemDefinition object that can be used to get and set the inputs for the coordinate system and redefine the coordinate system. |
| [HealthStatus](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature (such as a ClientFeature). If True, the OwnedBy property returns the feature. |
| [Name](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_Name.md) | Gets and sets the name of the UserCoordinateSystem. |
| [NativeObject](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Origin](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_Origin.md) | Property that returns the work point that represents the origin of the coordinate system. |
| [OwnedBy](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_OwnedBy.md) | Property that returns the PartFeature object that owns this object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parent](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_Parent.md) | Property that returns the parent ComponentDefinition object. |
| [Transformation](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_Transformation.md) | Gets and sets the transformation matrix for the coordinate system. |
| [Type](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_Visible.md) | Gets and sets the visibility of the coordinate system. |
| [XAngle](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_XAngle.md) | Property that returns the parameter associated with the rotation angle about the x-axis. |
| [XAxis](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_XAxis.md) | Property that returns the work axis that represents the x-axis of the coordinate system. |
| [XOffset](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_XOffset.md) | Property that returns the parameter associated with the X offset value. |
| [XYPlane](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_XYPlane.md) | Property that returns the work plane that represents the X-Y plane of the coordinate system. |
| [XZPlane](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_XZPlane.md) | Property that returns the work plane that represents the X-Z plane of the coordinate system. |
| [YAngle](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_YAngle.md) | Property that returns the parameter associated with the rotation angle about the y-axis. |
| [YAxis](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_YAxis.md) | Property that returns the work axis that represents the y-axis of the coordinate system. |
| [YOffset](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_YOffset.md) | Property that returns the parameter associated with the Y offset value. |
| [YZPlane](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_YZPlane.md) | Property that returns the work plane that represents the Y-Z plane of the coordinate system. |
| [ZAngle](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_ZAngle.md) | Property that returns the parameter associated with the rotation angle about the z-axis. |
| [ZAxis](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_ZAxis.md) | Property that returns the work axis that represents the z-axis of the coordinate system. |
| [ZOffset](../UserCoordinateSystemProxy/UserCoordinateSystemProxy_ZOffset.md) | Property that returns the parameter associated with the Z offset value. |

## Version

Introduced in version 2010
