# Face.GetSourceFace Method

Parent Object: [Face](../Face/Face.md)

## Description

Method that gets the source face that has been overridden by this face. The method returns Nothing if this face is not an override. An error is returned if this method is called on a face in a part.

## Syntax

Face.**GetSourceFace**( [***GetLeafSource***] As Boolean ) As [Face](../Face/Face.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| GetLeafSource | Boolean | Optional input Boolean that specifies whether to get the 'leaf' source face in the case where there are multiple levels of override. If specified to be False, the method returns the next level override face. If not specified, the argument defaults to True indicating that the leaf source will be returned. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |