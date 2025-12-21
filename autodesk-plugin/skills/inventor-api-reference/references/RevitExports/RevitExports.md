# RevitExports Object

## Description

RevitExports Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../RevitExports/RevitExports_Add.md) | Method that creates a new Revit model using the information supplied by the input RevitExportDefinition object. If RevitExportDefinition.EnableUpdating is set to True, the new RevitExport is returned and a browser node will for it. |
| [CreateDefinition](../RevitExports/RevitExports_CreateDefinition.md) | Method that creates a new RevitExportDefinition. The returned definition provides control over the selection of components to be exported, the simplification options to be applied, and aspects of the exact format of the resulting Revit model. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../RevitExports/RevitExports_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Count](../RevitExports/RevitExports_Count.md) | Gets the number of items in this collection. |
| [Item](../RevitExports/RevitExports_Item.md) | Allows integer-indexed access to items in the collection. |
| [Type](../RevitExports/RevitExports_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[AssemblyComponentDefinition.RevitExports](../AssemblyComponentDefinition/AssemblyComponentDefinition_RevitExports.md), [WeldmentComponentDefinition.RevitExports](../WeldmentComponentDefinition/WeldmentComponentDefinition_RevitExports.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Revit Export sample](../../sample-programs/CreateRevitExportSample_Sample.md) | This sample demonstrates how to create a RevitExport object. |

## Version

Introduced in version 2022
