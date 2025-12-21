# FlatPattern.GetEndOfPartPosition Method

Parent Object: [FlatPattern](../FlatPattern/FlatPattern.md)

## Description

Method that returns the current end of part position in the browser in parts and assemblies.

## Syntax

FlatPattern.**GetEndOfPartPosition**( ***After*** As Object, ***Before*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| After | Object | Output object that returns the object after which the end of part is currently positioned. This could return Nothing if there are no features before the end of part in the browser. Valid return objects in part are features, 2d and 3d sketches, all work features and derived part/assembly components. Valid return objects in assembly are features and 2d sketches. |
| Before | Object | Output object that returns the object before which the end of part is currently positioned. This could return Nothing if there are no features after the end of part in the browser. Valid return objects in part are features, 2d and 3d sketches, all work features and derived part/assembly components. Valid return objects in assembly are features and 2d sketches. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |