# FlatPattern.GetSheetMetalEntity Method

Parent Object: [FlatPattern](../FlatPattern/FlatPattern.md)

## Description

Returns the corresponding BRep entity (face, edge, etc.) in the sheet metal body given a BRep entity in the flat pattern body. If an entity is not found, the method returns Nothing. If multiple matches are found, an ObjectsEnumerator is returned.

## Syntax

FlatPattern.**GetSheetMetalEntity**( ***FlatPatternEntity*** As Object ) As Object

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FlatPatternEntity | Object |  |

## Version

Introduced in version 2016
