# BrowserFolder.SetEndOfPart Method

Parent Object: [BrowserFolder](../BrowserFolder/BrowserFolder.md)

## Description

Method that moves the end of part before or after the folder. The method only applies for first level folders in part documents and first level folders in the features portion of the browser in assembly documents. The method returns an error for all other folders.

## Syntax

BrowserFolder.**SetEndOfPart**( ***Before*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Before | Boolean | Input Boolean that specifies whether to move the end of part before or after the folder. True for before. |

## Version

Introduced in version 2010
