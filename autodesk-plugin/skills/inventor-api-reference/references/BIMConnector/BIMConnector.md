# BIMConnector Object

## Description

BIMConnector object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../BIMConnector/BIMConnector_Delete.md) | Method that deletes the connector. |
| [GetReferenceKey](../BIMConnector/BIMConnector_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BIMConnector/BIMConnector_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Definition](../BIMConnector/BIMConnector_Definition.md) | Read-only property that gets the definition object associated with this connector. |
| [DefinitionType](../BIMConnector/BIMConnector_DefinitionType.md) | Read-only property that returns the type of definition associated with this connector. This property lets you determine what type of connector this object represents. |
| [MissingAttachment](../BIMConnector/BIMConnector_MissingAttachment.md) | Read-only property that returns whether the attachment is missing or not. |
| [Name](../BIMConnector/BIMConnector_Name.md) | Read-write property that gets and sets the displayed name of the connector. This is the name that is visible in the browser and is editable by the end-user. |
| [Parent](../BIMConnector/BIMConnector_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Suppressed](../BIMConnector/BIMConnector_Suppressed.md) | Read-write property that defines whether the connector is suppressed or not. A value of True indicates the connector is suppressed. |
| [Type](../BIMConnector/BIMConnector_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BIMCableTrayConnectorDefinition.Parent](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_Parent.md), [BIMConduitConnectorDefinition.Parent](../BIMConduitConnectorDefinition/BIMConduitConnectorDefinition_Parent.md), [BIMConnectorDefinition.Parent](../BIMConnectorDefinition/BIMConnectorDefinition_Parent.md), [BIMConnectorLink.ConnectorOne](../BIMConnectorLink/BIMConnectorLink_ConnectorOne.md), [BIMConnectorLink.ConnectorTwo](../BIMConnectorLink/BIMConnectorLink_ConnectorTwo.md), [BIMConnectors.Add](../BIMConnectors/BIMConnectors_Add.md), [BIMConnectors.Item](../BIMConnectors/BIMConnectors_Item.md), [BIMDuctConnectorDefinition.Parent](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_Parent.md), [BIMElectricalConnectorDefinition.Parent](../BIMElectricalConnectorDefinition/BIMElectricalConnectorDefinition_Parent.md), [BIMPipeConnectorDefinition.Parent](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_Parent.md)

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |