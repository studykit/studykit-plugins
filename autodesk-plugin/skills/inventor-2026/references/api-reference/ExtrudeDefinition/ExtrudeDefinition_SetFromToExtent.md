# ExtrudeDefinition.SetFromToExtent Method

Parent Object: [ExtrudeDefinition](../ExtrudeDefinition/ExtrudeDefinition.md)

## Description

Method that changes the extents to be “from and to face” extents.

## Syntax

ExtrudeDefinition.**SetFromToExtent**( ***FromFace*** As Object, ***ExtendFromFace*** As Boolean, ***ToFace*** As Object, ***ExtendToFace*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FromFace | Object | Input Object that defines the “from face”. This can be either a Face or WorkPlane object. |
| ExtendFromFace | Boolean | Input Boolean that defines whether the “from face” should be extended to contain the extents of the profile. |
| ToFace | Object | Input Object that defines the “to face”. This can be either a Face or WorkPlane object. |
| ExtendToFace | Boolean | Input Boolean that defines whether the “to face” should be extended to contain the extents of the profile. |

## Version

Introduced in version 2012
