# iFeatureTemplateDescriptor Object

## Description

The iFeatureTemplateDescriptor object describes the iFeature file that was used to create the iFeature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [DelayReplaceAll](../iFeatureTemplateDescriptor/iFeatureTemplateDescriptor_DelayReplaceAll.md) | Method that flags the ReferenceComponent corresponding to the iFeature as being out of date. The next time this part is opened a message will be displayed to the user notifying them that the iFeature is out of date and allowing them to update it using the file specified. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iFeatureTemplateDescriptor/iFeatureTemplateDescriptor_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [InternalName](../iFeatureTemplateDescriptor/iFeatureTemplateDescriptor_InternalName.md) | Gets the Internal Name (a GUID) for this document. |
| [LastKnownSourceFileName](../iFeatureTemplateDescriptor/iFeatureTemplateDescriptor_LastKnownSourceFileName.md) | Property that returns the name of the iFeature file (.ide) used to create this iFeatureTemplateDescriptor. |
| [Parent](../iFeatureTemplateDescriptor/iFeatureTemplateDescriptor_Parent.md) | Property that returns the parent ComponentDefinition object. |
| [Type](../iFeatureTemplateDescriptor/iFeatureTemplateDescriptor_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[iFeature.iFeatureTemplateDescriptor](../iFeature/iFeature_iFeatureTemplateDescriptor.md), [iFeatureProxy.iFeatureTemplateDescriptor](../iFeatureProxy/iFeatureProxy_iFeatureTemplateDescriptor.md), [iFeatureTemplateDescriptors.Item](../iFeatureTemplateDescriptors/iFeatureTemplateDescriptors_Item.md), [PunchToolFeature.iFeatureTemplateDescriptor](../PunchToolFeature/PunchToolFeature_iFeatureTemplateDescriptor.md), [PunchToolFeatureProxy.iFeatureTemplateDescriptor](../PunchToolFeatureProxy/PunchToolFeatureProxy_iFeatureTemplateDescriptor.md)

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |