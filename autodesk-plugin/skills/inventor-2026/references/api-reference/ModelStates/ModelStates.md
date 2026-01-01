# ModelStates Object

## Description

ModelStates Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../ModelStates/ModelStates_Add.md) | Method that creates a new ModelState. The newly created ModelState is returned. |
| [AddSubstitute](../ModelStates/ModelStates_AddSubstitute.md) | Method that creates a new ModelState. The newly created ModelState is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveModelState](../ModelStates/ModelStates_ActiveModelState.md) | Read-only property that returns the active model state for this document. |
| [Application](../ModelStates/ModelStates_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Count](../ModelStates/ModelStates_Count.md) | Gets the number of items in this collection. |
| [ExcelWorkSheet](../ModelStates/ModelStates_ExcelWorkSheet.md) | Read-only property that returns the excel spreadsheet that represents the model states table. |
| [Item](../ModelStates/ModelStates_Item.md) | Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well. |
| [MemberEditScope](../ModelStates/ModelStates_MemberEditScope.md) | Read-write property that gets and sets whether the edits to a member should affect just the active member or all members. |
| [ModelStatesInEdit](../ModelStates/ModelStates_ModelStatesInEdit.md) | Read-write property that gets and sets the model states in edit. |
| [ModelStateTable](../ModelStates/ModelStates_ModelStateTable.md) | Read-only property that gets the ModelStateTable object that represents the model states table. If the ModelStates is from a model state member document then this property will return Nothing. |
| [Parent](../ModelStates/ModelStates_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../ModelStates/ModelStates_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[AssemblyComponentDefinition.ModelStates](../AssemblyComponentDefinition/AssemblyComponentDefinition_ModelStates.md), [ModelStateTable.Parent](../ModelStateTable/ModelStateTable_Parent.md), [PartComponentDefinition.ModelStates](../PartComponentDefinition/PartComponentDefinition_ModelStates.md), [SheetMetalComponentDefinition.ModelStates](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_ModelStates.md), [WeldmentComponentDefinition.ModelStates](../WeldmentComponentDefinition/WeldmentComponentDefinition_ModelStates.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Modify Multiple Model States Sample](../../sample-programs/ModifyMultipleModelStatesSample_Sample.md) | This sample demonstrates how to set multiple but not all model states into edit mode. |

## Version

Introduced in version 2022
