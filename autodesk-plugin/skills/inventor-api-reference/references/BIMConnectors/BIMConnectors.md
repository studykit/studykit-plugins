# BIMConnectors Object

## Description

BIMConnectors object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../BIMConnectors/BIMConnectors_Add.md) | Method that creates a new BIMConnector. The type of connector definition supplied will determine the type of connector created. The new BIMConnector is returned. |
| [CreateCableTrayConnectorDefinition](../BIMConnectors/BIMConnectors_CreateCableTrayConnectorDefinition.md) | Method that creates a new cable tray connector definition. The created definition object defines the inputs to create a cable tray connector and is used as input to the Add method of the BIMConnectors object to create a new connector. |
| [CreateConduitConnectorDefinition](../BIMConnectors/BIMConnectors_CreateConduitConnectorDefinition.md) | Method that creates a new conduit connector definition. The created definition object defines the inputs to create a conduit connector and is used as input to the Add method of the BIMConnectors object to create a new conduit connector. |
| [CreateDuctConnectorDefinition](../BIMConnectors/BIMConnectors_CreateDuctConnectorDefinition.md) | Method that creates a new duct connector definition. The created definition object defines the inputs to create a duct connector and is used as input to the Add method of the BIMConnectors object to create a new connector. |
| [CreateElectricalConnectorDefinition](../BIMConnectors/BIMConnectors_CreateElectricalConnectorDefinition.md) | Method that creates a new electrical connector definition. The created definition object defines the inputs to create a electrical connector and is used as input to the Add method of the BIMConnectors object to create a new connector. |
| [CreatePipeConnectorDefinition](../BIMConnectors/BIMConnectors_CreatePipeConnectorDefinition.md) | Method that creates a new pipe connector definition. The created definition object defines the inputs to create a pipe connector and is used as input to the Add method of the BIMConnectors object to create a new connector. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BIMConnectors/BIMConnectors_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../BIMConnectors/BIMConnectors_Count.md) | Gets the number of items in this collection. |
| [Item](../BIMConnectors/BIMConnectors_Item.md) | Returns the specified BIMConnector object from the collection. |
| [Type](../BIMConnectors/BIMConnectors_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BIMComponent.Connectors](../BIMComponent/BIMComponent_Connectors.md)

## Version

Introduced in version 2011
