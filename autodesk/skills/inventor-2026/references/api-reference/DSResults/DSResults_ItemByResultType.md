# DSResults.ItemByResultType Property

Parent Object: [DSResults](../DSResults/DSResults.md)

## Description

Gets the specified DSResult object from the collection.

## Syntax

DSResults.**ItemByResultType**( ***ResultType*** As [DSResultTypeEnum](../DSResultTypeEnum.md) ) As [DSResult](../DSResult/DSResult.md)

## Property Value

This is a read only property whose value is a [DSResult](../DSResult/DSResult.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ResultType | [DSResultTypeEnum](../DSResultTypeEnum.md) | Input DSResultTypeEnum value that specifies the type of result to return. If the specified type does not exist then Nothing is returned. |

## Version

Introduced in version 2013
