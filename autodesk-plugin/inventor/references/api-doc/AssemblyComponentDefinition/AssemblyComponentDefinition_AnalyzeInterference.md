# AssemblyComponentDefinition.AnalyzeInterference Method

Parent Object: [AssemblyComponentDefinition](../AssemblyComponentDefinition/AssemblyComponentDefinition.md)

## Description

Method that analyzes the interference between two components. The input ObjectCollections contain the component occurrences that are to be checked for interference. If only one set is provided then interference checking is performed between all occurrences provided in the set. If two sets are provided then the overlap between the components of the two collections are calculated.

## Syntax

AssemblyComponentDefinition.**AnalyzeInterference**( ***Set1*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***Set2***] As Variant ) As [InterferenceResults](../InterferenceResults/InterferenceResults.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Set1 | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input that contains ComponentOccurrenceobjects. If this set is provided without Set2, all occurrences in the set are checked for interference against all other occurrences in the set. |
| Set2 | Variant | Optional input that contains ComponentOccurrence objects. When this set is provided the occurrences in Set1 are checked for interference against the occurrences in Set2. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Interference Analysis](../../sample-programs/AssemblyComponentDefinition_AnalyzeInterference_Sample.md) | This sample demonstrates the functions used to calculate interference analysis in an assembly. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |