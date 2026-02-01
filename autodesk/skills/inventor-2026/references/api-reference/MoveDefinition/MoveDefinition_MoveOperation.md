# MoveDefinition.MoveOperation Property

Parent Object: [MoveDefinition](../MoveDefinition/MoveDefinition.md)

## Description

Property that returns the specified MoveOperation object. They are returned in the same order that they were applied. The MoveOperationCount property can used to determine the number of operations avaialable.

## Syntax

MoveDefinition.**MoveOperation**( ***Index*** As Long ) As [MoveOperation](../MoveOperation/MoveOperation.md)

## Property Value

This is a read only property whose value is a [MoveOperation](../MoveOperation/MoveOperation.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Long value that specifies the MoveOperation to return. The first item in the collection has an index of 1. |

## Version

Introduced in version 2013
