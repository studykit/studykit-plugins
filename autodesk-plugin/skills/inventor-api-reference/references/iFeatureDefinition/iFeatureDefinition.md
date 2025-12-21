# iFeatureDefinition Object

## Description

The iFeatureDefinition object represents the positional and parameter information of an iFeature.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveTableRow](../iFeatureDefinition/iFeatureDefinition_ActiveTableRow.md) | Gets and sets the row from the table that should be used to specify the sizes for the iFeature instances. |
| [Application](../iFeatureDefinition/iFeatureDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [iFeatureInputs](../iFeatureDefinition/iFeatureDefinition_iFeatureInputs.md) | Property that indicates the input information of the iFeature. |
| [iFeatureTable](../iFeatureDefinition/iFeatureDefinition_iFeatureTable.md) | Property that returns the table information associated with this iFeature. |
| [IsPunchTool](../iFeatureDefinition/iFeatureDefinition_IsPunchTool.md) | Property that specifies if this iFeature has been defined to be used as a punch tool. |
| [IsTableDriven](../iFeatureDefinition/iFeatureDefinition_IsTableDriven.md) | Property that specifies if this iFeature is driven by a table. |
| [PunchId](../iFeatureDefinition/iFeatureDefinition_PunchId.md) | Property that returns the PunchID associated with this iFeature. |
| [Type](../iFeatureDefinition/iFeatureDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[iFeature.iFeatureDefinition](../iFeature/iFeature_iFeatureDefinition.md), [iFeatureProxy.iFeatureDefinition](../iFeatureProxy/iFeatureProxy_iFeatureDefinition.md), [iFeatures.CreateiFeatureDefinition](../iFeatures/iFeatures_CreateiFeatureDefinition.md), [PunchToolFeature.iFeatureDefinition](../PunchToolFeature/PunchToolFeature_iFeatureDefinition.md), [PunchToolFeatureProxy.iFeatureDefinition](../PunchToolFeatureProxy/PunchToolFeatureProxy_iFeatureDefinition.md), [PunchToolFeatures.CreateiFeatureDefinition](../PunchToolFeatures/PunchToolFeatures_CreateiFeatureDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Placement of a standard iFeature](../../sample-programs/iFeatures_Sample.md) | This program demonstrates the placement of a standard iFeature in a part. |
| [Place table driven iFeature](../../sample-programs/iFeatureTable_Sample.md) | This program demonstrates the placement of a table driven iFeature in a part. |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |

## Version

Introduced in version 6
