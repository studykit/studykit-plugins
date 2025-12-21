# ComponentOccurrences Object

Derived from: [ComponentOccurrencesEnumerator](../ComponentOccurrencesEnumerator/ComponentOccurrencesEnumerator.md) Object

## Description

Provides access to the objects within an assembly and supports methods to create new occurrences.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../ComponentOccurrences/ComponentOccurrences_Add.md) | Method that creates a new for an existing part or subassembly. This method is the equivalent of the 'Place Component' command. |
| [AddByComponentDefinition](../ComponentOccurrences/ComponentOccurrences_AddByComponentDefinition.md) | Method that creates a new for a new part or subassembly. This method is the equivalent of the 'Create Component' command. |
| [AddCustomiPartMember](../ComponentOccurrences/ComponentOccurrences_AddCustomiPartMember.md) | Method that creates an of an iPartMember in this AssemblyComponentDefinition. The iPartMember is specified by a custom factory and a row in the factory. |
| [AddiAssemblyMember](../ComponentOccurrences/ComponentOccurrences_AddiAssemblyMember.md) | Method that creates an occurrence of an iAssemblyMember in an assembly. The iAssemblyMember is specified by a factory and a row in the factory. |
| [AddiPartMember](../ComponentOccurrences/ComponentOccurrences_AddiPartMember.md) | Method that creates an of an iPartMember in this AssemblyComponentDefinition. The iPartMember is specified by a factory and a row in the factory. |
| [AddUsingiMates](../ComponentOccurrences/ComponentOccurrences_AddUsingiMates.md) | Method that adds a new occurrence into the assembly. This method is the equivalent of using the Place Component command with the "Use iMate" check box checked. The method returns a failure if no matches are found. |
| [AddVirtual](../ComponentOccurrences/ComponentOccurrences_AddVirtual.md) | Method that creates a virtual component definition and adds an occurrence based on that definition. |
| [AddWithOptions](../ComponentOccurrences/ComponentOccurrences_AddWithOptions.md) | Method that creates a new occurrence for an existing part or subassembly. This method is the equivalent of the "Place Component" command. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllLeafOccurrences](../ComponentOccurrences/ComponentOccurrences_AllLeafOccurrences.md) | Return all unique leaf occurrences (optionally filtered to the specified definition) relative to this context. |
| [AllReferencedOccurrences](../ComponentOccurrences/ComponentOccurrences_AllReferencedOccurrences.md) | Property that returns all occurrences that reference the input object. |
| [Count](../ComponentOccurrences/ComponentOccurrences_Count.md) | Property that returns the number of items in this collection. |
| [Item](../ComponentOccurrences/ComponentOccurrences_Item.md) | Allows integer-indexed access to objects in the collection. |
| [ItemByName](../ComponentOccurrences/ComponentOccurrences_ItemByName.md) | Allows string-indexed access to items in the collection. (Usually found when this ability has been added to a pre-existing collection). |
| [Type](../ComponentOccurrences/ComponentOccurrences_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.Occurrences](../AssemblyComponentDefinition/AssemblyComponentDefinition_Occurrences.md), [ComponentDefinition.Occurrences](../ComponentDefinition/ComponentDefinition_Occurrences.md), [FlatPattern.Occurrences](../FlatPattern/FlatPattern_Occurrences.md), [PartComponentDefinition.Occurrences](../PartComponentDefinition/PartComponentDefinition_Occurrences.md), [SheetMetalComponentDefinition.Occurrences](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_Occurrences.md), [VirtualComponentDefinition.Occurrences](../VirtualComponentDefinition/VirtualComponentDefinition_Occurrences.md), [WeldmentComponentDefinition.Occurrences](../WeldmentComponentDefinition/WeldmentComponentDefinition_Occurrences.md), [WeldsComponentDefinition.Occurrences](../WeldsComponentDefinition/WeldsComponentDefinition_Occurrences.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding iAssembly occurrences](../../sample-programs/AddiAssemblyMember_Sample.md) | This sample demonstrates adding iAssembly occurrences to an assembly. |
| [Adding iPart occurrences to an assembly](../../sample-programs/AddiPartMember_Sample.md) | This sample demonstrates adding iPart occurrences to an assembly. |
| [Assembly Add Occurrence](../../sample-programs/AddOccurrence_Sample.md) | This sample demonstrates placing an assembly occurrence. |
| [iMate Creation During Occurrence Placement](../../sample-programs/AddUsingiMates_Sample.md) | This sample demonstrates creating multiple iMate results when adding an occurrence into an assembly. This uses the AddUsingiMate method which is the equivalent of using the Place Component command and checking the Use iMate check box on the dialog. |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Create assembly occurrence with representations](../../sample-programs/OccurrenceAddWithOptions_Sample.md) | This sample demonstrates how to create an assembly occurrence by specifying various representations. |

## Version

Introduced in version 4
