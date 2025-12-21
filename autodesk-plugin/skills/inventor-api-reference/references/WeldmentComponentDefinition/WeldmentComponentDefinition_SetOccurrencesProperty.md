# WeldmentComponentDefinition.SetOccurrencesProperty Method

Parent Object: [WeldmentComponentDefinition](../WeldmentComponentDefinition/WeldmentComponentDefinition.md)

## Description

Method that process the property of a collection of occurrences.

## Syntax

WeldmentComponentDefinition.**SetOccurrencesProperty**( ***pOccurrences*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***PropertyName*** As String, ***Value*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pOccurrences | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that contains the ComponentOccurrence objects to set the grounded on. The collection can contain top-level occurrences only, if occurrences within a subassembly are specified then they will be ignored. |
| PropertyName | String | Input String that indicates the property of the occurrences to set. Valid properties include: Grounded. |
| Value | Variant | Input value to set for the occurrences for their property. Valid values for the properties are as below: PropertyName = “Grounded”. Value = Boolean that indicates whether the occurrences are grounded or not. A value of True indicates that their grounded will be turned on. The Occurrences collection can contain top-level occurrences only, if occurrences within a subassembly are specified then they will be ignored. |

## Version

Introduced in version 2022
