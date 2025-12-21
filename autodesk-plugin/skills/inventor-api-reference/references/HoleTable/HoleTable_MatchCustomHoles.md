# HoleTable.MatchCustomHoles Method

Parent Object: [HoleTable](../HoleTable/HoleTable.md)

## Description

Method that specifies two or more custom holes (designated with center marks) to be the same.

## Syntax

HoleTable.**MatchCustomHoles**( ***HoleTags*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| HoleTags | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing HoleTag objects that represent center marks. All the hole tags are matched to the first hole tag in the collection. The method returns an error if any of the input hole tags do not represent a center mark. |

## Version

Introduced in version 2009
