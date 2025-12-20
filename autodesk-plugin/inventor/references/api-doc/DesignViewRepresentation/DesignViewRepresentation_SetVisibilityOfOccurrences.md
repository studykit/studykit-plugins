# DesignViewRepresentation.SetVisibilityOfOccurrences Method

Parent Object: [DesignViewRepresentation](../DesignViewRepresentation/DesignViewRepresentation.md)

## Description

Method that sets the visibility of a collection of occurrences. If occurrences within a subassembly are specified and the owning subassembly occurrence is associative to a design view representation, the associativity will be turned off.

## Syntax

DesignViewRepresentation.**SetVisibilityOfOccurrences**( ***Occurrences*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***Visible*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Occurrences | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that contains the ComponentOccurrence objects to set the visibility on. The collection can contain both top-level occurrences and those in subassemblies (ComponentOccurrenceProxy objects). |
| Visible | Boolean | Input Boolean that indicates if the set of occurrences should have the visibility turned off or on. A value of True indicates that their visibility will be turned on. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |