# RipDefinition Object

## Description

The RipDefinition object represents all of the information that defines a rip feature. The RipDefinition object is used in two ways. First it is used as input when creating a rip feature. Second it is used to query and edit existing rip features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../RipDefinition/RipDefinition_Copy.md) | Method that creates a copy of this RipDefinition object. The new RipDefinition object is independent of any feature. It can be edited and used as input to edit an existing feature or to create a new rip feature. |
| [SetFaceExtentsRipType](../RipDefinition/RipDefinition_SetFaceExtentsRipType.md) | Method that sets the RipDefinition so that it defines a rip that uses the entire rip face to determine the extent of the rip. |
| [SetPointToPointRipType](../RipDefinition/RipDefinition_SetPointToPointRipType.md) | Method that sets the RipDefinition so that it defines a point to point rip. |
| [SetSinglePointRipType](../RipDefinition/RipDefinition_SetSinglePointRipType.md) | Method that sets the RipDefinition so that it defines a single point rip. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../RipDefinition/RipDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../RipDefinition/RipDefinition_Parent.md) | Property that returns the parent rip definition feature. |
| [RipFace](../RipDefinition/RipDefinition_RipFace.md) | Gets and sets the face that the rip is defined along. |
| [RipType](../RipDefinition/RipDefinition_RipType.md) | Property that returns the method used to define the type of rip. The valid values for this property are kSinglePointRipType, kPointToPointRipType, and kFaceExtentsRipType. |
| [RipTypeDefinition](../RipDefinition/RipDefinition_RipTypeDefinition.md) | Property that returns the RipTypeDefinition object that defines the type of rip. |
| [Type](../RipDefinition/RipDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[PointToPointRipTypeDef.Parent](../PointToPointRipTypeDef/PointToPointRipTypeDef_Parent.md), [RipDefinition.Copy](../RipDefinition/RipDefinition_Copy.md), [RipFeature.Definition](../RipFeature/RipFeature_Definition.md), [RipFeatureProxy.Definition](../RipFeatureProxy/RipFeatureProxy_Definition.md), [RipFeatures.CreateRipDefinition](../RipFeatures/RipFeatures_CreateRipDefinition.md), [SinglePointRipTypeDef.Parent](../SinglePointRipTypeDef/SinglePointRipTypeDef_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |

## Version

Introduced in version 2011
