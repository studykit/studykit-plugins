# ImportedComponents Object

## Description

ImportedComponents Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../ImportedComponents/ImportedComponents_Add.md) | Method that creates a new ImportedComponent object using the information supplied by the input ImportedComponentDefinition object. Returns the imported component. |
| [CreateDataExchangeDefinition](../ImportedComponents/ImportedComponents_CreateDataExchangeDefinition.md) | Method that creates a new ImportedComponentDefinition object. Suitable for online import like FDX. |
| [CreateDefinition](../ImportedComponents/ImportedComponents_CreateDefinition.md) | Method that creates a new ImportedComponentDefinition object. The returned definition provides access to all of the items in the file that can be imported. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ImportedComponents/ImportedComponents_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Count](../ImportedComponents/ImportedComponents_Count.md) | Gets the number of items in this collection. |
| [Item](../ImportedComponents/ImportedComponents_Item.md) | Allows integer-indexed access to items in the collection. |
| [Parent](../ImportedComponents/ImportedComponents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../ImportedComponents/ImportedComponents_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[AssemblyComponentDefinition.ImportedComponents](../AssemblyComponentDefinition/AssemblyComponentDefinition_ImportedComponents.md), [ReferenceComponents.ImportedComponents](../ReferenceComponents/ReferenceComponents_ImportedComponents.md), [WeldmentComponentDefinition.ImportedComponents](../WeldmentComponentDefinition/WeldmentComponentDefinition_ImportedComponents.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [ImportedDWGComponent Creation](../../sample-programs/ImportedDWGComponentCreation_Sample.md) | This sample demonstrates how to create an imported DWG component into Inventor part document, and project the DWG entities onto Inventor planar sketch. |

## Version

Introduced in version 2016
