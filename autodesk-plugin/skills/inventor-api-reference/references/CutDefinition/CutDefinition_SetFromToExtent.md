# CutDefinition.SetFromToExtent Method

Parent Object: [CutDefinition](../CutDefinition/CutDefinition.md)

## Description

Method that changes the extent to be a 'from to' extent.

## Remarks

Calling this method for a CutDefinition object that was obtained from an existing cut feature will cause the cut feature to update with the change.

## Syntax

CutDefinition.**SetFromToExtent**( ***FromFace*** As Object, ***ExtendFromFace*** As Boolean, ***ToFace*** As Object, ***ExtendToFace*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FromFace | Object | Input Object that defines the 'from face'. This can be either a face or work plane. The same limitations for the 'from' face that exist when creating a cut feature interactively through the command exist when using the API to create a cut feature. |
| ExtendFromFace | Boolean | Input Boolean that defines whether the 'from face' should be extended to contain the extents of the profile. |
| ToFace | Object | Input Object that defines the 'to face'. This can be either a face or work plane. The same limitations for the 'to' plane that exist when creating a cut feature interactively through the command exist when using the API to create a cut feature. |
| ExtendToFace | Boolean | Input Boolean that defines whether the 'to face' should be extended to contain the extents of the profile. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |