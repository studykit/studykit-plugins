# TransientGeometry.CreateMatrix Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new 4x4 Matrix object. The matrix is initialized with an identity matrix.

## Syntax

TransientGeometry.**CreateMatrix**() As [Matrix](../Matrix/Matrix.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding iAssembly occurrences](../../sample-programs/AddiAssemblyMember_Sample.md) | This sample demonstrates adding iAssembly occurrences to an assembly. |
| [Adding iPart occurrences to an assembly](../../sample-programs/AddiPartMember_Sample.md) | This sample demonstrates adding iPart occurrences to an assembly. |
| [Assembly Add Occurrence](../../sample-programs/AddOccurrence_Sample.md) | This sample demonstrates placing an assembly occurrence. |
| [iMate Creation During Occurrence Placement](../../sample-programs/AddUsingiMates_Sample.md) | This sample demonstrates creating multiple iMate results when adding an occurrence into an assembly. This uses the AddUsingiMate method which is the equivalent of using the Place Component command and checking the Use iMate check box on the dialog. |
| [Demote occurence](../../sample-programs/BrowserPaneObject_Reorder_Demote_Sample.md) | This sample demonstrates how to demote a top level occurrence in an assembly into a new sub-assembly occurrence. |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [iMate Result Creation](../../sample-programs/iMateResult_Sample.md) | This sample demonstrates creating an iMate result using two existin iMate definitions. |
| [Create assembly occurrence with representations](../../sample-programs/OccurrenceAddWithOptions_Sample.md) | This sample demonstrates how to create an assembly occurrence by specifying various representations. |
| [UCS by transformation matrix](../../sample-programs/UserCoordinateSystems_CreateDefinition_Sample.md) | This sample demonstrates the creation of a user coordinate system (UCS) by specifying a transformation matrix. |

## Version

Introduced in version 4
