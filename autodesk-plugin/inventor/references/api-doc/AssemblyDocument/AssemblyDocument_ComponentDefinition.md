# AssemblyDocument.ComponentDefinition Property

Parent Object: [AssemblyDocument](../AssemblyDocument/AssemblyDocument.md)

## Description

Property that returns the object associated with this assembly. For a standard assembly document, an AssemblyComponentDefinition object will be returned. For a weldment assembly, a Weldment object.

## Syntax

AssemblyDocument.**ComponentDefinition**() As [AssemblyComponentDefinition](../AssemblyComponentDefinition/AssemblyComponentDefinition.md)

## Property Value

This is a read only property whose value is an [AssemblyComponentDefinition](../AssemblyComponentDefinition/AssemblyComponentDefinition.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding iAssembly occurrences](../../sample-programs/AddiAssemblyMember_Sample.md) | This sample demonstrates adding iAssembly occurrences to an assembly. |
| [Assembly Add Occurrence](../../sample-programs/AddOccurrence_Sample.md) | This sample demonstrates placing an assembly occurrence. |
| [iMate Creation During Occurrence Placement](../../sample-programs/AddUsingiMates_Sample.md) | This sample demonstrates creating multiple iMate results when adding an occurrence into an assembly. This uses the AddUsingiMate method which is the equivalent of using the Place Component command and checking the Use iMate check box on the dialog. |
| [Add assembly insert constraint](../../sample-programs/AssemblyConstraints_AddInsertConstraint_Sample.md) | This sample demonstrates the creation of an assembly insert constraint. |
| [Add assembly mate constraint](../../sample-programs/AssemblyConstraints_AddMateConstraint_Sample.md) | This sample demonstrates the creation of an assembly mate constraint. |
| [Add mate constraint using work planes in parts](../../sample-programs/AssemblyConstraints_AddMateConstraint2_Sample.md) | This sample demonstrates creating a mate constraint between two occurrences using the work planes within those occurrences. |
| [Add mate constraint with limits](../../sample-programs/AssemblyConstraints_AddMateConstraint3_Sample.md) | This sample demonstrates the creation of an assembly mate constraint with maximum and minimum limits defined. |
| [Traverse an Assembly](../../sample-programs/AssemblyTraverse_Sample.md) | This sample shows how to recursively traverse an assembly and get the count of leaf node components and subassemblies. |
| [Exporting the assembly BOM](../../sample-programs/BOMView_Export_Sample.md) | This sample demonstrates exporting the Assembly BOM to an external file. |
| [Client Graphics - Draw Range Box](../../sample-programs/ClientGraphics_Sample.md) | This sample demonstrates the use of client graphics to draw the range box of selected entities. |
| [Create assembly occurrence with representations](../../sample-programs/OccurrenceAddWithOptions_Sample.md) | This sample demonstrates how to create an assembly occurrence by specifying various representations. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |