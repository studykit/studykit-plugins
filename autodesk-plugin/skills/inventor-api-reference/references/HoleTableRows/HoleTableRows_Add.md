# HoleTableRows.Add Method

Parent Object: [HoleTableRows](../HoleTableRows/HoleTableRows.md)

## Description

Method that adds a row to the table.

## Syntax

HoleTableRows.**Add**( ***Hole*** As Object ) As [HoleTableRow](../HoleTableRow/HoleTableRow.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Hole | Object | Input object that specifies the hole to be added to the table. This can either be a DrawingCurve object (which represents the geometry of the hole to be added) or a Centermark object. The method returns an error if the input DrawingCurve does not represent a hole. For view based and feature type based hole tables, the method returns an error if the input hole feature type is not included in the hole table. |

## Version

Introduced in version 2009
