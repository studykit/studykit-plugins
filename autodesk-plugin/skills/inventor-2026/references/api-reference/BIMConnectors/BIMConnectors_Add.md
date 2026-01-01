# BIMConnectors.Add Method

Parent Object: [BIMConnectors](../BIMConnectors/BIMConnectors.md)

## Description

Method that creates a new BIMConnector. The type of connector definition supplied will determine the type of connector created. The new BIMConnector is returned.

## Syntax

BIMConnectors.**Add**( ***Definition*** As [BIMConnectorDefinition](../BIMConnectorDefinition/BIMConnectorDefinition.md), [***Name***] As String ) As [BIMConnector](../BIMConnector/BIMConnector.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Definition | [BIMConnectorDefinition](../BIMConnectorDefinition/BIMConnectorDefinition.md) | Input definition object that defines all of the required inputs to create a new connector. |
| Name | String | Defines the name of the new connector. It must be unique with respect to all existing connectors. If not provided, or an empty string is supplied then BIM Exchange will generate a default name. |

## Version

Introduced in version 2011
