# BIMComponent Object

## Description

BIMComponent object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ExportBuildingComponent](../BIMComponent/BIMComponent_ExportBuildingComponent.md) | Method that exports the BIM component as an adsk, ifc or rfa file. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BIMComponent/BIMComponent_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ComponentDefinition](../BIMComponent/BIMComponent_ComponentDefinition.md) | Read-only property that returns the Inventor PartComponentDefinition or AssemblyComponentDefinition that this BIMComponent object is associated with. |
| [ComponentDescription](../BIMComponent/BIMComponent_ComponentDescription.md) | Read-only property that returns the BIMComponentDescription object associated this document. |
| [ConnectorLinks](../BIMComponent/BIMComponent_ConnectorLinks.md) | Read-only property that returns the collection of connector links for this document. Through the returned object you can access all existing links between connectors and create new links between connectors. |
| [Connectors](../BIMComponent/BIMComponent_Connectors.md) | Read-only property that returns the collection of connectors for this document. Through the returned object you can access all existing connectors and create new connectors. |
| [Type](../BIMComponent/BIMComponent_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.BIMComponent](../AssemblyComponentDefinition/AssemblyComponentDefinition_BIMComponent.md), [BIMComponentPropertySet.Parent](../BIMComponentPropertySet/BIMComponentPropertySet_Parent.md), [BIMConnector.Parent](../BIMConnector/BIMConnector_Parent.md), [BIMExchangeServer.GetBIMComponent](../BIMExchangeServer/BIMExchangeServer_GetBIMComponent.md), [PartComponentDefinition.BIMComponent](../PartComponentDefinition/PartComponentDefinition_BIMComponent.md), [SheetMetalComponentDefinition.BIMComponent](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_BIMComponent.md), [WeldmentComponentDefinition.BIMComponent](../WeldmentComponentDefinition/WeldmentComponentDefinition_BIMComponent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Export to IFC Format Sample](../../sample-programs/ExportToIFCFormatSample_Sample.md) | This sample demonstrates how to export an assembly to IFC format. |

## Version

Introduced in version 2011
